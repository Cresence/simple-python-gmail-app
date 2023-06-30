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
            print(f'\nEmail {i+1}) \n')
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
            try:
                print(msg.text_body)
            except any:
                print("Body: Unknown error occured")
            print("\n-----"*5)
    except:
        print("Line 66, searchResult() did not function properly: Something went wrong.")


# Question Prompt
def runProgram():
    # User Option
    options = ['Y', 'N']
    # User input
    user_input = ''
    input_message = "Pick an option:\n"

    for index, item in enumerate(options):
        input_message += f'{index+1}) {item}\n'

    input_message += 'Your choice: '

    while user_input.upper() not in options:
        user_input = input(input_message)

    # Case-sensitive Input
    user_input = user_input.upper()
    # User picks N (No)
    if user_input == options[1]:
        print('\nGoodbye!')
    # User picks Y (Yes)
    if user_input == options[0]:
        serverQuery(searchTerm(), searchLimits())
        # Check user for concurrent query requests
        runProgram() 
    
        
runProgram()

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