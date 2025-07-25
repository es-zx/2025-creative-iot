import socket
import RPi.GPIO as GPIO
# vim: set fileencoding=utf-8 :
led_pin = 21
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led_pin, GPIO.OUT)

def control_led(state):
    
    if state == "on":
        GPIO.output(led_pin, GPIO.HIGH)
        print("LED on")
    elif state == "off":
        GPIO.output(led_pin, GPIO.LOW)
        print("LED close")
    else:
        print(f"state : {state}")

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
            # 新增：根據指令回傳訊息給 client
            if command == "on":
                client_socket.send("LED 已開啟".encode())
            elif command == "off":
                client_socket.send("LED 已關閉".encode())
            else:
                client_socket.send(f"未知指令: {command}".encode())
    except KeyboardInterrupt:
        break

client_socket.close()
server_socket.close()
GPIO.cleanup()