from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# browser = webdriver.Chrome("./chromedriver.exe")
browser = webdriver.Chrome()
browser.get("https://naver.com")

elem = browser.find_element_by_class_name("link_login")
elem.click()

time.sleep(3)

# browser.find_element_by_id("id").send_keys("naver_id")
browser.find_element_by_id("id").send_keys("naver_id")
time.sleep(1)
browser.find_element_by_id("pw").send_keys("naver_password")
time.sleep(1)
browser.find_element_by_id("log.login").click()
time.sleep(3)

# ID 새로 입력
browser.find_element_by_id("id").clear() 
time.sleep(1)
browser.find_element_by_id("id").send_keys("myID")

# HTML 정보 출력
print(browser.page_source)

# 특정한 xpth가 로딩될 때까지 기다리기(최대 10초)
try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "xpth"))) 
    # 성공 동작
    print(elem.text)
finally:
    browser.quit()
