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


