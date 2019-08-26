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
    soup = bs.BeautifulSoup(source, 'html.parser')

    sections = {}

    sections['lemma'] = soup.find(class_='lemma')
    sections['gloss'] = soup.find(class_='glosses')
    sections['relations'] = soup.find(class_='relations')
    sections['word_parts'] = soup.find(id='wordParts').find(class_="panel-body")
    sections['sentence_examples'] = soup.find(id='sentenceExamples')
    
    return sections


def grab_links(soup):
    ''' Grabs all link text and urls from soup.
    
    Args:
        soup: a bs.BeautifulSoup() <object>.
    
    Returns:
        links: <list> of <dict>s, each containing a 'text' and 'url' pair.
    '''
    links = []
    for link in soup.find_all('a'):
        links.append({'text':link.text, 'url':link.get('href')})

    return links

def lemma(s):
    clean_text = bs.BeautifulSoup(str(s), 'html.parser').text
    formatted = f'__**{clean_text}**__'

    return formatted

def gloss(s):
    clean_text = bs.BeautifulSoup(str(s), 'html.parser').text
    formatted = f'{clean_text}'

    return formatted

def word_parts(s):
    soup = bs.BeautifulSoup(str(s), "html.parser")
    
    links = grab_links(soup)

    # changes the unsplit word <strong>word</strong> to a markdown
    # **word**. The html tags can be stripped since they'll all be stripped
    # later anyway
    original_word_html = soup.find('strong')
    original_word = original_word_html.text
    original_word_html.replace_with(f'**{original_word}**')

    # cleans / stylizes links. Unrelated to grab_links()
    [link.replace_with(f'__{link.text}__') for link in soup.find_all('a')]

    # removes badges
    [badge.replace_with('') for badge in soup.find_all(class_='badge')]

    formatted = soup.text

    formatted = formatted.replace('\n', ' ')

    # for some reason, bs changes <em>it</em> to <em>h/</em>. This will not do.
    formatted = formatted.replace('h/', '*it*')
        
    return formatted


def sentence_examples(s):
    soup = bs.BeautifulSoup(str(s), 'html.parser')

    # the audio portion of the table has a class, the actual wanted text has no
    # classes.
    [tag.replace_with('') for tag in soup.find_all('td') if tag.has_attr('class')]

    strongs = soup.find_all('strong')
    for strong in strongs:
        strong.replace_with(f'**{strong.text}**\n')

    smalls = soup.find_all('small')
    for small in smalls:
        small.replace_with(f'*{small.text}*\n\n')

    print(soup.text)

    return None






s = fetch_oji_word_info('gaandakii-iganaak-ni')

print(lemma(s['lemma']))
print(gloss(s['gloss']))
print(word_parts(s['word_parts']))
print(sentence_examples(s['sentence_examples']))
