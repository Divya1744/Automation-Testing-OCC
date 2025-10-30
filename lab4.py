from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize Chrome driver
driver = webdriver.Chrome()
driver.maximize_window()

# Open the webpage
driver.get("https://the-internet.herokuapp.com/checkboxes")

# Wait for page to load
time.sleep(2)

# Find all checkboxes
checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")

# Check each checkbox if not already selected
for idx, cb in enumerate(checkboxes, start=1):
    if not cb.is_selected():
        cb.click()
    print(f"Checkbox {idx} -> Checked:", cb.is_selected())

# Wait a bit to see result before closing
time.sleep(2)
driver.quit()
