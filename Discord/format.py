#!/usr/bin/python3.6

import bs4 as bs

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


def fmt_lemma(s):
    clean_text = bs.BeautifulSoup(str(s), 'html.parser').text
    formatted = f'« **{clean_text}** »'

    return formatted


def fmt_gloss(s):
    clean_text = bs.BeautifulSoup(str(s), 'html.parser').text.strip()
    formatted = f'> {clean_text}'

    return formatted


def fmt_inflections(s):
    clean_text = bs.BeautifulSoup(str(s), 'html.parser').text
    clean_text = clean_text.strip()
    clean_text = clean_text.replace('; ','\n')
    formatted = f'`{clean_text}`'

    return formatted


def fmt_word_parts(s):
    soup = bs.BeautifulSoup(str(s), "html.parser")
    
    links = grab_links(soup)

    soup.find('strong').replace_with('')

    # cleans / stylizes links. Unrelated to grab_links()
    [link.replace_with(f'__{link.text}__') for link in soup.find_all('a')]

    # removes badges
    [badge.replace_with('') for badge in soup.find_all(class_='badge')]

    formatted = soup.text

    # destroy the random newlines, but keep that one newline that I want
    formatted = formatted.replace('\n', ' ')

    return formatted


def fmt_sentence_examples(s):
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

    formatted = soup.text
    return formatted


def fmt_relations(s):
    soup = bs.BeautifulSoup(str(s), 'html.parser')
    [tag.replace_with('') for tag in soup.find_all('span') if 'badge' in tag.get('class')]

    clean_text = soup.text.strip()
    if clean_text != '':
        formatted = f'*{clean_text}*'.replace('\n', '')
    else:
        return None

    return formatted


def fmt_all(sections):
    ''' Formats all sections given.

    Args:
        sections: <dict> with all available word info sections

    Returns:
        formatted_sections: <dict> with fromatted sections as values
    '''
    formatters = {
        'lemma': fmt_lemma,
        'gloss': fmt_gloss,
        'inflections': fmt_inflections,
        'word_parts': fmt_word_parts,
        'sentence_examples': fmt_sentence_examples,
        'relations': fmt_relations
    }
    formatted_sections = {}

    for s, v in sections.items():
        if v is not None:
            formatted_sections[s] = formatters[s](v)
        else:
            formatted_sections[s] = None

    return formatted_sections


def fmt_dict_to_text(formatted):
    ''' Combines formatted strings in a single string.

    Args:
        formatted: a <dict> of formatted sections and NoneTypes.

    Returns:
        fmt_string: a <string> with all available sections rendered in a
        logical order.
    '''
    print(formatted)
    string_order = ['lemma', 'relations', 'gloss', '\n', 'inflections', '\n', 'word_parts', '\n', 'sentence_examples']
    fmt_string = ''

    for string in string_order:
        if string == '\n':
            fmt_string += '\n'
        elif formatted[string] is not None:
            fmt_string += f'\n{formatted[string]}'

    return fmt_string
