from selenium import webdriver
import json


def get_data(text):
    data = {}
    lines = text.split("\n")
    if len(lines) == 3:
        data['name'] = lines[0]
        data['tag'] = ""
        data['star'] = -1
        data['comment'] = int(lines[1].split(" ")[0].replace('.', ''))
    else:
        data['name'] = lines[0]
        data['tag'] = ""
        data['star'] = -1
        data['comment'] = -1

    return data


path = executable_path = r"/home/msaidzengin/chromedriver"
url = "https://www.tripadvisor.com.tr/Attractions-g298656-Activities-Ankara.html#ATTRACTION_SORT_WRAPPER"
result_name = "result_tripadvisor.json"

driver = webdriver.Chrome(path)
driver.get(url)

place_data = []
cards = driver.find_elements_by_class_name("attraction_element")
for card in cards:
    data = get_data(card.text)
    place_data.append(data)

buttons = driver.find_elements_by_css_selector("a.pageNum.taLnk")
buttons[0].click()

for i in range(1, 8):
    cards = driver.find_elements_by_class_name("attraction_element")
    for card in cards:
        data = get_data(card.text)
        place_data.append(data)

    buttons = driver.find_elements_by_css_selector("a.pageNum.taLnk")
    print(i)
    if i > 4:
        buttons[4].click()
    else:
        buttons[i].click()

cards = driver.find_elements_by_class_name("attraction_element")
for card in cards:
    data = get_data(card.text)
    place_data.append(data)

driver.quit()

with open(result_name, 'w', encoding='utf-8') as f:
    json.dump(place_data, f, ensure_ascii=False, indent=4)
