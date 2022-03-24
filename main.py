import sys
import requests
import base64
import sys
from email.mime.text import MIMEText

AccessToken = ""

params = {
        "grant_type":    "refresh_token",
        "client_id":     "xxxxxxxxxxxxxxx",
        "client_secret": "xxxxxxxxxxxxxxx",
        "refresh_token": "xxxxxxxxxxxxxxxxxxxx",
        }

authorization_url = "https://www.googleapis.com/oauth2/v4/token"

r = requests.post(authorization_url, data=params)

if r.ok:
    AccessToken = str((r.json()['access_token']))


EmailFrom = "Test1@gmail.com"
EmailTo = "test2@gmail.com"

def create_message(sender, to, subject, message_text):
   
    message = MIMEText(message_text, 'html')
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    raw = base64.urlsafe_b64encode(message.as_bytes())
    raw = raw.decode()
    body = {'raw': raw}
    return body


body  = create_message(EmailFrom, EmailTo, "Just wanna Say Waka Waka!", "Waka Waka!")


url = "https://gmail.googleapis.com/gmail/v1/users/me/messages/send"

header = {
    'Authorization': 'Bearer ' + AccessToken,
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

r = requests.post(
    url,
    header,
    body
)
print("\n")
print(r.text)
print("\n")








