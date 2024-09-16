from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get("https://tezzasolutions.com")
driver.maximize_window()

error_count = 0
start_time = time.time()

try:
    nav_item = driver.find_element(By.LINK_TEXT, "https://tezza1234.com")  # this is a deliberate error
    nav_item.click()
except Exception as e:
    error_count += 1
    print(f"Error encountered: {e}")

end_time = time.time()
response_time = end_time - start_time

driver.quit()

# Output Metrics
print(f"Number of Errors Encountered: {error_count}")
print(f"Response Time: {response_time} seconds")
