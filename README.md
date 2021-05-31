# CommitteeBot
A quickly developed discord bot used to help the running of CompSoc

Current functions include 

`>addEvent "<time>"'  ~ Adds an event into a shared google calendar together with a google meets link

`>meeting`            ~ Sends detail of next meeting. The bot will start fetching events from 15 minutes prior so that any late requests still show the meeting link

Put google calendar id into the calendarAPI.py file, and insert the committee discord channelID into the Main.py file.

## Requirements
Running requires valid Google API credentials in a file called credentials.json (instructions can be found [here](https://developers.google.com/workspace/guides/create-credentials#desktop))
with OAUTH scope set to accept https://www.googleapis.com/auth/calendar. Running for the first time will generate a token.json. A bot token should be placed in `discordToken.scrt`

To install python modules run `pip install -r requirements.txt`
