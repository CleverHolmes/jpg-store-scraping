from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import json
import os
import datetime
from time import sleep
import time
import random
import json


option = Options()
# option.add_argument('--headless')
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.jpg.store/marketplace?view=allCollections")

data_array = {}

base_url = "/collection/"

data_file = os.path.join(os.getcwd(), 'data.json')
origin_file = os.path.join(os.getcwd(), 'origin.json')
sleep(5)

begin = 0
count = 0
while(True):
    sleep(5)
    if count == 25: 
        element_list = driver.find_elements(By.CSS_SELECTOR, f'a[href*="{base_url}"]')

        with open(data_file, "r") as file:
            data_array = json.load(file)
        with open(origin_file, "r") as file:
            origin_array = json.load(file)

        # Filter out unwanted URLs and create dictionaries
        url = [
            (item.get_attribute('href'), {})
            for item in element_list[begin::2]
            if item.get_attribute('href') != "https://www.jpg.store/collection/statistics"
            and item.get_attribute('href') not in data_array
        ]

        # Update data and origin arrays
        data_array.update(dict(url))
        origin_array.update(dict(url))

        # Print results
        print(begin, len(url))
        begin += len(url)

        with open(data_file, 'w') as file:
            json.dump(data_array, file, indent=4)
        with open(origin_file, 'w') as file:
            json.dump(origin_array, file, indent=4)
        count = 0
    count = count + 1
    driver.execute_script(f"window.scrollBy(0, 200000);")


