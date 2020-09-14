import chromedriver_binary
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://example.selenium.jp/reserveApp/')

# 名前の入力
name_element = driver.find_element_by_id('guestname')
name_element.send_keys('<your_name>')

# プランの選択
plan_element = driver.find_element_by_id('plan_a')
plan_element.click()

# 宿泊日の変更
day_element = driver.find_element_by_id('reserve_day')
day_element.clear()
day_element.send_keys('20')
