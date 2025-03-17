from locators.order_locators import OrderLocators
from pages.base_page import BasePage
import allure


class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderLocators()

    @allure.step("Заполняем все поля в части формы 'Для кого самокат'")
    def make_order_first_part(self, name, surname, address, phone):
        self.click_on_element(self.locators.COOKIE)
        self.click_on_element(self.locators.UPPER_ORDER_BUTTON)
        self.fill_input(self.locators.NAME, name)
        self.fill_input(self.locators.SURNAME, surname)
        self.fill_input(self.locators.ADDRESS, address)
        self.click_on_element(self.locators.SUBWAY_STATION)
        self.wait_visibility_of_element(self.locators.CHERKIZOVSKAYA_STATION)
        self.click_on_element(self.locators.CHERKIZOVSKAYA_STATION)
        self.fill_input(self.locators.PHONE, phone)
        self.click_on_element(self.locators.NEXT_BUTTON)

    @allure.step("Заполняем все поля в части формы 'Про аренду'")
    def make_order_second_part(self, arrival_time):
        self.fill_input(self.locators.ARRIVE_TIME, arrival_time)
        self.click_on_element(self.locators.BLACK_COLOR)
        self.click_on_element(self.locators.RENT_DURATION)
        self.click_on_element(self.locators.RENT_ONE_DAY)
        self.click_on_element(self.locators.FORM_ORDER_BUTTON)
        self.click_on_element(self.locators.YES_BUTTON)

    @allure.step("Отображается окно с номером заказа")
    def window_is_visible(self):
        return self.visibility_of_element(self.locators.ORDER_IS_DONE_WINDOW)
