import sys

if sys.version_info.major != 3:
    print("Bad python version: \""+str(sys.version_info.major)+"\" quitting...")
    sys.exit()
print("hi")
