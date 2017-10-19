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
    SIZES = []
    def give_size():
        print(i)
        str = matches.text
        print(str)
        size = str.count("rate")
        print(size)
        SIZES.append(size)
        print(SIZES)
        return SIZES
        RATES = []
        def give_rates():
            for x in range(0, SIZES[i]):
                response = matches.json()
                rate = response['include']['odds'][x]['rate']
                RATES.append(rate)
            return RATES
        ODDS_ID = []
        def give_odds():
            for x in range(0, SIZES[i]):
                response = matches.json()
                odds_id = response['include']['odds'][x]['id']
                ODDS_ID.append(odds_id)
            return ODDS_ID


A = []
B = []
C = []

A = give_size()
#B = give_rates()
#C = give_odds()

print(A)
#print(B)
#print(C)





