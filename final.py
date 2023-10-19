import json
import os

result_file = os.path.join(os.getcwd(), 'result.json')

with open(result_file, 'r', encoding='utf-8') as file:
    result = json.load(file)

final_file = os.path.join(os.getcwd(), 'final.json')
with open(final_file, 'r', encoding='utf-8') as file:
    final_data = json.load(file)

for item in result:
    print(item)
    key = result[item]['name']
    final_data[key] = {}
    final_data[key]['link'] = item
    final_data[key]['description'] = result[item]['description']
    final_data[key]['id'] = result[item]['id']

with open(final_file, 'w', encoding='utf-8') as file:
    json.dump(final_data, file, ensure_ascii=False, indent=4)