#!/usr/bin/python3.6

import praw

import Core.backend as backend

from Core.secrets import reddit as r
from Core.detect_language import is_english


reddit = praw.Reddit(client_id=r['client_id'],
                     client_secret=r['client_secret'],
                     user_agent=r['user_agent'],
                     username=r['username'],
                     password=r['password']
                     )


def normalize(text):
    return text.lower().strip()


def strip_mention(text):
    return text.replace('/u/ojibot', '', 1)


for mention in reddit.inbox.mentions(limit=10):
    body = strip_mention(normalize(mention.body))


    # ... todo specific commands here


    # No commands? The user must just want some text translated. Find out if
    # it's English or Ojibwe so you can translate in the right direction.

    # No text after the mention even? They must want the previous comment
    # translated.
    if body == '':
        parent = mention.parent()

        # Check if parent is a comment and not the submission
        if type(parent) == praw.models.reddit.comment.Comment:
            body = normalize(parent.body)
        else:
            #mention.reply('No command, translatable text, or parent comment found.')
            print('No command, translatable text, or parent comment found.')
            continue

    if is_english(body):
        pass
    else:
        #mention.reply(backend.to_eng('reddit', body))
        print(backend.to_eng('reddit', body))
