#!/usr/bin/python3.6

from fuzzywuzzy import fuzz
from fuzzywuzzy import process

import sqlite3
from Tools.db_context_manager import dbopen

requested_word = "Gwayahkooshkawin"

def fuzzy_match(requested_word):
    highest_match = {'word':None, 'ratio':0}
    with dbopen('words.db') as c:
        c.execute('SELECT title FROM words;')
        for result in c.fetchall():
            db_word = result[0]
            ratio = fuzz.ratio(requested_word, db_word)
            if ratio > highest_match['ratio']:
                highest_match = {'word': db_word, 'ratio': ratio}
    return highest_match

print(fuzzy_match('wasamoo'))
