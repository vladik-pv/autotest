import allure
from selenium import webdriver
from form_main import DataTypesPage
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture
def browser():
    """
    Фикстура для инициализации и завершения работы браузера.
    """
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@allure.feature("Проверка формы")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Тест функциональности формы")
@allure.description("Этот тест проверяет функциональность формы, включая заполнение полей, отправку формы и проверку подсветки полей.")
def test_data_types_form(browser):
    """
    Тест для проверки функциональности формы.
    """
    page = DataTypesPage(browser)
    
    with allure.step("Открыть страницу формы"):
        page.open()
    
    with allure.step("Заполнить форму данными"):
        page.fill_form(
            first_name="Иван",
            last_name="Петров",
            address="Ленина, 55-3",
            email="test@skypro.com",
            phone="+7985899998787",
            city="Москва",
            zip_code="",
            country="Россия",
            job_position="QA",
            company="Skypro"
        )
    
    with allure.step("Отправить форму"):
        page.submit_form()
    
    with allure.step("Проверить, что поле Zip code подсвечено красным"):
        assert page.is_zip_code_highlighted_red(By.ID, 'zip-code'), "Поле Zip code не подсвечено красным"
    
    with allure.step("Проверить, что остальные поля подсвечены зеленым"):
        fields_to_check = [
            "first-name", "last-name", "address", "e-mail", "phone",
            "city", "country", "job-position", "company"
        ]
        for field in fields_to_check:
            assert page.is_field_highlighted_green(field), f"Поле {field} не подсвечено зеленым"
    
    with allure.step("Завершить работу браузера"):
        browser.quit()
