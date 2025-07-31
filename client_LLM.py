import socket
from LLM import ask_gemini

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ("192.168.137.42", 8888)
client_socket.connect(server_address)

while True:
    sentence = input("請輸入句子（Ctrl+C 結束）：")
    command = ask_gemini(f"請判斷以下句子是正面還是負面，只能回答'on'或'off'，正面請回答'on'，負面請回答'off'：{sentence}")
    print(f"LLM送出指令：{command}")
    client_socket.send(command.strip().encode())

client_socket.close()
