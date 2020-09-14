import chromedriver_binary
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://loginsite-20200913164532-hostingbucket-dev.s3-website-ap-northeast-1.amazonaws.com/')

# 名前の入力
input_elements = driver.find_elements_by_css_selector('#login > div:nth-child(1) > div > input')
username_element = input_elements[0]
username_element.send_keys('TestUser-1')

# パスワードの入力
input_elements = driver.find_elements_by_css_selector('#login > div:nth-child(2) > div > input')
password_element = input_elements[0]
password_element.send_keys('Passw0rd!')

# ログイン
input_elements = driver.find_elements_by_css_selector('#login > input')
login_button = input_elements[0]
login_button.click()

# スクリーンショット
driver.save_screenshot('./screenshot.png')
