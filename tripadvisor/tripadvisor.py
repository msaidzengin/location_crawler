from selenium import webdriver
import json

path = executable_path = r"/home/msaidzengin/chromedriver"
url = "https://www.tripadvisor.com.tr/Attractions-g298656-Activities-Ankara.html#ATTRACTION_SORT_WRAPPER"
result_name = "result_tripadvisor.json"

driver = webdriver.Chrome(path)
driver.get(url)

place_data = []
titles = driver.find_elements_by_class_name("listing_title")
for title in titles:
    place_data.append(title.text)

buttons = driver.find_elements_by_css_selector("a.pageNum.taLnk")
buttons[0].click()

for i in range(1, 8):
    titles = driver.find_elements_by_class_name("listing_title")
    for title in titles:
        place_data.append(title.text)

    buttons = driver.find_elements_by_css_selector("a.pageNum.taLnk")
    if i > 4:
        buttons[4].click()
    else:
        buttons[i].click()

titles = driver.find_elements_by_class_name("listing_title")
for title in titles:
    place_data.append(title.text)

driver.quit()

with open(result_name, 'w', encoding='utf-8') as f:
    json.dump(place_data, f, ensure_ascii=False, indent=4)
