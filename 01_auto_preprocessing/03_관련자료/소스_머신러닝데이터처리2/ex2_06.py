﻿from selenium import webdriver

driver = webdriver.Chrome('F:/chromedriver_win32/chromedriver')
driver.implicitly_wait(3)

driver.get("http://en.wikipedia.org")

driver.execute_script("window.alert('하이!! selenium!!')")