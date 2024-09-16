from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import threading
import logging

logging.basicConfig(filename='spike_test.log', level=logging.INFO)

def simulate_user(user_id):
    try:
        start_time = time.time()
        driver = webdriver.Firefox()
        driver.get("https://tezzasolutions.com")
        driver.maximize_window()
        time.sleep(3)
        end_time = time.time()
        response_time = end_time - start_time
        logging.info(f"User {user_id}: Response Time: {response_time} seconds")
    except Exception as e:
        logging.error(f"User {user_id}: Error: {e}")
    finally:
        driver.quit()

# Simulating a sudden spike by launching multiple users at once
threads = []
for i in range(50):
    t = threading.Thread(target=simulate_user, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
