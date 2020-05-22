'''
reddit = praw.Reddit(client_id="T-VB-ecVtjieoA",
                             client_secret="mC3X2iQkmS6EK6tQXKNg1mT6_H4",
                             user_agent="TheQuestMaster")
'''

import praw
import os
import re

reddit = praw.Reddit(client_id=os.environ.get('client_id'),
                     client_secret=os.environ.get('client_secret'),
                     password=os.environ.get('pass'),
                     user_agent='r/RedditsQuests bot',
                     username='TheQuestMaster')

for submission in reddit.subreddit('RedditsQuests').new(limit=None):
    if 1:
        submission.comments.replace_more(limit=None)
        for comment in submission.comments.list():
            if (re.search('!completed', comment.body) is not None):
                    if comment.is_submitter:
                        if submission.saved is False:
                            completer = ""
                            if comment.parent().author_flair_text and comment.parent().author_flair_text.endswith("ᚬ"):
                                count_op = int(comment.parent().author_flair_text.replace("ᚬ",""))
                                count_taker = int(comment.parent().author_flair_text.replace("ᚬ",""))
                                count_op += 1
                                count_taker += 2
                                op_flair = "{0}ᚬ".format(count_op)
                                taker_flair = "{0}ᚬ".format(count_taker)
                                completer = comment.parent().author.name
                                reddit.subreddit('RedditsQuests').flair.set(submission.author.name, op_flair, "QuestFairer")
                                reddit.subreddit('RedditsQuests').flair.set(comment.parent().author.name, taker_flair, "QuestFairer")
                            else:
                                reddit.subreddit('RedditsQuests').flair.set(submission.author.name, "1ᚬ", "QuestFairer")
                                reddit.subreddit('RedditsQuests').flair.set(comment.parent().author.name, "2ᚬ", "QuestFairer")
                            submission.flair.select(None, "Completed!")
                            submission.save()
                            reply = 'This quest has been completed, but feel free to go ahead and recomplete this quest! Upvote me if you think this quest was quite nice. Good quest creators and/or executors may recieve a prize!\n\n^Beep ^boop^. ^Contact ^my ^creator ^Bobbbay^.'.format(completer)
                            submission.reply(reply).mod.distinguish(sticky=True)
                    break