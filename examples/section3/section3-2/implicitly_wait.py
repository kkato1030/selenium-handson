import chromedriver_binary
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(30)
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
input_elements = driver.find_elements_by_css_selector('<copied_selector>')
login_button = input_elements[0]
login_button.click()

# 情報取得
input_elements = driver.find_elements_by_css_selector('<copied_selector>')
get_info_button = input_elements[0]
get_info_button.click()
