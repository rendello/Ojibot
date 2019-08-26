#!/usr/bin/python3.6

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
    formatted = f'**{clean_text}**'

    return formatted

def gloss(s):
    clean_text = bs.BeautifulSoup(str(s), 'html.parser').text.strip()
    formatted = f'> {clean_text}'

    return formatted

def word_parts(s):
    soup = bs.BeautifulSoup(str(s), "html.parser")
    
    links = grab_links(soup)

    # changes the unsplit word <strong>word</strong> to a markdown
    # **word**. The html tags can be stripped since they'll all be stripped
    # later anyway
    original_word_html = soup.find('strong')
    original_word = original_word_html.text
    original_word_html.replace_with(f'**{original_word}**  <newline>')

    # cleans / stylizes links. Unrelated to grab_links()
    [link.replace_with(f'__{link.text}__') for link in soup.find_all('a')]

    # removes badges
    [badge.replace_with('') for badge in soup.find_all(class_='badge')]

    formatted = soup.text

    # destroy the random newlines, but keep that one newline that I want
    formatted = formatted.replace('\n', ' ')
    formatted = formatted.replace('<newline>', '\n')

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
        small.replace_with(f'> *{small.text}*\n')

    print(soup.text)

    return None






s = fetch_oji_word_info('gaandakii-iganaak-ni')

print(lemma(s['lemma']))
print(gloss(s['gloss']))
print(word_parts(s['word_parts']))
print(sentence_examples(s['sentence_examples']))
