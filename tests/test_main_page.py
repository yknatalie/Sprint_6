from pages.main_page import MainPage
from urls import Urls
import allure
import pytest


class TestMainPage:
    @allure.title("При нажатии на стрелку вопроса открывается соответствующий тест")
    @pytest.mark.parametrize("question_index", range(8))
    def test_questions(self, driver, question_index):
        page = MainPage(driver)
        page.scroll_to_question(question_index)
        page.click_on_question(question_index)
        assert page.answer_is_displayed(question_index)

    @allure.title("Тестируем кнопку Заказать в хэдере")
    def test_upper_order_button(self, driver):
        upper_button = MainPage(driver)
        upper_button.click_upper_order_button()
        assert upper_button.form_header_is_displayed()

    @allure.title("Тестируем кнопку Заказать внизу страницы")
    def test_lower_order_button(self, driver):
        lower_button = MainPage(driver)
        lower_button.scroll_to_order_button()
        lower_button.click_lower_order_button()
        assert lower_button.form_header_is_displayed()

    @allure.title("При клике на лого Самокат вверху страницы возвращаемся на главную страницу")
    def test_samokat_logo(self, driver):
        page = MainPage(driver)
        assert page.click_logo_samokat()

    @allure.title("При клике на лого Яндекс вверху страницы открывается новая вкладка Дзена")
    def test_yandex_logo(self, driver):
        yandex_logo = MainPage(driver)
        assert yandex_logo.switch_to_new_tab() == Urls.ZEN_URL
