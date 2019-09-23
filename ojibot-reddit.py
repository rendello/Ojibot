#!/usr/bin/python3.6

import praw

reddit = praw.Reddit(client_id='kG--QWUCV9GZlg',
                     client_secret=secret_token,
                     user_agent='my user agent',
                     username='my username',
                     password='my password')

print(reddit.read_only)  # Output: False
