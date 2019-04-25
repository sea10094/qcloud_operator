#-*- coding: utf-8 -*-
import time

from selenium import webdriver
url='https://graph.qq.com/oauth2.0/show?which=Login&display=pc&client_id=101488968&response_type=code&redirect_uri=https%3A%2F%2Fcloud.tencent.com%2Flogin%2FqqAccessCallback%3Fs_url%3Dhttps%253A%252F%252Fconsole.cloud.tencent.com%252Fcdb%26fwd_flag%3D7&state=BkruSfEIF4'
option = webdriver.ChromeOptions()
option.add_argument('--no-sandbox')
option.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=option)
driver.get(url)
driver.switch_to_frame('ptlogin_iframe')
driver.find_element_by_id('switcher_plogin').click()
driver.find_element_by_id("u").clear()
driver.find_element_by_id("u").send_keys('$user')
driver.find_element_by_id("p").clear()
driver.find_element_by_id("p").send_keys('$password')
driver.find_element_by_id("login_button").click()
time.sleep(3)
print(driver.get_cookie('skey'))
driver.quit()

