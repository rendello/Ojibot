#!/usr/bin/python3.6

import sqlite3
import re

from Core.db_context_manager import dbopen

def is_english(text):
    ''' Returns True is text is likely English, False if not.

    Splits text into words and checks those words against the database of
    common English words. If the ratio of English words / total words is high
    enough, returns True.

    Args:
        text: a <string> of text.

    Returns:
        <bool> True (is English) or False (probably not).
    '''

    # Makes string alphanumeric but keeps apostrophes
    alphanumeric_text = re.sub(r"[^a-zA-Z']", ' ', text).lower()
    words = alphanumeric_text.split()

    no_of_words = len(words)
    no_of_english_words = 0

    # No need + no division by 0
    if no_of_words == 0:
        return False

    with dbopen('Core/words.db') as c:
        for word in words:
            c.execute('SELECT word FROM common_english_words WHERE word=?', [word])
            if c.fetchone() is not None:
                no_of_english_words += 1

    ratio = no_of_english_words / no_of_words
    if ratio > 0.6:
        return True
    return False
