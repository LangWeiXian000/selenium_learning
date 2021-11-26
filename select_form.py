from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

class testCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://sahitest.com/demo/selectTest.htm")
        print("设置浏览器宽480、高800显示")
        self.driver.set_window_size(480, 800)  # 控制浏览器的大小
        sleep(3)
        self.driver.maximize_window()

    def test_select(self):
        sel = self.driver.find_element(By.XPATH,'//*[@id="s1Id"]')#先定位到下拉框
        # print(sel)
        # Select(sel).select_by_value('o1')#根据下拉框的value属性进行选择
        # sleep(2)
        # Select(sel).select_by_visible_text("o1")#根据下拉框的文本进行选择
        sleep(2)
        Select(sel).select_by_index(2)#根据下拉框的索引进行选择
        sleep(2)
        self.driver.quit()

    def test_select2(self):
        sel = self.driver.find_element(By.XPATH, '//*[@id="s1"]')
        sleep(2)
        Select(sel).select_by_value('-1')
        sleep(2)
        self.driver.quit()

if __name__ == '__main__':
    case = testCase()
    # case.test_select()
    case.test_select2()