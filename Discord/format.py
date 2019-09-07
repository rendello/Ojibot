#!/usr/bin/python3.6

import bs4 as bs

def strip_newlines_and_whitespace(string):
    return string.replace('\n', '').strip()


def fmt_lemma(s):
    soup = bs.BeautifulSoup(str(s), 'html.parser')
    text = strip_newlines_and_whitespace(soup.text)
    string_parts = [{'sect':'lemma', 'text':text, 'url':None}]

    return string_parts


def fmt_gloss(s):
    soup = bs.BeautifulSoup(str(s), 'html.parser')
    text = strip_newlines_and_whitespace(soup.text)
    string_parts = [{'sect':'gloss', 'text':text, 'url':None}]

    return string_parts


def fmt_inflections(s):
    soup = bs.BeautifulSoup(str(s), "html.parser")
    string_parts = []
    
    for child in soup.p.children:
        if child.name == 'strong':
            string_parts.append({'sect':'inflection', 'text':child.text, 'url':None})
        elif child.name == 'em':
            string_parts.append({'sect':'TMA', 'text':child.text, 'url':None})
        else:
            string_parts.append({'sect':'text', 'text':child, 'url':None})

    return string_parts


def fmt_word_parts(s):
    soup = bs.BeautifulSoup(str(s), "html.parser")
    string_parts = []
    
    for child in soup.div.children:
        if child.name == 'strong':
            string_parts.append({'sect':'orig_word', 'text':child.text, 'url':None})
        elif child.name == 'a':
            string_parts.append({'sect':'link', 'text':child.text, 'url':child['href']})
        else:
            string_parts.append({'sect':'text', 'text':child, 'url':None})

    return string_parts


def fmt_sentence_examples(s):
    soup = bs.BeautifulSoup(str(s), 'html.parser')
    string_parts = []

    for tag in soup.find_all():
        if tag.name == 'strong':
            string_parts.append({'sect':'oji_example', 'text':tag.text, 'url':None})
        elif tag.name == 'small':
            string_parts.append({'sect':'eng_example', 'text':tag.text, 'url':None})

    return string_parts


def fmt_relations(s):
    soup = bs.BeautifulSoup(str(s), 'html.parser')
    string_parts = []

    string_parts.append({'sect':'paired_preamble', 'text':'Paired with:', 'url':None})

    relations_link = soup.find('a')
    string_parts.append({'sect':'paired_word', 'text': relations_link.text, 'url':relations_link['href']})

    return string_parts


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
    #print(formatted)
    string_order = ['lemma', 'relations', 'gloss', '\n', 'inflections', '\n', 'word_parts', '\n', 'sentence_examples']
    fmt_string = ''

    for string in string_order:
        if string == '\n':
            fmt_string += '\n'
        elif formatted[string] is not None:
            fmt_string += f'\n{formatted[string]}'

    return fmt_string
