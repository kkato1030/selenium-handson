import chromedriver_binary
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('<test_site_url>')

# 名前の入力
input_elements = driver.find_elements_by_css_selector('<copied_selector>')
username_element = input_elements[0]
username_element.send_keys('TestUser-1')

# パスワードの入力
input_elements = driver.find_elements_by_css_selector('<copied_selector>')
username_element = input_elements[0]
username_element.send_keys('Passw0rd!')

# ログイン
input_elements = driver.find_elements_by_css_selector('#login > input')
login_button = input_elements[0]
login_button.click()
