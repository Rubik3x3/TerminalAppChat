import pyrebase
import creds
import functions

import os
from rich import print

firebaseConfig=creds.firebaseConfig

firebase=pyrebase.initialize_app(firebaseConfig)

auth=firebase.auth()

initSession = ("Not login")

def mainMenu():
    pass

def menuSession():
    print("[bold white]Select option:[/bold white]\n\n[1] Log in\n[2] Register\n[3] Exit\n")
    ans=int(input("Option: "))
    if ans == 1:
        default(initSession)
        login()
    elif ans == 2:
        default(initSession)
        signup()
    elif ans == 3:
        functions.clear()
        exit()
    else:
        default(initSession)
        menuSession()

def default(iSession):
    if os.name == "nt":
        os.system("cls")
        print("[bold blue][ Terminal App Chat][/bold blue] [cyan][Version 1.0.0][/cyan] [bold magenta][ "+iSession+" ][/bold magenta]\n[bright_black][     Developer by Franco Salvador Talarico      ][/bright_black]\n")
    else:
        os.system("clear")
        print("[bold blue][ Terminal App Chat][/bold blue] [cyan][Version 1.0.0][/cyan] [bold magenta][ "+iSession+" ][/bold magenta]\n[bright_black][     Developer by Franco Salvador Talarico      ][/bright_black]\n")

def login():
    print("[white white][ Log In ][/white white]\n")
    print("[i bright_black]Enter email: [/i bright_black]",end="")
    email=input()
    print("[i bright_black]Enter password: [/i bright_black]",end="")
    password=input()
    try:
        login = auth.sign_in_with_email_and_password(email,password)
        functions.notify("Successfully logged in!")
        default(email)
    except:
        functions.notify("Invalid email or password.")

def signup():
    print("[white white][ Register ][/white white]\n")
    print("[i bright_black]Enter email: [/i bright_black]",end="")
    email=input()
    print("[i bright_black]Enter password: [/i bright_black]",end="")
    password=input()
    try:
        user = auth.create_user_with_email_and_password(email,password)
        functions.notify("Successfully register!")
        default(email)
    except:
        functions.notify("Email already exist.")
    return

default(initSession)

menuSession()