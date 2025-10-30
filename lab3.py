from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Initialize the Chrome driver
driver = webdriver.Chrome()
driver.maximize_window()

# Open the website
driver.get("https://the-internet.herokuapp.com/dropdown")

# Wait a bit for the page to load
time.sleep(2)

# Locate the dropdown
dropdown = Select(driver.find_element(By.ID, "dropdown"))

# Select "Option 2"
dropdown.select_by_visible_text("Option 2")

# Print the selected option
print("Selected:", dropdown.first_selected_option.text)

# Close the browser
time.sleep(2)
driver.quit()
