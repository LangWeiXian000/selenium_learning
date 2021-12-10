from selenium import webdriver
from selenium.webdriver.support.expected_conditions import NoSuchElementException
from selenium.webdriver.common.by import By
import time

class WebDriver(object):
    def __init__(self,driver):
        self.driver = driver

    def findElement(self,*loc):
        '''单个定位元素的方法'''
        try:
            return self.driver.find_element(*loc)
        except NoSuchElementException as e:
            print("error Details{0}".format(e.args[0]))

    def findsElement(self,*loc):
        try:
            return self.driver.find_elements(*loc)
        except NoSuchElementException as e:
            print("error Details{0}".format(e.args[0]))