from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pyperclip
import json
import os
import datetime
from time import sleep
import time
import random

chrome_options = Options()
# chrome_options.add_argument('--headless')  # This line enables headless mode
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()


while(True):
    try:
        data_file = os.path.join(os.getcwd(), 'data.json')
        with open(data_file, "r") as file:
            data_array = json.load(file)

        result_file = os.path.join(os.getcwd(), 'result.json')
        with open(result_file, "r") as file:
            result_array = json.load(file)

        # print(result_array)

        for url in data_array:
            driver.get(url)

            # if driver.find_element(By.CSS_SELECTOR, 'h1.text-align-center').text == '404 - Page Not Found':
            #     continue

            name = driver.find_element(By.CSS_SELECTOR, 'h1[data-localize="coll-display-name"]').text

            description = driver.find_element(By.CSS_SELECTOR, 'span[data-localize="coll-description"]').text

            driver.find_element(By.CSS_SELECTOR, 'svg.w-5.shrink-0').click()

            id = pyperclip.paste()

            del data_array[url]

            result_array[url] = {}
            result_array[url]['name'] = name
            result_array[url]['description'] = description
            result_array[url]['id'] = id

            with open(result_file, 'w') as file:
                json.dump(result_array, file, indent=4)
                
            with open(data_file, 'w') as file:
                json.dump(data_array, file, indent=4)


    except Exception as e:
        pass
