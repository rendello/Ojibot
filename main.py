#!/usr/bin/python3.6

import io
from random import randint
from selenium import webdriver
import sqlite3


conn = sqlite3.connect('words.db')
c = conn.cursor()

def fetch_random_entry(db_file):
    c.execute("SELECT MAX(rowid) FROM words;")
    rand_id = randint(0, c.fetchone()[0])

    c.execute("SELECT title, url FROM words WHERE rowid=(?)", (rand_id, ))
    results = c.fetchone()
    title = results[0]
    url = results[1]
    return (title, url)


def get_screenshot(ojibwe_word):
    driver = webdriver.Firefox()
    element = driver.get(f'https://ojibwe.lib.umn.edu/main-entry/{word_url}')
    word_png_data = driver.find_element_by_class_name("main-entry-search").screenshot_as_png
    #roots_png_data = driver.find_element_by_id("wordParts").screenshot_as_png
    #driver.close()
    return png_data


def write_png_to_file(png_data, filename):
    with open("img.png", "wb") as png:
        png.write(png_data)


if __name__ == "__main__":
    print(fetch_random_entry('words.db'))
    #png_data = get_screenshot('adaawe')
    #write_png_to_file(png_data, 'img.png')

