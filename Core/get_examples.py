#!/usr/bin/python3.6

import bs4 as bs
import urllib.request

from random import uniform
from time import sleep

from db_context_manager import dbopen
from sqlite3 import IntegrityError


def to_infinity(start=1):
    i = start
    while True:
        yield i
        i += 1


def url_join(*urls):
    ''' Gets rid of double slashes in url joins. '''
    full_url = ''
    for url in urls:
        url = url.strip('/')
        url += '/'
        full_url += url
    full_url = full_url.replace('\n', '')
    return full_url


def get_soup(url):
    source = urllib.request.urlopen(url).read()
    return bs.BeautifulSoup(source, 'lxml')


def fetch_example_section(url):
    soup = get_soup(url)

    result = soup.find(id="sentenceExamples")
    if result is not None:
        result = str(result)
    return result


def extract_examples(example_section, url):
    soup = bs.BeautifulSoup(example_section, 'lxml')

    for row in soup.find_all('tr'):
        example = {}
        example['oji'] = row.find('strong').text
        example['eng'] = row.find('small').text
        example['url'] = url

    return example


def init_db():
    with dbopen('words.db') as c:
        c.execute('CREATE TABLE IF NOT EXISTS examples(eng TEXT, oji TEXT, url TEXT)')


def write_example_to_db(example, cursor):
        try:
            cursor.execute('INSERT INTO examples(eng, oji, url) VALUES (?,?,?)', (example['eng'], example['oji'], example['url']))

        # If columns aren't unique
        except IntegrityError as e:
            print(e)
            pass


def wait_a_bit():
    sleep(uniform(1, 3))


def print_in_place(text, flushzone=150):
    print(' ' * flushzone, end='\r', flush=True)
    print(text, end='\r', flush=True)



link_root = 'https://ojibwe.lib.umn.edu/main-entry'

init_db()

with dbopen('words.db') as c:
    c.execute('SELECT url FROM words;')
    for result in c.fetchall():
        link_end = result[0]
        link = url_join(link_root, link_end)

        # No need trying to scrape / record everything twice.
        c.execute(f'SELECT * FROM examples WHERE url = ?;', [link])
        if c.fetchone():
            continue

        example_section = fetch_example_section(link)

        # We still want the url to know if this entry has been recorded or not
        if example_section is None:
            example = {'eng': None, 'oji': None, 'url': link}
        else:
            example = extract_examples(example_section, url=link)

            wait_a_bit()
        #print_in_place(link)
        print(example)
        write_example_to_db(example, c)
