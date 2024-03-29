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
driver.get("https://dis.ecitizen.go.ke/auth/login")
try:
    # Wait for the page to load with a specific condition (e.g., element visibility)
    wait = WebDriverWait(driver, 10)  # 10 seconds timeout
    wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="vue-root"]/div/div[2]/div/div/div[1]/a')))
    # Assuming a submit button (uncomment if present):
    submit_button = driver.find_element(By.XPATH, '//*[@id="vue-root"]/div/div[2]/div/div/div[1]/a')
    submit_button.click()
    driver.find_element(By.ID, 'login_username').send_keys('254762521894')
    driver.find_element(By.ID, 'login_pwd').send_keys('')
    driver.find_element(By.XPATH, '//*[@id="login"]/div/div[5]/button').click()
    time.sleep(2)  # Adjust the wait time as needed
except Exception as e:
    print("Error:", e)
# driver.quit()