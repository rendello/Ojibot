#!/usr/bin/python3.6

from random import randint

from fuzzywuzzy import fuzz
from fuzzywuzzy import process

import sqlite3
from Core.Tools.db_context_manager import dbopen

from Core.normalize import to_rough_fiero


def fuzzy_match(requested_word, no_of_returns):
    ''' Returns a the best fuzzy matches for a requested word.

    Args:
        requested_word: <str>, an Ojibwe word to be fuzzy-searched.
        no_of_returns: an <int> of how many top matches are returned.

    Returns:
        highest_matches: a <list> of <dict>s, which are in the format
        {'word'=<str>, 'ratio'=<int>}, sorted from highest to lowest match
        ratio.
    '''
    highest_matches = [{'word':None,'ratio':0}] * no_of_returns
    with dbopen('Core/words.db') as c:
        c.execute('SELECT title FROM words;')
        for result in c.fetchall():
            returned_text = result[0]
            ratio = fuzz.ratio(requested_word, returned_text)
            db_word = {'word': returned_text, 'ratio': ratio}

            highest_index = 0
            for index, word in enumerate(highest_matches):
                if db_word not in highest_matches:
                    if db_word['ratio'] > word['ratio']:
                        highest_index = index + 1
                        if index == len(highest_matches) - 1:
                            highest_matches.insert(highest_index, db_word)
                            highest_matches.pop(0)
                    else:
                        if highest_index != 0:
                            highest_matches.insert(highest_index, db_word)
                            highest_matches.pop(0)
        highest_matches.reverse()
        return highest_matches


def get_random_word():
    with dbopen('Core/words.db') as c:
        c.execute('SELECT MAX(rowid) FROM words')
        ceiling = c.fetchone()[0]
        rand_id = randint(0, ceiling)
        c.execute('SELECT title FROM words WHERE rowid=?', [rand_id])
        word = c.fetchone()[0]
    return word
