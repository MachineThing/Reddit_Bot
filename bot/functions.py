def init_database():
    import sqlite3
    database = sqlite3.connect('db.sqlite3')

def reply_comment(comment):
    if comment.body == '!systeminfo':
        import platform
        f_reply = "# System info:\n"
        f_reply += "\n- Platform name: "+platform.system()
        f_reply += "\n- Platform release: "+platform.release()

        if platform.system() == 'Linux':
            import distro
            f_reply += "\n- **Linux distrobution info:**\n"
            distro = distro.linux_distribution()
            if distro[0] != '':
                f_reply += "\n\t- Distro name: "+distro[0]
            else:
                f_reply += "\n\t- Distro name: unknown"
            if distro[1] != '':
                f_reply += "\n\t- Distro version: "+distro[1]
            else:
                f_reply += "\n\t- Distro version: unknown"
            if distro[2] != '':
                f_reply += "\n\t- Distro codename: "+distro[2]
            else:
                f_reply += "\n\t- Distro codename: not available"

        f_reply += "\n# Python info:\n"
        f_reply += "\n- Python version: "+platform.python_version()
        if platform.python_implementation() != '':
            f_reply += "\n- Python implementation: "+platform.python_implementation()
        else:
            f_reply += "\n- Python implementation: unknown"
        f_reply += "\n- **Python build info:**"
        if platform.python_compiler() != '':
            f_reply += "\n\t- Python compiler: "+platform.python_compiler()
        else:
            f_reply += "\n\t- Python compiler: unknown"
        if platform.python_build()[1] != '':
            f_reply += "\n\t- Python build date: "+platform.python_build()[1]
        else:
            f_reply += "\n\t- Python build date: unknown"

        comment.reply(f_reply)
