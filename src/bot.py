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

def find(string): 
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex,string)       
    return [x[0] for x in url] 

for submission in reddit.subreddit(sub).new(limit=None):
    submission.comments.replace_more(limit=None)
    for comment in submission.comments.list():
        if (re.search('!completed', comment.body) is not None):
                if comment.is_submitter:
                    if submission.saved is False:
                        if (comment.parent().author.name is not submission.author.name):
                            if(find(comment.parent().body) != []):
                                completer = ""
                                if comment.parent().author_flair_text and comment.parent().author_flair_text.endswith("ᚬ"):
                                    count_taker = int(comment.parent().author_flair_text.replace("ᚬ",""))
                                    count_taker += 2
                                    taker_flair = "{0}ᚬ".format(count_taker)
                                    completer = comment.parent().author.name
                                    reddit.subreddit(sub).flair.set(comment.parent().author.name, taker_flair, "QuestFairer")
                                else:
                                    reddit.subreddit(sub).flair.set(comment.parent().author.name, "2ᚬ", "QuestFairer")
                                for flair in reddit.subreddit(sub).flair(redditor="Bobbbay", limit=None):
                                    count_op_str = flair['flair_text']
                                if ( count_op_str != "" ):
                                    count_op = int(count_op_str.replace("ᚬ", ""))
                                    count_op += 1
                                    op_flair = "{0}ᚬ".format(count_op)
                                    reddit.subreddit(sub).flair.set(submission.author.name, op_flair, "QuestFairer")
                                else:
                                    reddit.subreddit(sub).flair.set(submission.author.name, "1ᚬ", "QuestFairer")
                                submission.flair.select(None, "Completed!")
                                submission.save()
                                reply = 'This quest has been completed, but feel free to go ahead and recomplete this quest! \n\n^Upvote ^me ^if ^you ^think ^this ^quest ^was ^quite ^nice^. ^Beep ^boop^. ^Contact ^my ^creator ^Bobbbay^.'
                                submission.reply(reply).mod.distinguish(sticky=True)
                            else:
                                comment.mod.remove()
                                submission.author.message('Your comment in r/redditsquests has been removed', 'We only allow approvals that contain links. It\'s not your fault, but next time make sure the person who has completed the quest provides a link. PM u/MaxwellIsSmall for questions about this sub\'s rules and u/Bobbbay for any questions, concerns, or comments about the bot. ')
                        break