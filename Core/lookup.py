#!/usr/bin/python3.6

import bs4 as bs
import urllib.request

from Core.Tools.db_context_manager import dbopen


def get_word_urls(word):
    ''' Grabs every entry's OPD url-ending for a given word.

    Args:
        word: <str>, an Ojibwe word.

    Returns:
        <list> of unique <str>s, the urls for the given words.
    '''
    with dbopen('Core/words.db') as c:
        c.execute('SELECT url FROM words WHERE title=(?)', [word])
        results = c.fetchall()

        urls = []
        for result in results:
            url = result[0].replace('\n', '')
            if url not in urls:
                urls.append(url)

        return urls


def fetch_oji_word_info(word_url):
    ''' Fetches word information from the Ojibwe People's Dictionary.

    Args:
        word_url: <str>, The end section of the OPD's search url.

    Returns:
        A <dict> with all sections as keys, and their corresponding section
        html as values, or None if not found.
    '''
    source = urllib.request.urlopen(f"https://ojibwe.lib.umn.edu/main-entry/{word_url}").read()
    soup = bs.BeautifulSoup(source, 'html.parser')

    sections = {}

    sections['lemma'] = soup.find(class_='lemma')
    sections['gloss'] = soup.find(class_='glosses')
    sections['relations'] = soup.find(class_='relations')
    sections['inflections'] = soup.find(class_='inflectional-forms')
    try:
        sections['word_parts'] = soup.find(id='wordParts').find(class_="panel-body")
    except AttributeError:
        sections['word_parts'] = None
    sections['sentence_examples'] = soup.find(id='sentenceExamples')
    
    return sections
