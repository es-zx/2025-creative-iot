import socket

import requests

TG_BOT_TOKEN = "你的_bot_token"
TG_CHAT_ID = "你的_chat_id"
def send_to_telegram(message):
    url = f"https://api.telegram.org/bot{TG_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": TG_CHAT_ID, "text": message}
    try:
        requests.post(url, data=payload)
    except Exception as e:
        print("Telegram 傳送失敗：", e)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ("192.168.137.42", 8888)
client_socket.connect(server_address)

while True:
    command = input("請輸入指令（on/off）：")
    client_socket.send(command.encode())
    # 新增：接收 server 回傳的訊息
    response = client_socket.recv(1024).decode()
    print("Server 回應：", response)

    # 傳送 server 回應到 Telegram bot
    send_to_telegram(f"Server 回應：{response}")

client_socket.close()