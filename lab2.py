from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Setup ChromeDriver automatically
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    driver.get("https://www.amazon.in/")

    # Search for laptops
    search_box = driver.find_element(By.ID, "twotabsearchtextbox")
    search_box.send_keys("laptop")
    search_box.send_keys(Keys.RETURN)

    # Wait until results load
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "span.a-size-medium.a-color-base.a-text-normal"))
    )

    # Fetch the first 5 product titles
    products = driver.find_elements(By.CSS_SELECTOR, "span.a-size-medium.a-color-base.a-text-normal")[:5]

    print("\nTop 5 Laptop Results:\n")
    for idx, product in enumerate(products, start=1):
        print(f"{idx}. {product.text}")

finally:
    driver.quit()
