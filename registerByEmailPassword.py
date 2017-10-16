import requests
import json
import rndUserInfo



rndmail = rndUserInfo.generate_random_emails()
rndpass = rndUserInfo.generate_random_password()


url = 'https://api.trbna.com/betting_insider_user_auth/ru/mobile/v1/uid/register_by_email_password/'
payload = {"data":{"email":rndmail,"password":rndpass}}
headers = {'content-type': 'application/json'}

register_by_email_password = requests.post(url, data=json.dumps(payload), headers=headers)

def  give_token():
     response = register_by_email_password.json()
     token = response['state']['session']['id']
     return token


def give_id():
    response = register_by_email_password.json()
    id = response['result']['id']
    return id










