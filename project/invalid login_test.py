from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/login")

# Enter wrong username & password
driver.find_element(By.ID, "username").send_keys("wrong")
driver.find_element(By.ID, "password").send_keys("wrong")

# Click login
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

time.sleep(2)

if "Your username is invalid!" in driver.page_source:
    print("INVALID LOGIN TEST PASSED ✅")
else:
    print("TEST FAILED ❌")

driver.quit()
# Check error message