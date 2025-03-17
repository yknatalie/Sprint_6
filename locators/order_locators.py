from selenium.webdriver.common.by import By


class OrderLocators():
    COOKIE = By.XPATH, ".//button[@class='App_CookieButton__3cvqF']"
    UPPER_ORDER_BUTTON = By.XPATH, ".//button[@class='Button_Button__ra12g']"
    NAME = By.XPATH, ".//input[@placeholder='* Имя']"
    SURNAME = By.XPATH, ".//input[@placeholder='* Фамилия']"
    ADDRESS = By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']"
    SUBWAY_STATION = By.XPATH, ".//input[@placeholder='* Станция метро']"
    CHERKIZOVSKAYA_STATION = By.XPATH, ".//div[text()='Черкизовская']"
    PHONE = By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']"
    NEXT_BUTTON = By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"
    ARRIVE_TIME = By.XPATH, ".//input[@placeholder='* Когда привезти самокат']"
    RENT_DURATION = By.XPATH, ".//div[@class='Dropdown-placeholder']"
    RENT_ONE_DAY = By.XPATH, ".//div[@class='Dropdown-menu']/div[text()='сутки']"
    RENT_TWO_DAYS = By.XPATH, ".//div[@class='Dropdown-menu']/div[text()='двое суток']"
    BLACK_COLOR = By.XPATH, ".//input[@id='black']"
    GRAY_COLOR = By.XPATH, ".//input[@id='grey']"
    FORM_ORDER_BUTTON = By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"
    YES_BUTTON = By.XPATH, ".//button[text()='Да']"
    ORDER_IS_DONE_WINDOW = By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ']"
