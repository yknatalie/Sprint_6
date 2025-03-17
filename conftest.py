from selenium import webdriver
import pytest
from urls import Urls


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get(Urls.SAMOKAT_URL)
    yield driver
    driver.quit()
