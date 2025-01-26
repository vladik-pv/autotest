from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/ajax")
driver.implicitly_wait(16)

driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()

content = driver.find_element(By.CSS_SELECTOR, "#content")
txt = content.find_element(By.CSS_SELECTOR, "p.bg-success").text
print(txt)

driver.quit()
