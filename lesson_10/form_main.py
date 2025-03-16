from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DataTypesPage:

    URL = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"

    # Локаторы элементов
    FIRST_NAME_FIELD = (By.NAME, "first-name")
    LAST_NAME_FIELD = (By.NAME, "last-name")
    ADDRESS_FIELD = (By.NAME, "address")
    EMAIL_FIELD = (By.NAME, "e-mail")
    PHONE_FIELD = (By.NAME, "phone")
    CITY_FIELD = (By.NAME, "city")
    ZIP_CODE_FIELD = (By.NAME, "zip-code")
    COUNTRY_FIELD = (By.NAME, "country")
    JOB_POSITION_FIELD = (By.NAME, "job-position")
    COMPANY_FIELD = (By.NAME, "company")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    def __init__(self, driver: WebDriver) -> WebDriver:
        """
        Инициализирует экземпляр страницы с формой.

        :param driver: Экземпляр веб-драйвера (например, Chrome, Firefox).
        """

        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open(self):
        """
        Открывает страницу формы в браузере.
        """
        self.driver.get(self.URL)

    def fill_form(self, first_name, last_name, address, email, phone, city, zip_code, country, job_position, company) -> str:
        """
        Заполняет форму данными.

        :param first_name: Имя.
        :param last_name: Фамилия.
        :param address: Адрес.
        :param email: Электронная почта.
        :param phone: Телефон.
        :param city: Город.
        :param zip_code: Почтовый индекс.
        :param country: Страна.
        :param job_position: Должность.
        :param company: Компания.
        """
        self.driver.find_element(*self.FIRST_NAME_FIELD).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME_FIELD).send_keys(last_name)
        self.driver.find_element(*self.ADDRESS_FIELD).send_keys(address)
        self.driver.find_element(*self.EMAIL_FIELD).send_keys(email)
        self.driver.find_element(*self.PHONE_FIELD).send_keys(phone)
        self.driver.find_element(*self.CITY_FIELD).send_keys(city)
        self.driver.find_element(*self.ZIP_CODE_FIELD).send_keys(zip_code)
        self.driver.find_element(*self.COUNTRY_FIELD).send_keys(country)
        self.driver.find_element(*self.JOB_POSITION_FIELD).send_keys(job_position)
        self.driver.find_element(*self.COMPANY_FIELD).send_keys(company)

    def submit_form(self):
        """
        Отправляет форму.
        """
        self.driver.find_element(*self.SUBMIT_BUTTON).click()

    def is_zip_code_highlighted_red(self, by, selector) -> str:
        """
        Проверяет, выделено ли поле ZIP-кода красным цветом.

        :param by: Метод поиска элемента (например, By.NAME, By.ID).
        :param selector: Селектор элемента.
        :return: True, если поле выделено красным цветом, иначе False.
        """
        zip_code_field = self.wait.until(
            EC.presence_of_element_located((by, selector))
        )
        return "alert-danger" in zip_code_field.get_attribute("class")

    def is_field_highlighted_green(self, field_name) -> str:
        """
        Проверяет, выделено ли указанное поле зеленым цветом.

        :param field_name: Имя поля (ID элемента).
        :return: True, если поле выделено зеленым цветом, иначе False.
        """
        element = self.wait.until(
            EC.presence_of_element_located((By.ID, field_name))
        )
        return "alert-success" in element.get_attribute("class")
    
