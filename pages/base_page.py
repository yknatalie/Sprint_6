import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage():
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Находим элемент")
    def find_element(self,locator):
        return self.driver.find_element(*locator)

    @allure.step("Кликаем на элемент")
    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step("Заполняем поле ввода")
    def fill_input(self, locator, text):
        self.wait_visibility_of_element(locator)
        self.driver.find_element(*locator).send_keys(text)

    @allure.step("Дожидаемся пока элемент станет видимым")
    def wait_visibility_of_element(self, locator):
        return WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(locator))

    @allure.step("Скроллим до элемента")
    def scroll_to_element(self, locator):
        self.driver.execute_script("arguments[0].scrollIntoView();",
                                   self.driver.find_element(*locator))

    @allure.step("Элемент виден")
    def visibility_of_element(self, locator):
        return self.driver.find_element(*locator).is_displayed()

    @allure.step("Текущий дескриптор окна")
    def current_window_handle(self):
        return self.driver.current_window_handle

    @allure.step("Ожидание")
    def wait(self):
        return WebDriverWait(self.driver, 10)

    @allure.step("Все открытые вкладки")
    def window_handles(self):
        return self.driver.window_handles

    @allure.step("Делаем другую вкладку текущей")
    def switch_to_window(self, window):
        self.driver.switch_to.window(window)

    @allure.step("Текущий url")
    def current_url(self):
        return self.driver.current_url
