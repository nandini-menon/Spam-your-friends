import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com")
time.sleep(30)
elem = driver.find_element_by_class_name("input-search")
elem.clear()
elem.send_keys("Friend's name as stored in your phone")
elem.send_keys(Keys.RETURN)
for i in range (0,100):
	msg = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
	msg.clear()
	msg.send_keys("Message you want to send")
	msg.send_keys(Keys.RETURN)
driver.close()
