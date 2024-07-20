# Import necessary libraries for Google API, authentication, and time handling.
import os.path
import pickle
import time
from datetime import datetime
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Define the scope for read-only access to the Gmail API.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

# Path to your credentials file.
CREDENTIALS_FILE = '/Users/aathushankugendran/Desktop/emailf/remy-open-source/Email-Scraping/client_secret_79492345177-pbpjbug8hsdko7ej3r3t60nm81rl5vmt.apps.googleusercontent.com.json'

def authenticate_gmail():
    """
    Authenticate the user and return the credentials object.
    This function handles the OAuth 2.0 flow and token storage.
    """
    creds = None
    token_file = 'token.pickle'

    # Load credentials from the token.pickle file if it exists.
    if os.path.exists(token_file):
        with open(token_file, 'rb') as token:
            creds = pickle.load(token)

    # If there are no valid credentials, perform the OAuth flow to get new ones.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # Run the OAuth 2.0 flow to get new credentials.
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run.
        with open(token_file, 'wb') as token:
            pickle.dump(creds, token)

    return creds

def check_new_emails(service):
    """
    Check the user's inbox for new unread emails and write to a text file.
    """
    # Call the Gmail API to list messages in the inbox with the label 'INBOX' and the query 'is:unread'.
    results = service.users().messages().list(userId='me', labelIds=['INBOX'], q="is:read").execute()
    messages = results.get('messages', [])

    # Generate a timestamp for the filename.
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"emails_{timestamp}.txt"

    if not messages:
        print('No new emails.')
    else:
        with open(filename, 'w') as f:
            print('You have new emails!')
            for message in messages:
                # Get the message details.
                msg = service.users().messages().get(userId='me', id=message['id']).execute()
                snippet = msg['snippet']
                print(f'Message snippet: {snippet}')
                f.write(f'Message snippet: {snippet}\n')

def main():
    """
    Main function to authenticate the user and check for new emails.
    """
    # Authenticate the user and get the credentials.
    creds = authenticate_gmail()
    # Build the Gmail service.
    service = build('gmail', 'v1', credentials=creds)

    # Continuously check for new emails every hour.
    while True:
        check_new_emails(service)
        time.sleep(3600)  # Wait for one hour before checking again.

if __name__ == '__main__':
    main()