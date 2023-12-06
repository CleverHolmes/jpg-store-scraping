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

chrome_options = Options()
# chrome_options.add_argument('--headless')  # This line enables headless mode
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

result_file = os.path.join(os.getcwd(), 'result.json')

with open(result_file, "r", encoding='utf-8') as file:
    result_array = json.load(file)

for collection, details in result_array.items():
    if details['image'] == "":
        driver.get(details['link'])
        image_list = driver.find_elements(By.CSS_SELECTOR, 'img[loading="eager"]')
        for image in image_list:
            if 'https://res.cloudinary.com' in image.get_attribute('srcset'):
                details['image'] = image.get_attribute('srcset')

        with open(result_file, 'w', encoding='utf-8') as file:
            json.dump(result_array, file, ensure_ascii=False, indent=4)