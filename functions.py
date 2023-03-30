import os

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def notify(message):
    if os.name == "nt":
        pass
    else:
        os.system("notify-send 'Python App Chat' '{}'".format(message))