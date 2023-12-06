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

proxy_server = "http://49fcb87045f3a57acb4b6f0983876ce4caea018d:autoparse=true@proxy.zenrows.com"
proxy_port = 8001

chrome_options = Options()
chrome_options.add_argument(f'--proxy-server=https://{proxy_server}:{proxy_port}')

# chrome_options.add_argument('--headless')  # This line enables headless mode
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

Flag = True

while(Flag):
    try:
        data_file = os.path.join(os.getcwd(), 'data.json')
        result_file = os.path.join(os.getcwd(), 'result.json')

        with open(data_file, "r", encoding='utf-8') as file:
            data_array = json.load(file)

        with open(result_file, "r", encoding='utf-8') as file:
            result_array = json.load(file)

        for url, _ in list(data_array.items()):
            driver.get(url)

            name = driver.find_element(By.CSS_SELECTOR, 'h1[data-localize="coll-display-name"]').text
            description = driver.find_element(By.CSS_SELECTOR, 'span[data-localize="coll-description"]').text

            driver.find_element(By.CSS_SELECTOR, 'svg.w-5.shrink-0').click()
            id = pyperclip.paste()
            pyperclip.copy('')

            image = driver.find_element(By.CSS_SELECTOR, 'img[loading="eager"]').get_attribute('srcset')

            socials = [item.get_attribute('href') for item in driver.find_elements(By.XPATH, "//span[@class='group/item inline-flex']/a")]

            prices = [item.text for item in driver.find_elements(By.CSS_SELECTOR, 'span[data-notranslate="true"]')[2:8]]

            del data_array[url]

            result_array[name] = {
                'link': url,
                'description': description,
                'id': id,
                'image': image,
                'socials': socials,
                'prices': prices
            }

            # Write the results to files after the loop
            with open(result_file, 'w', encoding='utf-8') as file:
                json.dump(result_array, file,ensure_ascii=False,  indent=4)

            with open(data_file, 'w', encoding='utf-8') as file:
                json.dump(data_array, file,ensure_ascii=False,  indent=4)
                
    except KeyboardInterrupt as e:
        print(e)
        Flag = False

    except Exception as e:
        print(url)
        print(e)
        pass
