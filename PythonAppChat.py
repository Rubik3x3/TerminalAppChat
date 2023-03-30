import pyrebase
import creds

firebaseConfig=creds.firebaseConfig

firebase=pyrebase.initialize_app(firebaseConfig)

auth=firebase.auth()

def login():
    print("Log in...")
    email=input("Enter email: ")
    password=input("Enter password: ")
    try:
        login = auth.sign_in_with_email_and_password(email,password)
        print("Successfully logged in!")
    except:
        print("Invalid email or password.")



def signup():
    print("Sign up...")
    email = input("Enter email: ")
    password=input("Enter password: ")
    try:
        user = auth.create_user_with_email_and_password(email,password)
    except:
        print("Email already exist.")
    return

ans=str(input("Area you a new user? [y/n]"))

if ans == 'n':
    login()
elif ans == 'y':
    signup()