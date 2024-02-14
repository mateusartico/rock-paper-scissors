import random
import os
import sys

def computer_time(number_player):
    number = random.randint(1, 3)
    
    print()
    print_symbols(number_player)
    print('\033[35m VS \033[m', end='')
    print_symbols(number)
    print()

    if number == number_player:
        print('\033[33mTIE\033[m')
    else:
        if number == 1:
            if number_player == 2:
                print('\033[32mWIN\033[m')
            else:
                print('\033[31mLOSE\033[m')

        if number == 2:
            if number_player == 1:
                print('\033[31mLOSE\033[m')
            else:
                print('\033[32mWIN\033[m')

        if number == 3:
            if number_player == 1:
                print('\033[32mWIN\033[m')
            else:
                print('\033[31mLOSE\033[m')

    press_enter()

def print_symbols(number):
    if number == 1:
        print('O', end='')
    elif number == 2:
        print('/', end='')
    else:
        print('>8', end='')

def print_title():
    os.system('cls')
    for i in range(2):
        print('\033[1m-\033[m' * 88)
    title = '''
                 _                                             _                        
                | |                                           (_)                       
  _ __ ___   ___| | __  _ __   __ _ _ __   ___ _ __   ___  ___ _ ___ ___  ___  _ __ ___ 
 | '__/ _ \ / __| |/ / | '_ \ / _` | '_ \ / _ \ '__| / __|/ __| / __/ __|/ _ \| '__/ __|
 | | | (_) | (__|   <  | |_) | (_| | |_) |  __/ |    \__ \ (__| \__ \__ \ (_) | |  \__ \ 
 |_|  \___/ \___|_|\_\ | .__/ \__,_| .__/ \___|_|    |___/\___|_|___/___/\___/|_|  |___/
                       | |         | |                                                  
                       |_|         |_|                                                  
    '''
    print(f'\033[33m{title}\033[m')
    print(f'\n\033[1m{"By Mateus Artico".rjust(88, " ")}\033[m')
    print(f'\033[1m{"https://github.com/mateusartico".rjust(88, " ")}\033[m')
    for i in range(2):
        print('\033[1m-\033[m' * 88)
    print()

def print_menu():
    options = ['rock O', 'paper /', 'scissors >8']
    c = 1
    for i in options:
        print(f'{c}. {i}')
        c += 1

def press_enter():
    try:
        input("\n[!] Press Enter to restart... ")
    except(KeyboardInterrupt):
        print_title()
        print('\033[33m[!] Bye\033[m')
        sys.exit()

def input_int():
    while True:
        try:
            number = int(input("> "))
        except(ValueError, TypeError):
            print_title()
            print_menu()
            print('\033[31m[!] This is not an option\033[m')
            continue
        except(KeyboardInterrupt):
            print_title()
            print('\033[33m[!] Bye\033[m')
            sys.exit()
        else:
            print_title()
            print_menu()
            if not number in [1, 2, 3]:
                print('\033[31m[!] This is not an option\033[m')
                continue
            else:
                print(f'> {number}')
                return number

def rock_paper_scissors():
    while True:
        print_title()
        print_menu()
        number = input_int()
        computer_time(number)


if __name__ == '__main__':
    rock_paper_scissors()