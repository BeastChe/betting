import requests
import datetime





today = datetime.date.today()
DAY = []
for i in range (0, 7):
    day = today + datetime.timedelta(days=i)
    DAY.append(day.strftime('%Y%m%d'))
    url = 'https://api.trbna.com/betting_insider/ru/mobile/v2/matches/with_odds'
    payload = {'date': DAY[i], 'category_id': '208', 'bookmaker_id': 'default', 'line_type': 'default', 'tournament_id': 'default', 'include': 'team,odds'}
    headers = {'content-type': 'application/json'}
    matches = requests.get(url, params=payload,  headers=headers)
    print(matches.url)
    print(matches.text)


str = matches.text
size = str.count("rate")


def give_rate():
    RATES = []
    for i in range(0, size):
        response = matches.json()
        rate = response['include']['odds'][i]['rate']
        RATES.append(rate)



