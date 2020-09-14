import chromedriver_binary
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://example.selenium.jp/reserveApp/')

# 宿泊日の変更
year_element = driver.find_element_by_id('reserve_year')
year_element.clear()
year_element.send_keys('2020')

month_element = driver.find_element_by_id('reserve_month')
month_element.clear()
month_element.send_keys('9')

day_element = driver.find_element_by_id('reserve_day')
day_element.clear()
day_element.send_keys('20')

term_element = driver.find_element_by_id('reserve_term')
term_element.clear()
term_element.send_keys('2')

# 人数の変更
headcount_element = driver.find_element_by_id('headcount')
headcount_element.clear()
headcount_element.send_keys('3')

# プランの選択
plan_element = driver.find_element_by_id('plan_a')
plan_element.click()

# 名前の入力
name_element = driver.find_element_by_id('guestname')
name_element.send_keys('<your_name>')

# 次へをクリック
next_button = driver.find_element_by_id('goto_next')
next_button.click()

# 確定をクリック
commit_button = driver.find_element_by_id('commit')
commit_button.click()
