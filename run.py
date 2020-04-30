from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
options = webdriver.ChromeOptions()
options.add_argument("user-agent=CUSTOM_USER-AGENT")
driver = webdriver.Chrome('Webdriver PATH', chrome_options = options)
title = "제목"
content="내용"
uesr_id = "ID"
uesr_pw= "PW"
gall = "Target Gall URL"

driver.get("https://dcinside.com")
driver.find_element_by_xpath('//*[@id="user_id"]').send_keys(uesr_id)
driver.find_element_by_xpath('//*[@id="pw"]').send_keys(user_pw)
driver.find_element_by_xpath('//*[@id="login_ok"]').click()
driver.get(gall)
time.sleep(3)
driver.find_element_by_xpath('//*[@id="btn_write"]').click()
time.sleep(5)
driver.find_element_by_xpath('/html/body/div[2]/main/section/article[2]/form/div[1]/fieldset/div/input').send_keys(title)
driver.switch_to_frame(driver.find_element_by_xpath("//iframe[@name='tx_canvas_wysiwyg']"))
driver.find_element_by_tag_name('body').send_keys(content)
driver.switch_to_default_content()
time.sleep(10)
driver.find_element_by_xpath("/html/body/div[2]/main/section/article[2]/form/div[5]/button[2]").click()

