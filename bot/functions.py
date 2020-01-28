def reply_comment(comment):
    print(comment)
    if comment.body == '!systeminfo':
        comment.reply("Hi there!")
