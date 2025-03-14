from pages.order_page import OrderPage
import allure
import pytest
from data import Data


class TestOrderPage:
    @pytest.mark.parametrize("name,surname,address,phone,arrival_time", [Data.data_1, Data.data_2])
    def test_make_order(self, driver, name, surname, address, phone, arrival_time):
        order_page = OrderPage(driver)
        order_page.make_order_first_part(name, surname, address, phone)
        order_page.make_order_second_part(arrival_time)
        assert order_page.window_is_visible()
