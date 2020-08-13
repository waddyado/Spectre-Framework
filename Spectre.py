import os
import sys
import colorama
import time
#i dont write comments unless i have to sorry :(
sys.path.append('/generate/generate.py')
sys.path.append('/listener/listener.py')
sys.path.append('/scanner/scanner.py')
def initGenerate():
    from generate.generate import main, generate
    main()
def initListener():
    sys.path.append('/listener/listener.py')
    from listener.listener import main, lists, exploit, shell, connect
    main()
def initScanner():
    from scanner.scanner import main
    main()

def main():
    print('   _____                     __                 ______                                                     __  ')
    print('  / ___/ ____   ___   _____ / /_ _____ ___     / ____/_____ ____ _ ____ ___   ___  _      __ ____   _____ / /__')
    print('  \__ \ / __ \ / _ \ / ___// __// ___// _ \   / /_   / ___// __ `// __ `__ \ / _ \| | /| / // __ \ / ___// //_/')
    print(' ___/ // /_/ //  __// /__ / /_ / /   /  __/  / __/  / /   / /_/ // / / / / //  __/| |/ |/ // /_/ // /   / ,<   ')
    print('/____// .___/ \___/ \___/ \__//_/    \___/  /_/    /_/    \__,_//_/ /_/ /_/ \___/ |__/|__/ \____//_/   /_/|_|  ')
    print('     /_/                                                                                                       ')
    print('                           The All in One Pentesting Framework                                                 ')
    print('                                                                                                               ')
    print('type "help" for a list of commands')

    if len(sys.argv) > 1:
        args = sys.argv[1:]
        if "help" in args:
            print('Type "generate" to generate customized payloads')
            print('Type "listener" to select from a variety of listeners')
            print('Type "scanner" to select from a variety of vulnerability scanners')
            print('Type "exit" to exit (never coulda guessed that one)')
        elif "listener" in args:
            initListener()
        elif 'generate' in args:
            initGenerate()
        elif 'scanner' in args:
            initScanner()
            
    inp = input(':>')
    if inp == 'help':
        print('Type "generate" to generate customized payloads')
        print('Type "listener" to select from a variety of listeners')
        print('Type "scanner" to select from a variety of vulnerability scanners')
        print('Type "exit" to exit (never coulda guessed that one)')
        print('Type "cls" to clear screen')
        print('Press enter to continue...')
        helpinp = input('')
        os.system('cls')
        main()
        
    
            
    if inp == 'generate':
        initGenerate()
    elif inp == 'listener':
        initListener()
    elif inp == 'scanner':
        initScanner()
    elif inp == 'exit':
        print('bye bye')
        time.sleep(1)
        exit()
    elif inp == 'cls':
        os.system('cls')
        main()
    else:
        print('unrecognized command')
        time.sleep(1)
        os.system('cls')
        main()

if __name__=='__main__':
    main()
