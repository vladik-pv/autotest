from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get('http://the-internet.herokuapp.com/add_remove_elements/')

add_button = driver.find_element(By.CSS_SELECTOR, 'button')
for _ in range(5):
    add_button.click()

time.sleep(2)

delete_buttons = driver.find_elements(By.CSS_SELECTOR, 'button.added-manually')

time.sleep(2)

print(f'Количество кнопок Delete: {len(delete_buttons)}')

driver.get("http://uitestingplayground.com/dynamicid")

blue_button = driver.find_element(By.CSS_SELECTOR, "button.btn")
blue_button.click()

time.sleep(2)

time.sleep(2)

driver.get("http://uitestingplayground.com/classattr")

floating_button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")
floating_button.click()

time.sleep(2)

driver.quit()
