from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize Chrome driver
driver = webdriver.Chrome()
driver.maximize_window()

# Open the login page
driver.get("https://the-internet.herokuapp.com/login")

# Enter credentials
driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

# ✅ Correct locator for Login button
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# Wait for message to appear
time.sleep(2)
message = driver.find_element(By.ID, "flash").text
print("Message:", message.strip())

# Close browser
driver.quit()
