'''
reddit = praw.Reddit(client_id="T-VB-ecVtjieoA",
                             client_secret="mC3X2iQkmS6EK6tQXKNg1mT6_H4",
                             user_agent="TheQuestMaster")
'''

import praw
import os
import re

sub = "RedditsQuests"

client_id = "T-VB-ecVtjieoA" # os.environ.get('client_id')
client_secret = "mC3X2iQkmS6EK6tQXKNg1mT6_H4" # os.environ.get('client_secret')
password = "iamabot002" # os.environ.get('pass')

reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     password=password,
                     user_agent='r/RedditsQuests bot',
                     username='TheQuestMaster')

for submission in reddit.subreddit(sub).new(limit=None):
    if 1:
        print(submission.flair.choices())
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
                                reddit.subreddit(sub).flair.set(submission.author.name, op_flair, "QuestFairer")
                                reddit.subreddit(sub).flair.set(comment.parent().author.name, taker_flair, "QuestFairer")
                            else:
                                reddit.subreddit(sub).flair.set(submission.author.name, "1ᚬ", "QuestFairer")
                                reddit.subreddit(sub).flair.set(comment.parent().author.name, "2ᚬ", "QuestFairer")
                            submission.flair.select("4b693aec-88af-11ea-987a-0ed65c655b8f", "Completed!")
                            print(submission.flair.choices())
                            submission.save()
                            reply = 'This quest has been completed, but feel free to go ahead and recomplete this quest! \n\nUpvote me if you think this quest was quite nice. Good quest creators and/or executors may recieve a prize!\n\n^Beep ^boop^. ^Contact ^my ^creator ^Bobbbay^.'.format(completer)
                            submission.reply(reply).mod.distinguish(sticky=True)
                    break