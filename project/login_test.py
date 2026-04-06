from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Open browser
driver = webdriver.Chrome()

# Open login page
driver.get("https://the-internet.herokuapp.com/login")

# Enter username
driver.find_element(By.ID, "username").send_keys("tomsmith")

# Enter password
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

# Click login button
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# Wait for 2 seconds
time.sleep(2)

# Check result
if "secure" in driver.current_url:
    print("LOGIN SUCCESS ✅")
else:
    print("LOGIN FAILED ❌")

# Close browser
driver.quit()