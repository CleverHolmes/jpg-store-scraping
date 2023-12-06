import json
import os
import requests
from bs4 import BeautifulSoup

result_file = os.path.join(os.getcwd(), 'result.json')

with open(result_file, "r", encoding='utf-8') as file:
    result_array = json.load(file)

for collection, details in result_array.items():
    if not details['image']:
        response = requests.get(details['link'])
        if response.status_code == 200:
            html_content = response.text

            # Use BeautifulSoup to parse the HTML content
            soup = BeautifulSoup(html_content, 'html.parser')

            # Assuming the image URL is in the "src" attribute of an "img" tag
            img_tag = soup.find('img', {'loading': 'eager', 'src': True})
            if img_tag:
                image_url = img_tag['src']
                details['image'] = image_url

with open(result_file, 'w', encoding='utf-8') as file:
    json.dump(result_array, file, ensure_ascii=False, indent=4)