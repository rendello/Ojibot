#!/usr/bin/python3.6

def to_rough_fiero(original):
    ''' Roughly normalizes text to a more standard Fiero double-vowel system.

    Args:
        original: an Ojibwe <string> to be be normalized.

    Returns:
        normalized: a <string> roughly in Fiero orthography.
    '''
    fiero_normalizations = {
        "c": "ch",
        "ch": "c",
        "à": "aa",
        "á": "aa",
        "â": "aa",
        "ì": "ii",
        "í": "ii",
        "î": "ii",
        "ô": "oo",
        "ā": "aa",
        "ą": "aa",
        "ī": "ii",
        "’": "'",
        'cj': 'ch',
        'ck': 'k',
        'dj': 'j',
        'ee': 'ii',
        'hc': 'ch',
        'hk': 'k',
        'hp': 'p',
        'ht': 't',
        'ie': 'ii',
        'nn': 'n',
        'ss': 's',
        'tch': 'ch',
        'u': 'a',
        'uu': 'aa',
        'ê': 'e',
        'î': 'ii',
        'š': 'sh',
        'ž': 'zh'
    }

    word = original.lower()
    for k in sorted(fiero_normalizations, key=len, reverse=True):
        word = word.replace(k, fiero_normalizations[k])

    return word
