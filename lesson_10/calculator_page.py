from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    def __init__(self, browser) -> WebDriver:
        """
        Инициализирует экземпляр страницы калькулятора.

        :param browser: Chrome
        """
        self.browser = browser
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.screen = (By.CSS_SELECTOR, ".screen")
        self.button_7 = (By.XPATH, "//span[text()='7']")
        self.button_8 = (By.XPATH, "//span[text()='8']")
        self.button_plus = (By.XPATH, "//span[text()='+']")
        self.button_equals = (By.XPATH, "//span[text()='=']")

    def open(self):
        """
        Открывает страницу калькулятора в браузере.
        """
        self.browser.get(self.url)

    def set_delay(self, delay) -> str:
        """
        Устанавливает задержку для калькулятора.

        :param delay: Значение задержки в секундах.
        """
        delay_element = self.browser.find_element(*self.delay_input)
        delay_element.clear()
        delay_element.send_keys(delay)

    def click_button_7(self):
        """
        Нажимает кнопку '7' на калькуляторе.
        """
        self.browser.find_element(*self.button_7).click()

    def click_button_8(self):
        """
        Нажимает кнопку '8' на калькуляторе.
        """
        self.browser.find_element(*self.button_8).click()

    def click_plus(self):
        """
        Нажимает кнопку '+' на калькуляторе.
        """
        self.browser.find_element(*self.button_plus).click()

    def click_equals(self):
        """
        Нажимает кнопку '=' на калькуляторе.
        """
        self.browser.find_element(*self.button_equals).click()

    def get_result(self) -> str:
        """
        Ожидает и возвращает результат вычисления на экране калькулятора.
        :return: Текст результата на экране.
        """
        wait = WebDriverWait(self.browser, 50)
        wait.until(EC.text_to_be_present_in_element(self.screen, "15"))
        return self.browser.find_element(*self.screen).text
    