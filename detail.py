# import requests
# from bs4 import BeautifulSoup
# import pyperclip
# import json
# import os
# import datetime
# import time
# import random

# Flag = True

# while Flag:
#     try:
#         data_file = os.path.join(os.getcwd(), 'data.json')
#         result_file = os.path.join(os.getcwd(), 'result.json')

#         with open(data_file, "r", encoding='utf-8') as file:
#             data_array = json.load(file)

#         with open(result_file, "r", encoding='utf-8') as file:
#             result_array = json.load(file)

#         for url, _ in list(data_array.items()):
#             response = requests.get(url)

#             soup = BeautifulSoup(response.content, 'html.parser')

#             name = soup.select_one('h1[data-localize="coll-display-name"]').text
#             print('3->',name)

#             description = soup.select_one('span[data-localize="coll-description"]').text
#             print('4->',description)

#             image = soup.select_one('img[loading="eager"]').get('srcset')
#             print('4.5->',image)

#             socials = [item.get('href') for item in soup.select('span.group\/item.inline-flex a')]
#             print('6->',socials)

#             prices = [item for item in soup.select('span[data-notranslate="true"]')]
#             # prices = [item.text for item in soup.select('span[data-notranslate="true"]')[2:8]]
#             print('7->',prices)

#             # del data_array[url]

#             print('8')
#             result_array[name] = {
#                 'link': url,
#                 'description': description,
#                 'image': image,
#                 'socials': socials,
#                 'prices': prices
#             }

#             print('result->',result_array[name])

#             # Write the results to files after the loop
#             # with open(result_file, 'w', encoding='utf-8') as file:
#             #     json.dump(result_array, file, ensure_ascii=False, indent=4)

#             # with open(data_file, 'w', encoding='utf-8') as file:
#             #     json.dump(data_array, file, ensure_ascii=False, indent=4)
#             break

#         Flag = False

#     except KeyboardInterrupt as e:
#         print(e)
#         Flag = False

#     except Exception as e:
#         Flag = False
#         print(url)
#         print(e)
#         pass



import requests
from bs4 import BeautifulSoup
import json
import os
from time import sleep

result_file = os.path.join(os.getcwd(), 'result.json')

with open(result_file, "r", encoding='utf-8') as file:
    result_array = json.load(file)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

svg = 'M11.513 1.94254C11.2246 0.237905 8.77552 0.237904 8.48715 1.94254C8.2805 3.16417 6.78595 3.64978 5.9007 2.78292C4.66545 1.57334 2.6841 3.01289 3.45276 4.56146C4.00363 5.67125 3.07995 6.94258 1.85425 6.76162C0.143939 6.50911 -0.612873 8.83834 0.919219 9.63935C2.0172 10.2134 2.0172 11.7849 0.919218 12.3589C-0.612874 13.1599 0.143939 15.4891 1.85425 15.2366C3.07995 15.0557 4.00363 16.327 3.45276 17.4368C2.6841 18.9854 4.66546 20.4249 5.9007 19.2153C6.78595 18.3485 8.2805 18.8341 8.48715 20.0557C8.77552 21.7603 11.2246 21.7603 11.513 20.0557C11.7196 18.8341 13.2142 18.3485 14.0994 19.2153C15.3347 20.4249 17.316 18.9854 16.5474 17.4368C15.9965 16.327 16.9202 15.0557 18.1459 15.2366C19.8562 15.4891 20.613 13.1599 19.0809 12.3589C17.9829 11.7849 17.9829 10.2134 19.0809 9.63935C20.613 8.83834 19.8562 6.50911 18.1459 6.76162C16.9202 6.94258 15.9965 5.67125 16.5474 4.56146C17.316 3.01289 15.3347 1.57334 14.0994 2.78292C13.2142 3.64978 11.7196 3.16417 11.513 1.94254ZM8.29287 13.6601C8.22746 13.5947 8.173 13.5225 8.1295 13.4457L6.70708 12.0233C6.31656 11.6328 6.31656 10.9996 6.70708 10.6091C7.09761 10.2186 7.73077 10.2186 8.1213 10.6091L9.02548 11.5133L12.2462 8.29262C12.6367 7.9021 13.2698 7.9021 13.6604 8.29262C14.0509 8.68315 14.0509 9.31631 13.6604 9.70684L9.70708 13.6601C9.31656 14.0506 8.6834 14.0506 8.29287 13.6601Z'

lists=[]

for collection, details in result_array.items():
    if details['link'] in lists:
        flag = True
        while flag:
            response = requests.get(details['link'], headers=headers)

            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')

                image = soup.find('div', class_='relative z-[1] hidden h-14 w-14 rounded-full bg-background-main lg:block lg:h-36 lg:w-36').find('img')
                if image.get('srcset'):
                    details['image'] = image.get('srcset')
                if image.get('src'):
                    details['image'] = image.get('src')

                banner = soup.find('div', class_='relative flex flex-col items-center h-40 md:h-44 lg:h-64 bg-background-popout overflow-hidden').find('img')
                if banner.get('srcset'):
                    details['banner'] = banner.get('srcset')
                if banner.get('src'):
                    details['banner'] = banner.get('src')

                category = [item.text for item in soup.find_all('span', class_='m-0 font-lexend text-xs sm:text-sm font-normal text-text-subdued')]
                details['category'] = category

                verify = soup.find('path',{'d':svg})
                if verify:
                    details['verify'] = True
                else:
                    details['verify'] = False

                with open(result_file, 'w', encoding='utf-8') as file:
                    json.dump(result_array, file, ensure_ascii=False, indent=4)

                    flag = False

            else:
                print(f"Failed to fetch {details['link']} - Status Code: {response.status_code}")
                
            sleep(1)

requests.Session().close()