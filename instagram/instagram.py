from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
from selenium import webdriver
import pandas as pd
import requests
import time
import json


def load_all_page(driver):

    time.sleep(3)
    SCROLL_PAUSE_TIME = 1
    images_data = []
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            driver.execute_script("window.scrollTo(document.body.scrollHeight,0);")
            break
        last_height = new_height
        time.sleep(1)
        html_to_parse = str(driver.page_source)
        html = bs(html_to_parse, "html5lib")
        images_url = html.findAll("div", {"class": "v1Nh3 kIKUG  _bz0w"})
        images_data += images_url

    images_data = set(images_data)

    urls = []

    for image in images_data:
        link = 'https://www.instagram.com' + image.find('a', href=True)['href']
        urls.append(link)

    return urls


def main():
    path = r"/home/msaidzengin/chromedriver"
    instagram_url = 'msaidzengin'
    url = 'https://www.instagram.com/' + instagram_url

    driver = webdriver.Chrome(path)
    driver.get(url)
    photo_urls = load_all_page(driver)

    locations = []

    for photo in photo_urls:
        driver.get(photo)
        html_to_parse = str(driver.page_source)
        html = bs(html_to_parse, "html5lib")
        loc = html.find("a", {"class": "O4GlU"})
        try:
            name = loc.getText()
            url = 'https://www.instagram.com/' + loc['href']
            locations.append({
                'name': name,
                'url': url
            })
        except:
            pass

        time.sleep(1)

    with open('loc.json', 'w', encoding='utf-8') as f:
        json.dump(locations, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    main()
