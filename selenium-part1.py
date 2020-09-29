from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

driver = webdriver.Chrome('/Users/raj454raj/Downloads/chromedriver')
driver.get("https://github.com")
driver.maximize_window()

team_element = driver.find_elements_by_class_name("HeaderMenu-link")[1]
team_element.click()

elements = driver.find_elements_by_class_name("team-resource")
elements[0].click()
time.sleep(3)
print(driver.title)
driver.quit()
