import praw
import os
import re

sub = "RedditsQuests"

client_id = os.environ.get('client_id')
client_secret = os.environ.get('client_secret')
password = os.environ.get('pass')

reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     password=password,
                     user_agent='r/RedditsQuests bot',
                     username='TheQuestMaster')

for flair in reddit.subreddit(sub).flair(limit=None):
    print(flair)
    
print(reddit.subreddit(sub).flair.delete_all())