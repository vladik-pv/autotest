from selenium import webdriver
from form_main import DataTypesPage
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_data_types_form(browser):
    page = DataTypesPage(browser)
    page.open()

    # Заполнение формы
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
        company="SkyPro"
    )

    # Отправка формы  
    page.submit_form()  
    assert page.is_zip_code_highlighted_red(By.ID, 'zip-code'), "Поле Zip code не подсвечено красным"  

    fields_to_check = [  
        "first-name", "last-name", "address", "e-mail", "phone",  
        "city", "country", "job-position", "company"  
    ]  

    for field in fields_to_check:  
        assert page.is_field_highlighted_green(field), f"Поле {field} не подсвечено зеленым"  

    browser.quit()
