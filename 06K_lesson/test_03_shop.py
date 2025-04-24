import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


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
    browser.get("https://www.saucedemo.com/")

    browser.find_element(By.ID, "user-name").send_keys(USERNAME)
    browser.find_element(By.ID, "password").send_keys(PASSWORD)
    browser.find_element(By.ID, "login-button").click()

    items_to_add = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie"
    ]

    for item_name in items_to_add:
        item_xpath = f"//div[text()='{
            item_name
            }']/ancestor::div[@class='inventory_item']//button"
        browser.find_element(By.XPATH, item_xpath).click()

    browser.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    browser.find_element(By.ID, "checkout").click()

    browser.find_element(By.ID, "first-name").send_keys(FIRST_NAME)
    browser.find_element(By.ID, "last-name").send_keys(LAST_NAME)
    browser.find_element(By.ID, "postal-code").send_keys(ZIP_CODE)
    browser.find_element(By.ID, "continue").click()

    total_element = browser.find_element(By.CLASS_NAME, "summary_total_label")
    total_text = total_element.text
    total_value = total_text.split()[-1]

    assert total_value == EXPECTED_TOTAL, f"Ожидаемая сумма: {
        EXPECTED_TOTAL
        }, Фактическая сумма: {total_value}"
