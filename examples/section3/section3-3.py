import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait  # 追記
from selenium.webdriver.support import expected_conditions  # 追記
from selenium.webdriver.common.by import By # 追記
import time

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

#待機時間設定
wait = WebDriverWait(driver, 30)

#指定したボタンが表示されクリック出来る状態になるまで待機する
css_selector = 'body > div > section > div > div > button'
wait.until(expected_conditions.element_to_be_clickable((By. CSS_SELECTOR, css_selector)))

# 情報取得
input_elements = driver.find_elements_by_css_selector(css_selector)
get_info_button = input_elements[0]
get_info_button.click()

# スクリーンショット
driver.save_screenshot('./screenshot.png')
driver.close()
