from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class testCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://tyuni.weixiao.qq.com/")
        print("设置浏览器宽480、高800显示")
        self.driver.set_window_size(480, 800)  # 控制浏览器的大小
        time.sleep(3)

#控制浏览器前进或后退
    def test_fallback(self):
        self.driver.maximize_window()  # 将浏览器窗口最大化
        time.sleep(2)
        self.driver.find_element(By.XPATH,'//*[@id="route-root"]/div/div/header/section/div[2]/a[1]').click()
        time.sleep(2)
        self.driver.back()#回退到上一个页面
        time.sleep(2)
        self.driver.forward()#回退后再前进到之前的页面
        time.sleep(2)
        self.driver.quit()

    def test_refresh(self):
        self.driver.maximize_window()  # 将浏览器窗口最大化
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="route-root"]/div/div/header/section/div[2]/a[1]').click()
        self.driver.refresh()#刷新当前页面
        time.sleep(2)
        self.driver.quit()

if __name__ =='__main__':
    case = testCase()
    # case.test_fallback()
    case.test_refresh()



