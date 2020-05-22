'''
reddit = praw.Reddit(client_id="T-VB-ecVtjieoA",
                             client_secret="mC3X2iQkmS6EK6tQXKNg1mT6_H4",
                             user_agent="TheQuestMaster")
'''

import praw
import os
import re

reddit = praw.Reddit(client_id='T-VB-ecVtjieoA',
                     client_secret='mC3X2iQkmS6EK6tQXKNg1mT6_H4',
                     password='iamabot002',
                     user_agent='r/redditsquestsbot',
                     username='TheQuestMaster')

for submission in reddit.subreddit('bobbbaybots').new(limit=None):
    if 1:
        submission.comments.replace_more(limit=None)
        for comment in submission.comments.list():
            print(comment.body)
            if (re.search('!completed', comment.body) is not None):
                    if comment.is_submitter:
                        if submission.saved is False:
                            completer = ""
                            if comment.parent().author_flair_text and comment.parent().author_flair_text.endswith("Ջ"):
                                count = int(comment.parent().author_flair_text.replace("Ջ",""))
                                count += 1
                                newflair = "{0}Ջ".format(count)
                                completer = comment.parent().author.name
                                reddit.subreddit('bobbbaybots').flair.set(comment.parent().author.name, newflair, "QuestFairer")
                                print("EDITED FLAIR")
                            else:
                                reddit.subreddit('bobbbaybots').flair.set(comment.parent().author.name, "1Ջ", "QuestFairer")
                                print("NEWBYYYY")
                            submission.save()
                            reply = 'This quest has been completed by {0}, but feel free to go ahead and recomplete this quest! \n\n^Beep ^boop^. ^Contact ^my ^creator ^Bobbbay^.'.format(completer)
                            submission.reply(reply).mod.distinguish(sticky=True)
                    break
    
