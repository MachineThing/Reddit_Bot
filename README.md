# Reddit bot

This is a Reddit bot I made in Python.

## How to run:

Just run the command:

```shell
python3 manage.py init
```

to make a .conf file, you will need to make a Reddit account and a [Reddit app](www.reddit.com/prefs/apps) first. And then after that to run the bot, run the command:

```shell
python3 manage.py run
```

this will create a database if not already and monitor for new comments and do actions if the comments contain a command like `!systeminfo`.

## Commands:

| command name | effect |
| --- | --- |
| !systeminfo | replies out the system info (the platform name and version and Python version and other things)

© Mason Fisher 2020
