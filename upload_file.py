import os
from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By

file_path = os.path.abspath('./files/')
driver = webdriver.Chrome()
upload_page = 'file:///' + file_path + 'upfile.html'
driver.get(upload_page)
driver.find_element(By.ID,'file').send_keys(file_path + 'test.txt')