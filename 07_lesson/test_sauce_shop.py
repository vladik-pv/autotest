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
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_shopping_flow(browser):
    # Создаем экземпляр SauceDemoPage
    sauce_demo_page = SauceDemoPage(browser)
    
    # Открываем страницу Sauce Demo
    sauce_demo_page.open()
    
    # Логинимся
    sauce_demo_page.login(USERNAME, PASSWORD)
    
    # Добавляем товары в корзину
    items_to_add = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie"
    ]
    for item_name in items_to_add:
        sauce_demo_page.add_item_to_cart(item_name)
    
    # Переходим в корзину
    sauce_demo_page.go_to_cart()
    
    # Начинаем оформление заказа
    sauce_demo_page.checkout()
    
    # Заполняем информацию о доставке
    sauce_demo_page.fill_shipping_info(FIRST_NAME, LAST_NAME, ZIP_CODE)
    
    # Получаем итоговую сумму и проверяем ее
    total_value = sauce_demo_page.get_total_amount()
    assert total_value == EXPECTED_TOTAL, (
        f"Ожидаемая сумма: {EXPECTED_TOTAL}, Фактическая сумма: {total_value}"
    )
    