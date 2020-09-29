from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

class FuntionalTestRunner:
    def __init__(self, test_type="local", platform="desktop"):
        self.test_type = test_type
        self.platform = platform
        self.driver = self.get_driver()

    def get_desired_caps(self):
        build_name = "Sample testing Github"
        build = "Test "
        # Only required for remote tests
        if self.platform == "mobile":
            return {
                'browserName': 'iPhone',
                'device': 'iPhone 11',
                'realMobile': 'true',
                'os_version': '13.0',
                'name': build_name,
                'build': build
            }
        else:
            return {
                'os_version': 'Catalina',
                'resolution': '1920x1080',
                'browser': 'Chrome',
                'browser_version': 'latest',
                'os': 'OS X',
                'name': build_name,
                'build': build
            }

    def get_driver(self):
        if self.test_type == "local":
            return webdriver.Chrome('/Users/raj454raj/Downloads/chromedriver')
        else:
            return webdriver.Remote(
                     command_executor='http://%s:%s@hub-cloud.browserstack.com/wd/hub' % (os.environ["automate_username"],
                                                                                          os.environ["automate_authkey"]),
                     desired_capabilities=self.get_desired_caps()
                   )

    def run_test(self):
        driver = self.driver
        driver.get("https://github.com")
        if self.platform == "mobile":
            buttons = driver.find_elements_by_tag_name("button")
            for button in buttons:
                if button.get_attribute("aria-label") == "Toggle navigation":
                    button.click()
                    break
            time.sleep(5)
        else:
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

    def run_session(self):
        try:
            self.run_test()
        except Exception as e:
            print(e)
            self.driver.quit()

runner = FuntionalTestRunner("remote", "mobile")
runner.run_session()
