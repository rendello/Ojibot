#!/usr/bin/python3.6

import bs4 as bs

def strip_newlines_and_whitespace(string):
    return string.replace('\n', '').strip()


def serialize_lemma(s):
    soup = bs.BeautifulSoup(str(s), 'html.parser')
    text = strip_newlines_and_whitespace(soup.text)
    string_parts = [{'sect':'lemma', 'text':text, 'url':None}]

    return string_parts


def serialize_gloss(s):
    soup = bs.BeautifulSoup(str(s), 'html.parser')
    text = strip_newlines_and_whitespace(soup.text)
    string_parts = [{'sect':'gloss', 'text':text, 'url':None}]

    return string_parts


def serialize_inflections(s):
    soup = bs.BeautifulSoup(str(s), "html.parser")
    string_parts = []
    
    for child in soup.p.children:
        if child.name == 'strong':
            string_parts.append({'sect':'inflection', 'text':child.text, 'url':None})
        elif child.name == 'em':
            string_parts.append({'sect':'TMA', 'text':child.text, 'url':None})
        elif child.name == None:
            string_parts.append({'sect':'text', 'text':child.replace(';',''), 'url':None})

    return string_parts


def serialize_word_parts(s):
    soup = bs.BeautifulSoup(str(s), "html.parser")
    string_parts = []
    
    for child in soup.div.children:
        if child.name == 'strong':
            string_parts.append({'sect':'orig_word', 'text':child.text, 'url':None})
        elif child.name == 'a':
            string_parts.append({'sect':'link', 'text':child.text, 'url':child['href']})
        elif child.name == None:
            string_parts.append({'sect':'text', 'text':child, 'url':None})

    return string_parts


def serialize_sentence_examples(s):
    soup = bs.BeautifulSoup(str(s), 'html.parser')
    string_parts = []

    for tag in soup.find_all():
        if tag.name == 'strong':
            string_parts.append({'sect':'oji_example', 'text':tag.text, 'url':None})
        elif tag.name == 'small':
            string_parts.append({'sect':'eng_example', 'text':tag.text, 'url':None})

    return string_parts


def serialize_relations(s):
    soup = bs.BeautifulSoup(str(s), 'html.parser')
    string_parts = []

    string_parts.append({'sect':'paired_preamble', 'text':'Paired with:', 'url':None})

    relations_link = soup.find('a')
    string_parts.append({'sect':'paired_word', 'text': relations_link.text, 'url':relations_link['href']})

    return string_parts


def serialize_all(sections):
    serializers = {
        'lemma': serialize_lemma,
        'gloss': serialize_gloss,
        'inflections': serialize_inflections,
        'word_parts': serialize_word_parts,
        'sentence_examples': serialize_sentence_examples,
        'relations': serialize_relations
    }
    serialized_sections = []

    for section, v in sections.items():
        if v is not None:
            for section in serializers[section](v):
                serialized_sections.append(section)

    return serialized_sections


def int_to_superscript(integer):
    number_superscripts = {
        '1': '¹',
        '2': '²',
        '3': '³',
        '4': '⁴',
        '5': '⁵',
        '6': '⁶',
        '7': '⁷',
        '8': '⁸',
        '9': '⁹',
    }
    superscripted_number = ''
    string_number = str(integer)
    for char in string_number:
        superscripted_number += number_superscripts[char]

    return superscripted_number


def format_for_discord(serialized_sections):
    sect_formatting = {
        'lemma': ('**«','»**\n'),
        'gloss': ('*', '*\n'),
        'inflection': ('', ': '),
        'TMA': ('*', '*\n'),
        'oji_example': ('**', '**\n'),
        'eng_example': ('>*', '*\n'),
        'paired_preamble': ('',''),
        'paired_word': ('',''),
        'orig_word': ('',''),
        'link': ('',''),
        'text': ('','')
    }

    string = ''
    url_no = 1
    links = []

    for s in serialized_sections:
        fmt = sect_formatting[s['sect']]

        text = s['text']
        url = s['url']
        if url != None:
            superscript_no = int_to_superscript(url_no)
            text += f' __{text}__`{superscript_no}`'
            links.append({'no': url_no, 'url':url})
            url_no += 1

        sect_string = f'{fmt[0]}{text}{fmt[1]}'
        string += sect_string

    string += "\n"
    for link in links:
        string += f'`{str(link["no"])}`: https://ojibwe.lib.umn.edu{link["url"]}\n'
    
    return string
