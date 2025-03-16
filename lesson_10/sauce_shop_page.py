from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class SauceDemoPage:
    def __init__(self, browser) -> WebDriver:
        """
        Инициализирует экземпляр страницы Sauce Demo.

        :param browser: Экземпляр веб-драйвера (например, Chrome, Firefox).
        """
        self.browser = browser
        self.url = "https://www.saucedemo.com/"
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.item_button = (By.XPATH, "//div[text()='{item_name}']/ancestor::div[@class='inventory_item']//button")
        self.cart_link = (By.CLASS_NAME, "shopping_cart_link")
        self.checkout_button = (By.ID, "checkout")
        self.first_name_field = (By.ID, "first-name")
        self.last_name_field = (By.ID, "last-name")
        self.zip_code_field = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_label = (By.CLASS_NAME, "summary_total_label")

    def open(self):
        """
        Открытие страници в браузере.
        """
        self.browser.get(self.url)

    def login(self, username, password) -> str:
        """
        Выполняет вход в систему.

        :param username: Имя пользователя.
        :param password: Пароль.
        """
        self.browser.find_element(*self.username_field).send_keys(username)
        self.browser.find_element(*self.password_field).send_keys(password)
        self.browser.find_element(*self.login_button).click()

    def add_item_to_cart(self, item_name) -> str:
        """
        Добавляет товар в корзину.

        :param item_name: Название товара.
        """
        item_xpath = (self.item_button[0], self.item_button[1].format(item_name=item_name))
        self.browser.find_element(*item_xpath).click()

    def go_to_cart(self):
        """
        Переход в корзину.
        """
        self.browser.find_element(*self.cart_link).click()

    def checkout(self):
        """
        Оформление заказа.
        """
        self.browser.find_element(*self.checkout_button).click()

    def fill_shipping_info(self, first_name, last_name, zip_code) -> str:
        """
        Заполняет информацию о доставке.

        :param first_name: Имя.
        :param last_name: Фамилия.
        :param zip_code: Почтовый индекс.
        """
        self.browser.find_element(*self.first_name_field).send_keys(first_name)
        self.browser.find_element(*self.last_name_field).send_keys(last_name)
        self.browser.find_element(*self.zip_code_field).send_keys(zip_code)
        self.browser.find_element(*self.continue_button).click()

    def get_total_amount(self) -> str:
        """
        Возвращает общую сумму заказа.

        :return: Общая сумма заказа.
        """
        total_element = self.browser.find_element(*self.total_label)
        total_text = total_element.text
        return total_text.split()[-1]
    