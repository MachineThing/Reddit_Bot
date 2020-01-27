from getpass import getpass
import sys, hashlib

if sys.version_info.major != 3:
    if sys.version_info.major == 2:
        print("Python 2 is not supported! quitting...")
    else:
        print("Unknown python version: \""+str(sys.version_info.major)+"\"! quitting...")
    sys.exit()

if sys.argv[1] == 'init':
    botUsername = input("Bot Username: ")
    botPassword = getpass("Bot Password: ")
    confFile = open('.conf', 'w')
    confFile.write(botUsername.lower()+'\n'+hashlib.sha224(bytes(botPassword, "ascii")).hexdigest())
    confFile.close()
elif sys.argv[1] == 'run':
    try:
        confFile = open('.conf', 'r')
    except FileNotFoundError:
        print("Configuration file not found, did you run \"python3 manage.py init\"? quitting...")
        sys.exit()
    lines = confFile.read().split('\n')
    botUsername = lines[0]
    botPassword = lines[1]
    confFile.close()
    print(botSecret)
