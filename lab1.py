from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Set up ChromeDriver automatically
service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
# options.add_argument("--headless")  # Uncomment if you don’t want the browser to pop up
driver = webdriver.Chrome(service=service, options=options)

try:
    driver.get("https://www.wikipedia.org/")

    # Search for Selenium (software)
    search_box = driver.find_element(By.NAME, "search")
    search_box.send_keys("Selenium (software)")
    search_box.send_keys(Keys.RETURN)

    # Wait until the first *non-empty* paragraph in the article is found
    paragraphs = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.mw-parser-output > p"))
    )

    first_paragraph_text = ""
    for p in paragraphs:
        text = p.text.strip()
        if text:
            first_paragraph_text = text
            break

    print("\nFirst Paragraph:\n", first_paragraph_text)

finally:
    driver.quit()
