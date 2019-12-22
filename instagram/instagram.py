from pandas.io.json import json_normalize
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
from selenium import webdriver
from datetime import datetime
import pandas as pd
import numpy as np
import requests
import zipfile
import time
import json
import re
import os


def load_all_page(driver):

    time.sleep(3)
    SCROLL_PAUSE_TIME = 2
    images_data = []
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            driver.execute_script(
                "window.scrollTo(document.body.scrollHeight,0);")
            break
        last_height = new_height
        time.sleep(1)
        html_to_parse = str(driver.page_source)
        html = bs(html_to_parse, "html5lib")
        images_url = html.findAll("div", {"class": "v1Nh3 kIKUG  _bz0w"})
        images_data += images_url

    images_data = set(images_data)

    return images_data


def process_data(images_data):
    urls = []

    for image in images_data:
        link = 'https://www.instagram.com' + image.find('a', href=True)['href']
        urls.append(link)

    return urls


def main():
    path = r"/home/msaidzengin/chromedriver"
    instagram_url = 'beklentisel'
    url = 'https://www.instagram.com/' + instagram_url

    driver = webdriver.Chrome(path)
    driver.get(url)
    images_data = load_all_page(driver)
    driver.quit()

    photo_urls = process_data(images_data)


if __name__ == "__main__":
    main()
