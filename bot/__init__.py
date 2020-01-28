import praw

def info():
    print("Hello!")
    
def make_bot(rUsername, rPassword, rClient, rSecret):
    reddit = praw.Reddit(client_id=rClient, client_secret=rSecret, username=rUsername, passwrod=rPassword)
