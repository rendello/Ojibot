#!/usr/bin/python3.6

import praw

import Core.backend as backend

from Core.secrets import reddit as r


reddit = praw.Reddit(client_id=r['client_id'],
                     client_secret=r['client_secret'],
                     user_agent=r['user_agent'],
                     username=r['username'],
                     password=r['password']
                     )



for mention in reddit.inbox.mentions(limit=1):
    print(mention.body)
    #mention.reply(backend.to_eng('reddit', 'Anishinaabemowin'))
    print(backend.to_eng('reddit', 'Anishinaabemowin'))
