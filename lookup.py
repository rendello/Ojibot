#!/usr/bin/python3.6

import bs4 as bs
import urllib.request


def fetch_oji_word_info(word_url):
    ''' Fetches word information from the Ojibwe People's Dictionary.

    Args:
        word_url: <str>, The end section of the OPD's search url.

    Returns:
        A <dict> with all sections as keys, and their corresponding section
        html as values, or None if not found.
    '''
    source = urllib.request.urlopen(f"https://ojibwe.lib.umn.edu/main-entry/{word_url}").read()
    soup = bs.BeautifulSoup(source, 'html5lib')

    sections = {}

    sections['lemma'] = soup.find(class_='lemma')
    sections['gloss'] = soup.find(class_='glosses')
    sections['word_parts'] = soup.find(id='wordParts').find(class_="panel-body")
    
    return sections

s = fetch_oji_word_info('anishinaabemowin-ni')

for k, v in s.items():
    print(f'{k}\n---\n{v}\n\n\n')

    
