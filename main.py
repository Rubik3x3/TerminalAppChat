import pyrebase
import creds
import functions

import os
from rich import print

firebaseConfig=creds.firebaseConfig

firebase=pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

auth=firebase.auth()

initSession = ("Not login")

uid = ""

def mainMenu(email,nick):
    print("[bold white]Main Menu, select option:[/bold white]\n\n[1] Join Chat\n[2] Create Chat\n[3] Exit\n")
    ans=int(input("Option: "))
    if ans == 1:
        print(nick)
    elif ans == 2:
        createChat(email,nick)
    elif ans == 3:
        functions.clear()
        exit()
    else:
        default(email)
        mainMenu(email,nick)

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
        nick = db.child("users").child(login['localId']).get()
        default(email)
        mainMenu(email,nick)
    except:
        functions.notify("Invalid email or password.")

def createChat(email,nick):
    default(email)
    print("[white white][ CREATE CHAT ][/white white]\n")
    ans = str(input("Enter the chat name: "))
    data = {
        "name": ans,
        "mensajes":{

        }
    }
    db.child("chats").push(data)
    db.child(uid['localId']).child("chats").set(data)
def signup():
    print("[white white][ Register ][/white white]\n")
    print("[i bright_black]Enter email: [/i bright_black]",end="")
    email=input()
    print("[i bright_black]Enter password: [/i bright_black]",end="")
    password=input()
    print("[i bright_black]Enter the Nick: [/i bright_black]",end="")
    nick=str(input())
    try:
        global uid
        user = auth.create_user_with_email_and_password(email,password)
        data = {
            "nick": nick
        }
        uid = user['localId']
        results = db.child("users").child(uid).set(data)
        functions.notify("Successfully register!")
        default(email)
        mainMenu(email,nick)
    except:
        functions.notify("Email already exist.")
    return

default(initSession)

menuSession()