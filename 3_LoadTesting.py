from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Metrics tracking
response_times = []
error_count = 0


def record_response_time(start_time):
    end_time = time.time()
    response_time = end_time - start_time
    response_times.append(response_time)
    logging.info(f"Response Time: {response_time:.2f} seconds")


def main():
    global error_count
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

    # Starting the test
    test_start_time = time.time()

    # Iterating over each nav item with sub-menu
    for nav_item, sub_items in nav_items_with_submenus.items():
        try:
            start_time = time.time()  # Start timing for the particular navigation item
            # Locating the main nav link
            nav_link = driver.find_element(By.LINK_TEXT, nav_item)
            nav_link.click()
            time.sleep(2)

            # Locate the sub-menu items
            dropdown_menu = driver.find_element(By.XPATH, f"//a[text()='{nav_item}']/following-sibling::ul")
            submenu_items = dropdown_menu.find_elements(By.TAG_NAME, "li")

            # Verify if the correct number of sub-menu items are present
            if len(submenu_items) == len(sub_items):
                logging.info(f"PASS: '{nav_item}' displays the correct number of sub-menu items.")
            else:
                logging.error(f"FAIL: '{nav_item}' does not display the correct number of sub-menu items.")

            # Click and test each sub-menu item
            for sub_item in sub_items:
                try:
                    if sub_item == "Testing as a Service - TaaS":
                        submenu_link = driver.find_element(By.XPATH, "//a[contains(text(), 'Testing as a Service')]")
                    else:
                        submenu_link = driver.find_element(By.LINK_TEXT, sub_item)

                    submenu_link.click()
                    time.sleep(3)

                    # Optionally, verifying the page URL or title to ensure navigation was successful
                    current_url = driver.current_url
                    logging.info(
                        f"PASS: Successfully navigated to '{sub_item}' under '{nav_item}' (URL: {current_url}).")

                    # Navigating back to the original page to test the next sub-menu item
                    driver.back()
                    time.sleep(2)

                    nav_link = driver.find_element(By.LINK_TEXT, nav_item)
                    nav_link.click()
                    time.sleep(2)

                    record_response_time(start_time)
                except Exception as e:
                    error_count += 1
                    logging.error(
                        f"ERROR: Could not navigate to sub-menu item '{sub_item}' under '{nav_item}'. Exception: {e}")
        except Exception as e:
            error_count += 1
            logging.error(f"ERROR: Could not test '{nav_item}'. Exception: {e}")

    # Ending the test
    test_end_time = time.time()
    total_time = test_end_time - test_start_time

    # Calculating and print metrics
    average_response_time = sum(response_times) / len(response_times) if response_times else 0
    throughput = len(response_times) / total_time
    error_rate = (error_count / (len(response_times) + error_count)) * 100

    logging.info(f"Total Time for test: {total_time:.2f} seconds")
    logging.info(f"Throughput: {throughput:.2f} requests per second")
    logging.info(f"Average Response Time: {average_response_time:.2f} seconds")
    logging.info(f"Error Rate: {error_rate:.2f}%")

    driver.quit()


if __name__ == "__main__":
    main()
