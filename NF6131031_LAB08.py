import RPi.GPIO as GPIO
import time
from linebot import LineBotApi
from linebot.models import TextSendMessage

# LINE 設定
CHANNEL_ACCESS_TOKEN = 'J7e2S2Uod0Zba9fSc2guhveM+iGXUnY+vseo4wlftTQ+ryFX3TvxWsw/skmh9e/BAXumyDjsho6LllLwdkydvYd1OJfdBQI5S3Hop361L/QzDCHFuZiFsDBkNgphVoKFmCapgh8HdYVJJ9U5e6GQHwdB04t89/1O/w1cDnyilFU='
USER_ID = 'Ua464659fde889810efe050db7104fe4b'

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

# HC-SR04 腳位設定
TRIG = 17
ECHO = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def get_distance():
    GPIO.output(TRIG, False)
    time.sleep(0.05)
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    return round(distance, 2)

def send_line_message(text):
    message = TextSendMessage(text=text)
    line_bot_api.push_message(to=USER_ID, messages=[message])

try:
    print("開始距離偵測（Ctrl+C 中斷）")
    while True:
        distance = get_distance()
        print(f"距離：{distance} cm")
        send_line_message(f"📏 距離為：{distance} cm")
        time.sleep(3)

except KeyboardInterrupt:
    print("\n程式中止")

finally:
    GPIO.cleanup()
