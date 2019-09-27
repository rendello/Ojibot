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
    return full_url


def get_soup(url):
    source = urllib.request.urlopen(url).read()
    return bs.BeautifulSoup(source, 'lxml')


def fetch_example_section(url):
    soup = get_soup(url)

    result = str(soup.find(id="sentenceExamples"))
    return result


def extract_examples(example_section):
    soup = bs.BeautifulSoup(example_section, 'lxml')
    examples = []

    for row in soup.find_all('tr'):
        example = {}
        example['oji'] = row.find('strong').text
        example['eng'] = row.find('small').text
        examples.append(example)

    return examples


def init_db():
    with dbopen('words.db') as c:
        c.execute('CREATE TABLE IF NOT EXISTS examples(eng TEXT UNIQUE, oji TEXT UNIQUE)')


def write_examples_to_db(examples):
    if examples == []:
        return

    with dbopen('words.db') as c:
        for example in examples:
            try:
                c.execute('INSERT INTO examples(eng, oji) VALUES (?,?)', (example['eng'], example['oji']))
            except IntegrityError:
                pass


def wait_a_bit():
    sleep(uniform(0, 10))


def print_in_place(text, flushzone=150):
    print(' ' * flushzone, end='\r', flush=True)
    print(text, end='\r', flush=True)


root = 'https://ojibwe.lib.umn.edu/'

letters = ['a','aa','b','ch','d','e','g','h',"'",'i', 'ii','j','k','m','n','o','oo','p','s','sh','t','w','y','z','zh']

init_db()

for letter in letters:
    
    section_examples = []
    for page in to_infinity():

        url = url_join(root, f'browse/ojibwe/{letter}?page={str(page)}')

        soup = get_soup(url)
 
        links = soup.select("a[href*=main-entry]")
        if links != []:

            for link in links:
                link = url_join('https://ojibwe.lib.umn.edu/', f'{link["href"]}')

                example_section = fetch_example_section(link)
                if example_section != None:
                    section_examples.extend(extract_examples(example_section))

                    print_in_place(link)

                    wait_a_bit()
        else:
            break

    write_examples_to_db(section_examples)
