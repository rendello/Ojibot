#!/usr/bin/python3.6

import io
from urllib.parse import quote_plus
from selenium import webdriver

def get_screenshot(ojibwe_word):
    encoded_word = quote_plus(ojibwe_word)

    driver = webdriver.Firefox()
    element = driver.get(f'https://ojibwe.lib.umn.edu/search?utf8=%E2%9C%93&q={encoded_word}&commit=Search&type=ojibwe')
    png_data = driver.find_element_by_class_name("main-entry-search").screenshot_as_png 
    #driver.close()
    return png_data

def write_png_to_file(png_data, filename):
    with open("img.png", "wb") as png:
        png.write(png_data)


if __name__ == "__main__":
    png_data = get_screenshot('mooz')
    write_png_to_file(png_data, 'img.png')

