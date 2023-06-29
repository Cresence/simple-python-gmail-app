from dotenv import load_dotenv
import os
from redbox import gmail
from redbox.query import SUBJECT, UNSEEN

# Load environment variables from .env file
load_dotenv()

# dotenv variables + account credentials
gmail.username = os.environ.get("email-username")
gmail.password = os.environ.get("email-password")
gmail.port = os.environ.get("email-port")

gmail.connect()

inbox = gmail["INBOX"]

msgs = inbox.search(subject="bill")

print(type(msgs))

# All message subjects
for msg in msgs:
    print(msg.subject)


# Get raw message content
# print(type(msg.content))

# Convert to email.messages.EmailMessage (from standard library)
# print(type(msg.email))

gmail.close()
