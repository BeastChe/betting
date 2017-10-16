import requests
import json
import rndUserInfo
import userInfo
import csv

url = 'https://api.trbna.com/betting_insider/ru/mobile/v2/user/generate/'
payload = {"data": {"email": rndUserInfo.generate_random_emails(), "id": userInfo.id,
                    "name": rndUserInfo.generate_random_nic()}}
headers = {'content-type': 'application/json', 'Authorization': 'Bearer ' + userInfo.token}
generate = requests.post(url, data=json.dumps(payload), headers=headers)


if generate.status_code == 200:
   with open('/Users/chechetkin/Desktop/python/users.csv', 'a', newline='') as csvfile:
        user = csv.writer(csvfile, delimiter=' ',
                           quoting=csv.QUOTE_MINIMAL)
        user.writerow([userInfo.id, userInfo.token, rndUserInfo.generate_random_emails(), rndUserInfo.generate_random_password(), rndUserInfo.generate_random_nic()])
else:
    print("ПОЛЬЗОВАТЕЛЬ НЕ СОЗДАЛСЯ")
    print(generate.status_code)
    print(generate.json())
