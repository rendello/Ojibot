#!/usr/bin/python3.6

from Core.lookup import fetch_oji_word_info
from Core.db_lookup import fuzzy_match, get_random_word, get_word_urls
from Core.normalize import to_rough_fiero
from Core.format import serialize_all, _format


def to_eng(formatter, word):
    ''' Gets a supposed Ojibwe word from the chat, and gives the definiton and
    other word information. Tries to find the closest word if the spelling's
    not exactly the same.

    Args:
        ctx: context, needed for Discord
        word: <str>, a supposed Ojibwe word.

    Returns:
        string: a <str> of nicely formatted information about the requested
        word (or whatever word's most similar).
    '''

    urls = get_word_urls(word)

    # Find the closest word if the specific requested spelling's not in db
    if urls == []:
        word = to_rough_fiero(word)
        word = fuzzy_match(word, 1)[0]['word'] # Single element list containing dict
        urls = get_word_urls(word)

    # Sometimes there's multiple words with the same definition
    string = ''
    for url in urls:
        info = fetch_oji_word_info(url)
        serialized = serialize_all(info)
        string += _format(formatter, serialized)

    return string


def random_to_eng(formatter):
    string = to_eng(formatter, get_random_word())
    return string
