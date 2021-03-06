# Assertion script with all three CTAs' title text assertion - iphone 11 breaking maximize_window

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

desired_capabilities = {
    'browserName': 'iPhone',
    'device': 'iPhone 11',
    'realMobile': 'true',
    'os_version': '13.0',
    'name': 'selenium-part4',
    'build': 'Test Github teams page - IIIT'
}

driver = webdriver.Remote(
            command_executor='http://%s:%s@hub-cloud.browserstack.com/wd/hub' % (os.environ["automate_username"],
                                                                                 os.environ["automate_authkey"]),
            desired_capabilities=desired_capabilities
         )
driver.get("https://github.com")
driver.maximize_window()

team_element = driver.find_elements_by_class_name("HeaderMenu-link")[1]
team_element.click()
time.sleep(2)

elements = driver.find_elements_by_class_name("team-resource")
expected_page_titles = ["GitHub Actions Cheat Sheet | GitHub Resources",
                        "Collaboration is the key to DevOps success | GitHub Resources",
                        "Culture matters: How healthy teams build better software | GitHub Resources"]

assert(len(elements) == 3)

iterator = 0
for i in range(len(elements)):
    element = driver.find_elements_by_class_name("team-resource")[i]
    element.click()
    time.sleep(3)
    print(driver.title)
    assert(driver.title == expected_page_titles[i])
    iterator += 1
    driver.back()
    time.sleep(1)

driver.quit()
