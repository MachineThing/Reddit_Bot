import praw, datetime

def make_bot(rUsername, rPassword, rClient, rSecret):
    reddit = praw.Reddit(client_id=rClient, client_secret=rSecret, username=rUsername, password=rPassword, user_agent=rUsername)
    time = datetime.datetime.now()
    return [[int(str(time.year)[2:]), time.month, time.day, time.hour, time.minute, time.second], reddit]
