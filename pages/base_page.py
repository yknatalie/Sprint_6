import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage():
    def __init__(self, driver):
        self.driver = driver

    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    def fill_input(self, locator, text):
        self.wait_visibility_of_element(locator)
        self.driver.find_element(*locator).send_keys(text)

    def wait_visibility_of_element(self, locator):
        return WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(locator))

    def scroll_to_element(self, locator):
        self.driver.execute_script("arguments[0].scrollIntoView();",
                                   self.driver.find_element(*locator))

    def visibility_of_element(self, locator):
        return self.driver.find_element(*locator).is_displayed()
