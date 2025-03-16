import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from urls import Urls


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MainPageLocators()

    @allure.step("Скроллим до вопроса")
    def scroll_to_question(self, question_index):
        question_locator = self.locators.get_question_locator(question_index)
        self.scroll_to_element(question_locator)

    @allure.step("Кливакаем на вопрос")
    def click_on_question(self, question_index):
        question_locator = self.locators.get_question_locator(question_index)
        self.click_on_element(question_locator)

    @allure.step("Ответ на вопрос виден")
    def answer_is_displayed(self, question_index):
        answer_locator = self.locators.get_answer_locator(question_index)
        element = self.find_element(answer_locator)
        return element.is_displayed()

    @allure.step("Кликаем на кнопку 'Заказать' в хэдэре")
    def click_upper_order_button(self):
        self.click_on_element(self.locators.UPPER_ORDER_BUTTON)

    @allure.step("Отображается заголовок формы Про Аренду ")
    def form_header_is_displayed(self):
        return self.visibility_of_element(self.locators.FORM_HEADER)

    @allure.step("Кликаем нижнюю кнопку Заказать")
    def click_lower_order_button(self):
        self.click_on_element(self.locators.LOWER_ORDER_BUTTON)

    @allure.step("Скроллим до нижней кнопки Заказать")
    def scroll_to_order_button(self):
        self.scroll_to_element(self.locators.LOWER_ORDER_BUTTON)

    @allure.step("Отображается первый вопрос на главной странице")
    def click_logo_samokat(self):
        self.click_on_element(self.locators.UPPER_ORDER_BUTTON)
        self.click_on_element(self.locators.SAMOKAT_LOGO)
        self.scroll_to_element(self.locators.QUESTION_1)
        return self.visibility_of_element(self.locators.QUESTION_1)

    @allure.step("Перейти на новую вкладку")
    def switch_to_new_tab(self):
        original_window = self.current_window_handle()
        wait = self.wait()
        self.click_on_element(self.locators.YANDEX_LOGO)
        wait.until(EC.number_of_windows_to_be(2))
        for window_handle in self.window_handles():
            if window_handle != original_window:
                self.switch_to_window(window_handle)
                break
        wait.until(EC.url_to_be(Urls.ZEN_URL))
        return self.current_url()
