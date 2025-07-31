import time
import requests
READ_APIKEY = '0132WFV7194G8MZ5'
#https://api.thingspeak.com/channels/2900335/feeds.json?api_key=0132WFV7194G8MZ5&results=1
FIELD_NUMBER = 1

url = "https://api.thingspeak.com/channels/2900335/feeds.json?api_key=0132WFV7194G8MZ5&results=1"


# 顯示 ThingSpeak 資料
while True:
    response = requests.get(url)
    data = response.json()
    for feed in data['feeds']:
        print(feed['created_at'], feed[f'field{FIELD_NUMBER}'])
    time.sleep(1)
