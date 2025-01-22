from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/classattr")

floating_button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")
floating_button.click()

time.sleep(2)

driver.quit()
