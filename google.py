from  selenium import webdriver
import json

def get_data(text):
    data = {}
    lines = text.split("\n")
    if len(lines) == 2:
        data['name'] = lines[0]
        data['tag'] = lines[1]
        data['star'] = -1
        data['comment'] = -1
    else:
        data['name'] = lines[0]
        data['tag'] = lines[-1]
        data['star'] = float(lines[1].replace(',','.'))
        data['comment'] = int(lines[-2][1:-1].replace('.',''))
    
    return data
    
path = executable_path=r"/home/msaidzengin/chromedriver"
url = "https://www.google.com/travel/things-to-do/see-all?g2lb=2502405%2C2502548%2C4208993%2C4254308%2C4258168%2C4260007%2C4270442%2C4274032%2C4285990%2C4289525%2C4291318%2C4301054%2C4305595%2C4308216%2C4313006%2C4315873%2C4317816%2C4317915%2C4324289%2C4326405%2C4326765%2C4328159%2C4329288%2C4329496%2C4333189%2C4270859%2C4284970%2C4291517%2C4292955%2C4316256%2C4333108&hl=tr&gl=tr&un=1&otf=1&dest_mid=%2Fm%2F0jyw&dest_src=ts&dest_state_type=sattd&sa=X#ttdm=39.912628_32.853774_11&ttdmf=%25252Fm%25252F0gjb198"
result_name = "result_google.json"

driver = webdriver.Chrome(path)
driver.get(url)

place_data = []
cards = driver.find_elements_by_class_name("f4hh3d")

for card in cards:
    data = get_data(card.text)
    place_data.append(data)

driver.quit()

with open(result_name, 'w', encoding='utf-8') as f:
    json.dump(place_data, f, ensure_ascii=False, indent=4)
