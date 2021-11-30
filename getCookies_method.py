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

    def test_getCookie(self):
        cookie = self.driver.get_cookies()
        print(cookie)
        sleep(2)
        self.driver.quit()

    def test_addCookie(self):
        self.driver.add_cookie({'name': '123', 'value': 'aaa'})
        for cookie in self.driver.get_cookies():
            print(" %s -> %s " % (cookie['name'], cookie['value']))

    def test_deleteCookie(self):
        cookie = self.driver.get_cookies()
        print(cookie)
        self.driver.add_cookie({'name': '123', 'value': 'aaa'})#添加cookie
        for cookie in self.driver.get_cookies():
            print(" %s : %s " % (cookie['name'], cookie['value']))
        self.driver.delete_cookie({'name':'123'})#删除指定cookie
        self.driver.delete_all_cookies()#清除浏览器所有cookie



if __name__ == '__main__':
    case = testCase()
    case.test_deleteCookie()