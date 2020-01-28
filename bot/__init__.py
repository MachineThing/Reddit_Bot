import praw, datetime, platform

def make_bot(rUsername, rPassword, rClient, rSecret, rTargSub):
    reddit = praw.Reddit(client_id=rClient, client_secret=rSecret, username=rUsername, password=rPassword, user_agent=str(platform.platform())+':machinethingbot by MachineThing')
    subreddit = reddit.subreddit(rTargSub)
    time = datetime.datetime.now()
    return {'time':[int(str(time.year)[2:]), time.month, time.day, time.hour, time.minute, time.second], 'bot':reddit, 'subreddit':subreddit}

from .functions import *
