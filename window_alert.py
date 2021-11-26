from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

class testCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com/")
        print("设置浏览器宽480、高800显示")
        self.driver.set_window_size(480, 800)  # 控制浏览器的大小
        sleep(3)
        self.driver.maximize_window()

        #百度首页的设置
    def test_alert(self):
        above = self.driver.find_element(By.ID,'s-usersetting-top')#找到设置元素
        ActionChains(self.driver).move_to_element(above).perform()#移动鼠标到该元素上
        sleep(2)
        self.driver.find_element(By.XPATH,'//*[@id="s-user-setting-menu"]/div/a[1]').click()#点击搜索设置
        sleep(2)
        self.driver.find_element(By.XPATH,'//*[@id="se-setting-7"]/a[2]').click()#点击保存设置
        sleep(2)
        alert = self.driver.switch_to.alert#获取弹窗
        alert_text = alert.text
        print(alert_text)#获取弹窗的文本
        sleep(2)
        alert.accept()#接收弹框
        sleep(2)
        self.driver.quit()

if __name__ == '__main__':
    case = testCase()
    case.test_alert()
