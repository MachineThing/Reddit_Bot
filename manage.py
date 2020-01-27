import sys

if sys.version_info.major != 3:
    if sys.version_info.major == 2:
        print("Python 2 is not supported! quitting...")
    else:
        print("Unknown python version: \""+str(sys.version_info.major)+"\"! quitting...")
    sys.exit()

if sys.argv[1] == 'init':
    botId = input("Bot ID: ")
    botSecret = input("Bot Secret: ")
    confFile = open('.conf', 'w')
    confFile.write(botId+'\n'+botSecret)
    confFile.close()
elif sys.argv[1] == 'run':
    try:
        confFile = open('.conf', 'r')
    except FileNotFoundError:
        print("Configuration file not found, did you run \"python3 manage.py init\"? quitting...")
        sys.exit()
    lines = confFile.read().split('\n')
    botId = lines[0]
    botSecret = lines[1]
    confFile.close()
    print(botSecret)
