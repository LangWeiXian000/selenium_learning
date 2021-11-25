from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep,ctime
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchFrameException


class testCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com/")
        print("设置浏览器宽480、高800显示")
        self.driver.set_window_size(480, 800)  # 控制浏览器的大小
        sleep(3)
        self.driver.maximize_window()

    def test_wait(self):
        print(ctime())
        for i in range(10):
            try:
                el = self.driver.find_element(By.ID,'kw')
                if el.is_displayed():
                    break
            except:
                pass
            sleep(2)
        else:
            print('time out')
        print(ctime())
        self.driver.quit()


    def test_wait2(self):
        self.driver.find_element(By.LINK_TEXT,'新闻').click()
        '''隐式等待，不影响脚本的运行速度。不是固定的等待时间，在设置的等待时间里寻找元素，
        如果元素存在则继续执行，如果定位不到元素，在等待时间内将以轮询的方式不断判断元素是否存在'''
        self.driver.implicitly_wait(20)
        all_handle = self.driver.window_handles
        self.driver.switch_to.window(all_handle[-1])
        print(self.driver.current_url)
        try:
            print(ctime())
            self.driver.find_element(By.NAME,'word222').send_keys('selenium')
        except NoSuchFrameException as msg:
            print(msg)
        finally:
            print(ctime())
        self.driver.quit()

    def test_elements(self):
        self.driver.find_element(By.ID,'kw').send_keys('selenium')
        self.driver.find_element(By.ID,'su').click()
        sleep(2)
        #定位一组元素
        texts = self.driver.find_elements(By.XPATH,"//div[@tpl='se_com_default']/h3/a")
        #计算结果个数
        print(len(texts))
        #循环遍历每一条搜索结果的标题
        for t in texts:
            print(t.text)
        self.driver.quit()




if __name__ == '__main__':
    case = testCase()
    case.test_elements()
