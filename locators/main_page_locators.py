from selenium.webdriver.common.by import By


class MainPageLocators:
    def get_question_locator(self, index):
        return By.ID, f'accordion__heading-{index}'

    def get_answer_locator(self, index):
        return By.ID, f'accordion__panel-{index}'

    QUESTION_1 = By.XPATH, ".//div[text()='Сколько это стоит? И как оплатить?']"

    UPPER_ORDER_BUTTON = By.XPATH, ".//button[@class='Button_Button__ra12g']"
    LOWER_ORDER_BUTTON = By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"

    FORM_HEADER = By.XPATH, ".//div[@class='Order_Header__BZXOb']"

    SAMOKAT_LOGO = By.XPATH, "//img[@alt='Scooter']"
    YANDEX_LOGO = By.XPATH, "//img[@alt='Yandex']"
