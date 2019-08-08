from selenium.webdriver.remote.webdriver import WebDriver

#  BasePage是通用父类page，完成driver的传递
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver: WebDriver = driver

    def find(self, locator, value):
        if value == None:
            self.driver.find_element(*locator)
        else:
            self.driver.find_element(locator, value)

    def click_by_js(self, by, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.
                                            element_to_be_clickable((by, locator)))
        #  添加隐式等待
        self.driver.execute_script("arguments[0].click();",
                                   self.driver.find_element(by, locator)
                                   )
