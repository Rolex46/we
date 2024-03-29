from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("http://3.139.109.244/")
driver.maximize_window()
try:
    # Wait for the page to load with a specific condition (e.g., element visibility)
    wait = WebDriverWait(driver, 10)  # 10 seconds timeout
    wait.until(EC.presence_of_element_located((By.ID, "name")))
    driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[1]/div/button').click()
    # Find form elements using more specific locators
    name_input = driver.find_element(By.ID, "name")
    email_input = driver.find_element(By.ID, "email")
    message_input = driver.find_element(By.ID, "message")
    # Fill the form fields
    name_input.send_keys(" Name")
    email_input.send_keys("email@example.com")
    message_input.send_keys("message")
    # Assuming a submit button (uncomment if present):
    submit_button = driver.find_element(By.XPATH, '//*[@id="contact"]/form/button')
    submit_button.click()
    time.sleep(2)  # Adjust the wait time as needed
except Exception as e:
    print("Error:", e)
# driver.quit()