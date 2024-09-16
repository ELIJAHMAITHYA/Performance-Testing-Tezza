from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# initiaalize firefox browser
driver = webdriver.Firefox()
driver.get("https://tezzasolutions.com/software-testing/")
driver.maximize_window()
time.sleep(3)

# wait for the browser page to load fully
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
actions = ActionChains(driver)

# Clink on each link in the nav respectively
nav_items = ["Home", "Company", "Expertise", "Services", "Resources", "Contact"]

for item in nav_items:
    try:
        nav_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, item))
        )

        actions.move_to_element(nav_link).perform()
        time.sleep(2)

        if item in ["Company", "Expertise", "Services", "Resources"]:

            dropdown_menu = nav_link.find_element(By.XPATH, "../ul")
            submenu_items = dropdown_menu.find_elements(By.TAG_NAME, "li")

            if submenu_items:
                print(f"PASS: '{item}' displays a drop-down with {len(submenu_items)}items.")
            else:
                print(f"FAIL: '{item}' does not display a drop-down menu.")
        else:
            if nav_link.is_displayed() and nav_link.is_enabled():
                print(f"PASS: '{item}' is a direct link and is clickable.")
            else:
                print(f"FAIL: '{item}' is not clickable.")
    except Exception as e:
        print(f"ERROR: Could not test '{item}'.Exception: {e}")

driver.quit()
