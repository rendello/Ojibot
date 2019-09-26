#!/usr/bin/python3.6

from time import sleep as sleep_for_seconds
import urllib.request
import bs4 as bs
import sqlite3
from Core.db_context_manager import dbopen

def grab_gloss(soup):
    gloss = soup.select()


def grab_examples(soup):
    pass


def to_infinity(start=1):
    i = start
    while True:
        yield i
        i += 1


#letters = ['a','aa','b','ch','d','e','g','h',"'",'i', 'ii','j','k','m','n','o','oo','p','s','sh','t','w','y','z','zh']
letters = ['oo']

def get_examples(link):
    source = urllib.request.urlopen(link).read()
    soup = bs.BeautifulSoup(source, 'lxml')

    example_result = soup.find(id="sentenceExamples"), 'lxml'
    if example_result == None:
        return

    new_soup = bs.BeautifulSoup(str(example_result), 'lxml')


    examples = []
    for tag in new_soup.find_all('td'):
        if tag == None:
            continue

        string_parts = {}
        tag_soup = bs.BeautifulSoup(str(tag), 'lxml')

        if tag_soup == None:
            return

        try:
            string_parts['oji_example'] = tag_soup.find('strong').text
            string_parts['eng_example'] = tag_soup.find('small').text
        except:
            print('AHHHHHHHHHHHHHhh')

        examples.append(string_parts)

    if examples == []:
        return
    return examples



with dbopen('words.db') as c:
    c.execute('CREATE TABLE IF NOT EXISTS examples(eng TEXT, oji TEXT);')

for letter in letters:
    for page in to_infinity():
        url = f"https://ojibwe.lib.umn.edu/browse/ojibwe/{letter}?page={str(page)}"
        source = urllib.request.urlopen(url).read()
        soup = bs.BeautifulSoup(source, 'lxml')
 
        links = soup.select("a[href*=main-entry]")
        if links != []:
            for link in links:
                with open('latest_link', 'w') as f:
                    f.write(str(link))

                link = f"https://ojibwe.lib.umn.edu/{link['href']}"

                examples = get_examples(link)
                if examples == None:
                    continue

                with dbopen('words.db') as c:
                    for example in examples:
                        c.execute("INSERT INTO examples(oji, eng) VALUES(?,?)", [example['oji_example'], example['eng_example']])

        # Means we've run out of pages for that letter.
        else:
            break

