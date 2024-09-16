from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get("https://tezzasolutions.com")
driver.maximize_window()
time.sleep(3)


# Define the main nav items and their respective sub-menu links
nav_items_with_submenus = {
    "Company": ["About", "History", "Methodology", "Engagement Model", "Clients & Partners"],
    "Expertise": ["Strategy and Consulting", "Software Testing", "Technology and Engineering", "Quality Assurance"],
    "Services": ["Testing as a Service - TaaS", "Cybersecurity", "AI Automation Tools", "Staff Augmentation",
                 "Trainings", "Digital Agency", "Tezza Multi-media Hub"],
    "Resources": ["Blog", "Events", "Case Studies", "Press Release"]
}


# Iterate over each nav item with sub-menu
for nav_item, sub_items in nav_items_with_submenus.items():
    try:
        # Locate the main nav link
        nav_link = driver.find_element(By.LINK_TEXT, nav_item)
        nav_link.click()
        time.sleep(2)


        # Locate the sub-menu items
        dropdown_menu = nav_link.find_element(By.XPATH, "../ul")
        submenu_items = dropdown_menu.find_elements(By.TAG_NAME, "li")


        # Verify if the correct number of sub-menu items are present
        if len(submenu_items) == len(sub_items):
            print(f"PASS: '{nav_item}' displays the correct number of sub-menu items.")
        else:
            print(f"FAIL: '{nav_item}' does not display the correct number of sub-menu items.")


        # Click and test each sub-menu item
        for sub_item in sub_items:
            try:
                #Use Partial link text for "Testing as a Service - TaaS"
                if sub_item == "Testing as a Service - TaaS":
                    submenu_link = driver.find_element (By.XPATH,"//a[contains((text), 'Testing as a Service')]")

                else:
                    submenu_link = driver.find_element(By.LINK_TEXT, sub_item)

                submenu_link.click()
                time.sleep(3)

                # Optionally, verify the page URL or title to ensure navigation was successful
                current_url = driver.current_url
                print(f"PASS: Successfully navigated to '{sub_item}' under '{nav_item}' (URL: {current_url}).")

                # Navigate back to the original page to test the next sub-menu item
                driver.back()
                time.sleep(2)

                # Re-open the drop-down for the next sub-menu item
                nav_link = driver.find_element(By.LINK_TEXT, nav_item)
                nav_link.click()
                time.sleep(2)

            except Exception as e:
                print(f"ERROR: Could not navigate to sub-menu item '{sub_item}' under '{nav_item}'. Exception: {e}")
    except Exception as e:
        print(f"ERROR: Could not test '{nav_item}'. Exception: {e}")

# Close the browser
driver.quit()