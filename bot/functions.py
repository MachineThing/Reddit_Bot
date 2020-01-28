def get_comments(subreddit):
    posts = subreddit.hot(limit=5)
    for submission in posts:
        print(submission.title)
