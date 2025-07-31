import RPi.GPIO as GPIO
import time
import requests #pip install requests

#ThinkSpeak的APIKEY 每個人都不一樣 需要自行修改
Think_Speak_APIKEY = 'DBTCB37O8I7BYIQF'
#傳送資料的時間間隔
detection_period = 5
GPIO.setmode(GPIO.BCM) #自行設定呼叫pin腳的模式 BCM or Board
#自行設定GPIO的PIN腳
T = 27  #Trig
E = 22 #Echo

GPIO.setup(T,GPIO.OUT)
GPIO.setup(E,GPIO.IN)

#參考第五周的課程內容 實作距離感測器的function
def dis():
    GPIO.output(T,False)
    time.sleep(0.5)

    GPIO.output(T,True)
    time.sleep(0.00001)
    GPIO.output(T,False)

    pulse_start = time.time()
    pulse_end = time.time()

    while GPIO.input(E) == 0:
        pulse_start = time.time()

    while GPIO.input(E) == 1:
        pulse_end = time.time()
    
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration*17150
    distance = round(distance,2)
    return distance
    pass
while True :
    distance = dis()
    if distance is not None:
        Think_Speak_URL = f'https://api.thingspeak.com/update?api_key={Think_Speak_APIKEY}&' \
                            f'field1={"{0:0.1f}".format(distance)}&'
        query = requests.get(Think_Speak_URL)
        print(f'HTTP:{query.status_code}')
        print('距離:',distance,"公分")
    else:
        print("Failed to get reading")
    time.sleep(detection_period)

GPIO.cleanup()