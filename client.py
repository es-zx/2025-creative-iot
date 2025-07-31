import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ("192.168.137.42", 8888)
client_socket.connect(server_address)

while True:
    command = input("請輸入指令（on/off）：")
    client_socket.send(command.encode())

client_socket.close()
