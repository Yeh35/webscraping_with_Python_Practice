from selenium import webdriver
browser = webdriver.Chrome()

browser.maximize_window() #창 최대화

url = "https://flight.naver.com/"
browser.get(url)

#가는 날 선택
elem = browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]")
print(elem)
elem.click()

#이번달 27일, 28일 선택
calender = browser.find_element_by_class_name("modal_modal__1rTeN")
calender.find_element_by_link_text("27").click()
calender.find_element_by_link_text("28").click()

#browser.quit()

