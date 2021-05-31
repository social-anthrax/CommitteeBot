from __future__ import print_function
import datetime
import os.path
from googleapiclient.discovery import Resource, build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


def authorize():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    return build('calendar', 'v3', credentials=creds)




def getEvents(self, results):
    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
    events_result = self.events().list(calendarId='comp-soc.com_1k2f1gda8js9nav1ilr5g5h6vk@group.calendar.google.com', timeMin=now,
                                          maxResults=results, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        return 'No upcoming events found.'
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        return '\n'.join(start.split('T')) + '\n' + event['summary'] + '\n' + event["hangoutLink"]


Resource.getEvents = getEvents

if __name__ == '__main__':
    service = authorize()
    print(service.getEvents(2))
