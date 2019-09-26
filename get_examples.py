#!/usr/bin/python3.6

import bs4 as bs
import urllib.request


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


def fetch_example_section(url):
    source = urllib.request.urlopen(url).read()
    soup = bs.BeautifulSoup(source, 'lxml')

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




root = 'https://ojibwe.lib.umn.edu/'
examples = []

#letters = ['a','aa','b','ch','d','e','g','h',"'",'i', 'ii','j','k','m','n','o','oo','p','s','sh','t','w','y','z','zh']
letters = ['oo']

for letter in letters:
    for page in to_infinity():

        url = url_join(root, f'browse/ojibwe/{letter}?page={str(page)}')

        source = urllib.request.urlopen(url).read()
        soup = bs.BeautifulSoup(source, 'lxml')
 
        links = soup.select("a[href*=main-entry]")
        if links != []:

            for link in links:
                link = url_join('https://ojibwe.lib.umn.edu/', f'{link["href"]}')

                example_section = fetch_example_section(link)
                if example_section != None:
                    examples.extend(extract_examples(example_section))
                    print(examples)
        else:
            break

print('\n\n\n')
print(examples)
