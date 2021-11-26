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
        sleep(3)

    '''切换浏览器窗口'''
    def test_window_handles(self):
        self.driver.maximize_window()  # 将浏览器窗口最大化
        sleep(2)
        self.driver.find_element(By.LINK_TEXT,'新闻').click()
        sleep(2)
        print(self.driver.current_url)
        all_handle = self.driver.window_handles
        self.driver.switch_to.window(all_handle[-1])
        sleep(2)
        print(self.driver.current_url)
        self.driver.quit()

    '''刷新当前页面 & 控制浏览器前进或后退'''
    def test_refresh(self):
        self.driver.maximize_window()  # 将浏览器窗口最大化
        sleep(2)
        self.driver.find_element(By.LINK_TEXT, '新闻').click()
        sleep(2)
        all_handle = self.driver.window_handles
        self.driver.switch_to.window(all_handle[-1])
        self.driver.find_element(By.XPATH, '//*[@id="channel-all"]/div/ul/li[3]/a').click()
        self.driver.back()  # 回退到上一个页面
        sleep(2)
        self.driver.forward()  # 回退后再前进到之前的页面
        sleep(2)
        self.driver.refresh()  # 刷新当前页面
        sleep(2)
        self.driver.quit()

    # 操作元素的一些方法
    def test_element_methods(self):
        size = self.driver.find_element(By.XPATH, '//*[@id="s-top-left"]/a[1]').size
        print(size)  # 获取元素的尺寸
        self.driver.find_element(By.XPATH, '//*[@id="s-top-left"]/a[1]').click()
        text = self.driver.find_element(By.XPATH, '//*[@id="s-top-left"]/a[1]').text
        print(text)  # 获取元素的文本
        attribute = self.driver.find_element(By.XPATH, '//*[@id="s-top-left"]/a[1]').get_attribute('class')
        print(attribute)  # 获取元素的class属性值，还可以是type、id、name等任意属性
        result = self.driver.find_element(By.XPATH, '//*[@id="s-top-left"]/a[1]').is_displayed()
        print(result)  # 查看这个元素是否可见，返回ture或者False
        '''
        webdriver中元素的常用方法
        clear()清除文本
        send_keys(value)模拟按键输入
        click()点击元素
        submit()有些搜索框不提供搜索按钮，而是通过键盘上的回车键完成搜索内容的提交，就可以用这个
        size 返回元素的尺寸
        text 获取元素的文本
        get_attribute(name) 获取属性值
        is_displayed() 设置该元素是否用户可见
        '''

    def test_Action_methods(self):
        self.driver.maximize_window()
        sleep(2)
        above = self.driver.find_element(By.ID, 's-usersetting-top')  # 找到
        ActionChains(self.driver).move_to_element(above).perform()
        self.driver.find_element(By.XPATH, '//*[@id="s-user-setting-menu"]/div/a[1]').click()
        sleep(2)
        self.driver.quit()
        ''''
        ActionChains类的鼠标操作方法
        perform()执行ActionChains类中存储的所有行为
        context_click()右击
        double_click()双击
        drag_and_drop()拖动
        move_to_element()鼠标悬停
        '''


if __name__ == '__main__':
    case = testCase()
    # case.test_window_handles()
    # case.test_refresh()
    # case.test_element_methods()
    # case.test_Action_methods()

