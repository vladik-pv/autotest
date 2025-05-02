import pytest
from selenium import webdriver
from calculator_page import CalculatorPage

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_calculator(browser):
    calculator_page = CalculatorPage(browser)
    
    # Открываем страницу калькулятора
    calculator_page.open()
    
    # Устанавливаем задержку
    calculator_page.set_delay("45")
    
    # Выполняем действия на калькуляторе
    calculator_page.click_button_7()
    calculator_page.click_plus()
    calculator_page.click_button_8()
    calculator_page.click_equals()
    
    # Получаем результат и проверяем его
    result_text = calculator_page.get_result()
    assert result_text == "15", (
        f"Ожидаемый результат: 15, Фактический результат: {result_text}"
    )
