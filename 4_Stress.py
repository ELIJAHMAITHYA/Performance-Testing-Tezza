from selenium import webdriver
from selenium.webdriver.common.by import By
import threading
import time
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

response_times = []
error_count = 0


def record_response_time(start_time):
    end_time = time.time()
    response_time = end_time - start_time
    response_times.append(response_time)
    logging.info(f"Response Time: {response_time:.2f} seconds")


def simulate_user(url):
    global error_count
    driver = webdriver.Firefox()
    try:
        start_time = time.time()
        driver.get(url)
        time.sleep(2)

        # Clicking on a main navigation item and then a sub-menu item
        nav_item = "Company"
        sub_item = "About"
        nav_link = driver.find_element(By.LINK_TEXT, nav_item)
        nav_link.click()
        time.sleep(2)

        submenu_link = driver.find_element(By.LINK_TEXT, sub_item)
        submenu_link.click()
        time.sleep(3)

        current_url = driver.current_url
        logging.info(f"PASS: Successfully navigated to '{sub_item}' under '{nav_item}' (URL: {current_url}).")

        record_response_time(start_time)
    except Exception as e:
        error_count += 1
        logging.error(f"ERROR: Exception encountered - {e}")
    finally:
        driver.quit()


def main(url, number_of_users):

 # Running  stress testing with a given number of concurrent users

    global response_times, error_count
    response_times = []
    error_count = 0
    start_time = time.time()

    threads = []
    for _ in range(number_of_users):
        thread = threading.Thread(target=simulate_user, args=(url,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()
    total_time = end_time - start_time

    # Calculate and print metrics
    average_response_time = sum(response_times) / len(response_times) if response_times else 0
    throughput = number_of_users / total_time
    error_rate = (error_count / number_of_users) * 100

    logging.info(f"Total Time for {number_of_users} users: {total_time:.2f} seconds")
    logging.info(f"Throughput: {throughput:.2f} requests per second")
    logging.info(f"Average Response Time: {average_response_time:.2f} seconds")
    logging.info(f"Error Rate: {error_rate:.2f}%")


if __name__ == "__main__":
    test_url = "https://tezzasolutions.com"

    number_of_users = 10

    main(test_url, number_of_users)
