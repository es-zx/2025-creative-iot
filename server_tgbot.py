
import socket
import RPi.GPIO as GPIO
import requests
# vim: set fileencoding=utf-8 :

TG_BOT_TOKEN = "你的_bot_token"
TG_CHAT_ID = "你的_chat_id"
def send_to_telegram(message):
    url = f"https://api.telegram.org/bot{TG_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": TG_CHAT_ID, "text": message}
    try:
        requests.post(url, data=payload)
    except Exception as e:
        print("Telegram 傳送失敗：", e)

led_pin = 21
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led_pin, GPIO.OUT)

def control_led(state):
    
    if state == "on":
        GPIO.output(led_pin, GPIO.HIGH)
        msg = "LED on"
    elif state == "off":
        GPIO.output(led_pin, GPIO.LOW)
        msg = "LED close"
    else:
        msg = f"state : {state}"
    print(msg)
    send_to_telegram(msg)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("192.168.137.42", 8888))
server_socket.listen(1)

client_socket, client_address = server_socket.accept()



while True:
    try:
        data = client_socket.recv(1024)
        if data:
            command = data.decode().strip()
            control_led(command)
            # 傳送收到的指令到 Telegram bot
            send_to_telegram(f"收到指令: {command}")
    except KeyboardInterrupt:
        break

client_socket.close()
server_socket.close()
GPIO.cleanup()
