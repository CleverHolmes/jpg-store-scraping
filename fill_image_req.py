import requests
from bs4 import BeautifulSoup
import json
import os

result_file = os.path.join(os.getcwd(), 'result.json')

with open(result_file, "r", encoding='utf-8') as file:
    result_array = json.load(file)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

for collection, details in result_array.items():
    if details['image'] == "":
        response = requests.get(details['link'], headers=headers)

        if response.status_code == 200:
            print("collection->",collection)
            soup = BeautifulSoup(response.text, 'html.parser')
            image = soup.find('div', class_='relative z-[1] hidden h-14 w-14 rounded-full bg-background-main lg:block lg:h-36 lg:w-36').find('img')

            if image.get('srcset'):
                details['image'] = image.get('srcset')

            if image.get('src'):
                details['image'] = image.get('src')

            with open(result_file, 'w', encoding='utf-8') as file:
                json.dump(result_array, file, ensure_ascii=False, indent=4)

        else:
            print(f"Failed to fetch {details['link']} - Status Code: {response.status_code}")

requests.Session().close()