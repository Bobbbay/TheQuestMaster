import praw

reddit = praw.Reddit(client_id="T-VB-ecVtjieoA",
                             client_secret="mC3X2iQkmS6EK6tQXKNg1mT6_H4",
                             user_agent="TheQuestMaster")

for submission in reddit.subreddit("learnpython").hot(limit=10):
        print(submission.title)
