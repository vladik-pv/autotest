from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/textinput")

element = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
element.send_keys("SkyPro")
element = driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()

name_button = driver.find_element(By.CSS_SELECTOR, "#updatingButton").text
print(name_button)

driver.quit
