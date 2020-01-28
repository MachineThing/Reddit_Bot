from getpass import getpass
import sys, base64

if sys.version_info.major != 3:
    if sys.version_info.major == 2:
        print("Python 2 is not supported! quitting...")
    else:
        print("Unknown python version: \""+str(sys.version_info.major)+"\"! quitting...")
    sys.exit()

if sys.argv[1] == 'init':
    botUsername = input("Bot Username: ")
    botPassword = getpass("Bot Password: ")
    targReddit = input("Target subreddit (where the bot will be active in): ")
    confFile = open('.conf', 'w')
    confFile.write(botUsername.lower()+'\n'+str(base64.b64encode(bytes(botPassword, "ascii")))[2:-1]+'\n'+targReddit.lower())
    confFile.close()
elif sys.argv[1] == 'run':
    try:
        confFile = open('.conf', 'r')
    except FileNotFoundError:
        print("Configuration file not found, did you run \"python3 manage.py init\"? quitting...")
        sys.exit()
    lines = confFile.read().split('\n')
    botUsername = lines[0]
    botPassword = str(base64.b64decode(lines[1]))[2:-1]
    targReddit = lines[2]
    confFile.close()
    print(botPassword)
