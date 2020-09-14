import chromedriver_binary
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://example.selenium.jp/reserveApp/')

# 名前の入力
name_element = driver.find_element_by_id('guestname')
print(name_element)
