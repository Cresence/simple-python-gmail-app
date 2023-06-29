from dotenv import load_dotenv
import os
import imaplib
import email
import ssl

# Load environment variables from .env file
load_dotenv()

# dotenv variables + account credentials
IMAP_SERVER = os.environ.get("email-hostname")
USERNAME = os.environ.get("email-username")
PASSWORD = os.environ.get("email-password")
PORT = os.environ.get("email-port")

# Create an SSL context and disable certificate validation
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

# Connect to the IMAP server
imap = imaplib.IMAP4_SSL(IMAP_SERVER, PORT, ssl_context=context)

# Login to your account
imap.login(USERNAME, PASSWORD)

# Select the mailbox you want to read emails from (e.g., 'INBOX')
mailbox = 'INBOX'
imap.select(mailbox)

# Search for emails in the selected mailbox
status, data = imap.search(None, 'ALL')
email_ids = data[0].split()

# Iterate over the email IDs and fetch the email contents
for email_id in email_ids:
    # Fetch the email based on the ID
    status, data = imap.fetch(email_id, '(RFC822)')
    raw_email = data[0][1]

    # Parse the raw email content
    msg = email.message_from_bytes(raw_email)

    # Extract email information
    subject = msg['Subject']
    sender = msg['From']
    date = msg['Date']

    # Print email details
    print(f"Subject: {subject}")
    print(f"From: {sender}")
    print(f"Date: {date}")

    # Process email body
    if msg.is_multipart():
        # If the email has multiple parts, iterate over them
        for part in msg.walk():
            content_type = part.get_content_type()
            if content_type == 'text/plain':
                body = part.get_payload(decode=True).decode('utf-8')
                print(f"Body: {body}")
    else:
        # If the email is not multipart, simply extract the body
        body = msg.get_payload(decode=True).decode('utf-8')
        print(f"Body: {body}")

    print('-' * 50)

# Logout and close the connection
imap.logout()
imap.close()