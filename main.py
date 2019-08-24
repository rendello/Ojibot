#!/usr/bin/python3.6

import io
from random import randint
from selenium import webdriver
import sqlite3

from db_context_manager import dbopen


def fetch_random_entry(db_file):
    with dbopen('words.db') as c:
        c.execute("SELECT MAX(rowid) FROM words;")
        max_id = c.fetchone()[0]
        rand_id = randint(0, max_id)

        c.execute("SELECT title, url FROM words WHERE rowid=(?)", [rand_id])
        results = c.fetchone()
        title = results[0]
        url = results[1]

        return (title, url)


def get_screenshot(word_url):
    with webdriver.Firefox() as wd:
        element = wd.get(f'https://ojibwe.lib.umn.edu/main-entry/{word_url}')
        #word_png_data = wd.find_element_by_class_name("main-entry-search").screenshot_as_png
        roots_png_data = wd.find_element_by_id("wordParts").screenshot_as_png
        return roots_png_data


def write_png_to_file(png_data, filename):
    with open("img.png", "wb") as png:
        png.write(png_data)


if __name__ == "__main__":
    title, url = fetch_random_entry('words.db')
    png_data = get_screenshot(url)
    write_png_to_file(png_data, 'img.png')

