from dotenv import load_dotenv
import os
from redbox import gmail
from redbox.query import SUBJECT, FLAGGED
import time

# Load environment variables from .env file
load_dotenv()

# dotenv variables + account credentials
gmail.username = os.environ.get("email-username")
gmail.password = os.environ.get("email-password")
gmail.port = os.environ.get("email-port")
# Defined email folder
inbox = gmail.inbox

def serverQuery(subject, limit):
    try:
        # Connect to server
        print('Connecting to server...\n')
        gmail.connect()
        searchResult(subject, limit)
    except:
        # End connection if error
        print("Line 23, severQuery(): Something went wrong.")
        gmail.close()
        print('\nDisconnected from server.')

    # Search satisfied, connection ended.
    gmail.close()
    print('\nDisconnected from server.')

def userPrompt(str):
    arg = input(str)
    return arg

def searchTerm():
    input = userPrompt("What subject would you like to search?: ")
    print("\nYou choose: " + input)
    return inbox.search(SUBJECT(input))

def searchLimits():
    input = userPrompt("How many items to populate with?: ")
    print("\nYou choose: " + input)
    return int(input)

def searchResult(msgs, limit):
    print("Searching...")
    time.sleep(5)
    try: 
        for i in range(limit):
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
                print("\n")
            except UnicodeDecodeError:
                print("Date: Unicode error")
            except ValueError:
                print("Date: Value error")
            except any:
                print("Unknown error occured")
            print("-----")
    except:
        print("Line 66, searchResult() did not function properly: Something went wrong.")


# Question Prompt
def runProgram():
    # User Option
    options = ['Y', 'N']
    # User input
    userInput = ''
    msg = userPrompt('Would you like to search your email?\n')
    for index, item in enumerate(options):
        status += f'{index+1}) {item}\n'
    
    msg += "Your choice: "

    while userInput.upper() not in options:
        userInput = input(msg)
    # User picks N (No)
    if userInput == options[1]:
        print('You picked: ' + userInput)
        print('\nGoodbye!')
    # User picks Y (Yes)



# Static search test:
# msgs = inbox.search(SUBJECT("bill"))
# msg = msgs[0]
# print(msg)
# for i in range(10):
#     msg = msgs[i]
#     try:
#         print(msg.from_)
#     except UnicodeDecodeError:
#         print("From: Unicode error")
#     try:
#         print(msg.subject)
#     except UnicodeDecodeError:
#         print("Subject: Unicode error")
#     try:
#         print(msg.date)
#     except UnicodeDecodeError:
#         print("Date: Unicode error")
#     except ValueError:
#         print("Date: Value error")
#     except any:
#         print("Unknown error occured")
#     print("-----")