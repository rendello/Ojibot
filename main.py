#!/usr/bin/python3.6

import io
from selenium import webdriver

driver = webdriver.Firefox()
element = driver.get('https://ojibwe.lib.umn.edu/search?utf8=%E2%9C%93&q=anishinaabe&commit=Search&type=ojibwe')
element = driver.find_element_by_class_name("main-entry-search").screenshot_as_png 

with open("img.png", "wb") as png:
    png.write(element)

#from selenium.webdriver.common.keys import Keys
#
#driver = webdriver.Firefox()
#driver.get("http://www.python.org")
#assert "Python" in driver.title
#elem = driver.find_element_by_name("q")
#elem.clear()
#elem.send_keys("pycon")
#elem.send_keys(Keys.RETURN)
#assert "No results found." not in driver.page_source
#driver.close()
