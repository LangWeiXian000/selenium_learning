from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


class testCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.126.com/")
        print("设置浏览器宽480、高800显示")
        self.driver.set_window_size(480, 800)  # 控制浏览器的大小
        sleep(3)
        self.driver.maximize_window()

    def test_switch_frame(self):
        login_frame = self.driver.find_element(By.CSS_SELECTOR,'iframe[id^="x-URS-iframe"]')
        self.driver.switch_to_frame(login_frame)#切换到iframe
        self.driver.find_element(By.NAME,'email').send_keys('1234567@126.COM')
        sleep(2)
        self.driver.find_element(By.NAME,'password').send_keys("123456")
        self.driver.find_element(By.ID,'un-login').click()
        # self.driver.find_element(By.ID,'dologin').click()
        sleep(2)
        self.driver.switch_to.default_content()#切换回iframe框外的页面
        self.driver.find_element(By.ID,'prevTheme').click()
        sleep(2)
        self.driver.quit()




if __name__ == '__main__':
    case = testCase()
    case.test_switch_frame()