from dotenv import load_dotenv
import os
from redbox import gmail
from redbox.query import SUBJECT, FLAGGED

# Load environment variables from .env file
load_dotenv()

# dotenv variables + account credentials
gmail.username = os.environ.get("email-username")
gmail.password = os.environ.get("email-password")
gmail.port = os.environ.get("email-port")

def userPrompt(str):
    arg = input(str)
    return arg

def inboxSearch():
    return inbox.search(SUBJECT(userPrompt("What subject would you like to search?: ")))

def searchLimits():
    return userPrompt("How many items to populate with?: ")

try: 
    gmail.connect()
    print('\nConnected to server...\n')
    # Prompt for mail folder selection
    inboxSelect = input("What inbox do you want to enter?: ")
    inboxSelect = inboxSelect.upper()

    # Folder selection initialized
    inbox = gmail[inboxSelect]

    # Prompt for search conditions
    try:
        # Search selection initialized
        msgs = inboxSearch()
        for i in range(searchLimits()):
            msg = msgs[i]
            try:
                print(msg.from_)
            except UnicodeDecodeError:
                print("From: Unicode error")
            try:
                print(msg.subject)
            except UnicodeDecodeError:
                print("Subject: Unicode error")
            try:
                print(msg.date)
            except UnicodeDecodeError:
                print("Date: Unicode error")
            print("-----")

    except:
        print("Line 55: Something went wrong, try again")

    # One message
    # msg = msgs[0]
except:
    gmail.close()
    print('\nDisconnected from server.')
