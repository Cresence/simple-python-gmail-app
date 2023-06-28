from dotenv import load_dotenv
load_dotenv()

import imaplib
import email
from email.header import decode_header
import webbrowser
import os

# dotenv variables + account credentials
imap_server = os.environ.get("email-hostname")
username = os.environ.get("email-username")
password = os.environ.get("email-password")
port = os.environ.get("email-port")

def clean(text):
    # clean text for creating a folder
    return "".join(c if c.isalnum() else "_" for c in text)

# create an IMAP4 class with SSL
imap = imaplib.IMAP4_SSL(imap_server)

# authenticate
imap.login(username, password)

# email fetching (if successful)
status, messages = imap.select("INBOX")

# number of top emails to fetch
N = 3

# total number of emails
messages = int(messages[0])

# email loop and extraction
for i in range(messages, messages-n, -1):
    # fetch the email message by ID
    res, msg = imap.fetch(str(i), "(RFC822)")
    for response in msg:
        if isinstance(response, tuple):
            # parse a bytes eail into a message object
            msg = email.message_from_bytes(response[1])
            # decode the email subject
            subject, encoding = decode_header(msg["Subject"])[0]
            if isinstance(subject, bytes):
                # if it's a bytes, decode to str
                subject = subject.decode(encoding)
            # decode email sender
            From, encoding = decode_header(msg.get("From"))[0]
            if isinstance(From, bytes):
                From = From.decode(encoding)
            print("Subject:", subject)
            print("From:", From)
            # if the email message is multipart
            if msg.is_multipart():
                # iterate over email parts
                for part in msg.walk():
                    # extract content type of email
                    content_type = part.get_content_type()
                    content_disposition = str(part.get("Content-Disposition"))
                    try:
                        # get the email body
                        body = part.get_payload(decode=True).decode