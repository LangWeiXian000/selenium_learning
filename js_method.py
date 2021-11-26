from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep,ctime
from selenium.webdriver import ActionChains


class testCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://sahitest.com/demo/formTest.htm")
        # self.driver.get("https://www.baidu.com/")
        # print("设置浏览器宽800、高600显示")
        # self.driver.maximize_window()
        # self.driver.set_window_size(800, 600)  # 控制浏览器的大小

    #执行这个方法需要更换为百度的网址
    def test_js_methods(self):
        sleep(2)
        self.driver.find_element(By.ID,'kw').send_keys('seleniumm')#输入内容
        self.driver.find_element(By.ID,'su').click()
        js = 'window.scrollTo(200,450)'#第一个参数表示水平的左边距，第二个参数表示垂直的上边距
        self.driver.execute_script(js)# 这个方法通过js设置浏览器窗口滚动条的位置
        sleep(2)
        self.driver.quit()


    def test_js_methods2(self):
        alert = self.driver.switch_to.alert  # 获取弹窗
        sleep(2)
        print(alert.text)  # 获取弹窗的文本
        alert.accept()  # 接收弹框
        sleep(2)
        #定义输入的内容
        input_text = "selenium"
        js = "document.querySelector('textarea').value='"+ input_text + "';"#将输入的内容与js拼接
        print(js)
        self.driver.execute_script(js)
        sleep(5)
        self.driver.quit()


if __name__ == '__main__':
    case = testCase()
    case.test_js_methods2()