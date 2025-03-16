import allure
import pytest
from selenium import webdriver
from calculator_page import CalculatorPage

@pytest.fixture
def browser():
    """
    Фикстура для инициализации и завершения работы браузера.
    """
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@allure.feature("Проверка калькулятора")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Тест функциональности калькулятора")
@allure.description("Этот тест проверяет функциональность калькулятора, включая сложение чисел.")
def test_calculator(browser):
    """
    Тест для проверки функциональности калькулятора.
    """
    calculator_page = CalculatorPage(browser)

    with allure.step("Открыть страницу калькулятора"):
        calculator_page.open()
    
    with allure.step("Установить задержку в 45 секунд"):
        calculator_page.set_delay("45")
    
    with allure.step("Выполнить сложение чисел 7 и 8"):
        calculator_page.click_button_7()
        calculator_page.click_plus()
        calculator_page.click_button_8()
        calculator_page.click_equals()
    
    with allure.step("Проверить, что результат равен 15"):
        result_text = calculator_page.get_result()
        assert result_text == "15", (
            f"Ожидаемый результат: 15, Фактический результат: {result_text}"
        )
