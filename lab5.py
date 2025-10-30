from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the Chrome driver
driver = webdriver.Chrome()
driver.maximize_window()

# Open Google
driver.get("https://www.google.com")

# Wait a bit to ensure the page fully loads
time.sleep(2)

# Capture and save screenshot
driver.save_screenshot("google.png")

print("✅ Screenshot saved successfully as google.png")

# Close the browser
driver.quit()
