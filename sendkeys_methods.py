from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep,ctime
from selenium.webdriver import ActionChains


class testCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com/")
        print("设置浏览器宽480、高800显示")
        self.driver.set_window_size(480, 800)  # 控制浏览器的大小


    def test_keys_methods(self):
        self.driver.maximize_window()
        sleep(2)
        self.driver.find_element(By.ID,'kw').send_keys('seleniumm')#输入内容
        sleep(2)
        '''删除多余的m'''
        self.driver.find_element(By.ID,'kw').send_keys(Keys.BACK_SPACE)
        sleep(2)
        self.driver.find_element(By.ID,'kw').clear()#清空input框
        sleep(2)
        '''输入空格+教程'''
        self.driver.find_element(By.ID,'kw').send_keys(Keys.SPACE)
        self.driver.find_element(By.ID,'kw').send_keys("教程")
        sleep(2)
        '''Ctrl+a,全选'''
        self.driver.find_element(By.ID,'kw').send_keys(Keys.CONTROL,'a')
        sleep(2)
        '''ctrl+x,剪切'''
        self.driver.find_element(By.ID,'kw').send_keys(Keys.CONTROL,'x')
        sleep(2)
        '''ctrl+v,粘贴'''
        self.driver.find_element(By.ID,'kw').send_keys(Keys.CONTROL,'v')
        sleep(2)
        '''回车，代替单击操作'''
        self.driver.find_element(By.ID,'kw').send_keys(Keys.ENTER)
        sleep(2)
        self.driver.quit()




if __name__ == '__main__':
    case = testCase()
    case.test_keys_methods()
