#!/usr/bin/python3.6

import sqlite3
from db_context_manager import dbopen

with dbopen('Core/words.db') as c:
    
    with open('Core/common-english-words.txt') as f:
        for line in f:
            c.execute('INSERT INTO common_english_words(word) VALUES(?)', [line.strip('\n')])
