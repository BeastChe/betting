import requests
import json
import matches
import rndUserInfo
import userInfo

if matches

url = 'https://api.trbna.com/betting_insider/ru/mobile/v2/bets/'
payload = {"data": {"odds_id": "1488",
    "amount": 500,
    "rate": 2.15,
    "comment": "А вот так вот )"
  }
}
headers = {'content-type': 'application/json', 'Authorization': 'Bearer ' + userInfo.token}
bets = requests.post(url, data=json.dumps(payload), headers=headers)