import allure
import pytest
from selenium import webdriver
from sauce_shop_page import SauceDemoPage

# Константы
USERNAME = "standard_user"
PASSWORD = "secret_sauce"
FIRST_NAME = "John"
LAST_NAME = "Doe"
ZIP_CODE = "12345"
EXPECTED_TOTAL = "$58.29"

@pytest.fixture
def browser():
    """
    Фикстура для инициализации и завершения работы браузера.
    """
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@allure.feature("Процесс покупки")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Тест процесса покупки на сайте Sauce Demo")
@allure.description("Этот тест проверяет процесс покупки на сайте Sauce Demo,\
 включая вход в систему, добавление товаров в корзину,\
 оформление заказа и проверку итоговой суммы.")
def test_shopping_flow(browser):
    """
    Тест для проверки процесса покупки на сайте Sauce Demo.
    """
    sauce_demo_page = SauceDemoPage(browser)
    
    with allure.step("Открыть страницу Sauce Demo"):
        sauce_demo_page.open()
    
    with allure.step("Войти в систему"):
        sauce_demo_page.login(USERNAME, PASSWORD)
    
    with allure.step("Добавить товары в корзину"):
        items_to_add = [
            "Sauce Labs Backpack",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Onesie"
        ]
        for item_name in items_to_add:
            sauce_demo_page.add_item_to_cart(item_name)
    
    with allure.step("Перейти в корзину"):
        sauce_demo_page.go_to_cart()
    
    with allure.step("Начать оформление заказа"):
        sauce_demo_page.checkout()
    
    with allure.step("Заполнить информацию о доставке"):
        sauce_demo_page.fill_shipping_info(FIRST_NAME, LAST_NAME, ZIP_CODE)
    
    with allure.step("Проверить итоговую сумму"):
        total_value = sauce_demo_page.get_total_amount()
        assert total_value == EXPECTED_TOTAL, (
            f"Ожидаемая сумма: {EXPECTED_TOTAL}, Фактическая сумма: {total_value}"
        )

    