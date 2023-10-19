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

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.jpg.store/marketplace?view=allCollections")

data_array = {}

base_url = "/collection/"

data_file = os.path.join(os.getcwd(), 'data.json')
sleep(5)

cnt = 0

while(True):
    if cnt == 20:
        cnt = 0
        element_list = driver.find_elements(By.CSS_SELECTOR,f'a[href*="{base_url}"]')

        with open(data_file, "r") as file:
            data_array = json.load(file)

        for item in element_list:
            url = item.get_attribute('href')

            if url == "https://www.jpg.store/collection/statistics":
                continue

            if url in data_array:
                continue

            data_array[url] = {}
            print(url)

        with open(data_file, 'w') as file:
            json.dump(data_array, file, indent=4)
    
    cnt = cnt + 1

    driver.execute_script(f"window.scrollBy(0, 200000);")

    sleep(5)
