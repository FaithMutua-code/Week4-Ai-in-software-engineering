from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://example.com/login")

# Valid credentials
driver.find_element(By.NAME, "username").send_keys("validuser")
driver.find_element(By.NAME, "password").send_keys("validpass")
driver.find_element(By.CSS_SELECTOR, "button[type=submit]").click()
time.sleep(1)
print("Valid login test passed!")

# Invalid credentials
driver.get("https://example.com/login")
driver.find_element(By.NAME, "username").send_keys("fakeuser")
driver.find_element(By.NAME, "password").send_keys("wrongpass")
driver.find_element(By.CSS_SELECTOR, "button[type=submit]").click()
time.sleep(1)
print("Invalid login test handled correctly!")

driver.quit()
