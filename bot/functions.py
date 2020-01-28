def init_database():
    import sqlite3
    database = sqlite3.connect('db.sqlite3')

def reply_comment(comment):
    if comment.body == '!systeminfo':
        comment.reply("Hi there!")
