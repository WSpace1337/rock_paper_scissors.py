from random import randint
from colorama import init, Fore, Back, Style
from termcolor import colored
import os
import time
#гавно код by ykraincki :3
init(autoreset=True)

clear = lambda: os.system('cls')
choice = ['камень', 'ножницы', 'бумага']

def main():
    computer = choice[randint(0,2)]

    print(Fore.RED + 'Добро пожаловать в игру Камень, Ножницы,Бумага!')
    player = input(Fore.RED + 'Напишите свой предмет:').lower()

    if player not in choice:
        print('Нету такого знака!')
        player = input(Fore.RED + 'Повторите ввод:').lower()
    else:
        pass
    print(Fore.RED + 'Бот выбрал: ' + computer)


    if player == computer:
        print(Fore.RED + 'Ничья!')
    elif player == 'камень' and computer == 'бумага':
        print(Fore.RED + 'Вы проиграли!')
    elif player == 'бумага' and computer == 'камень':
        print(Fore.RED + 'Вы выиграли!')
    elif player == 'ножницы' and computer == 'камень':
        print(Fore.RED + 'Вы проиграли!')
    elif player == 'камень' and computer == 'ножницы':
        print(Fore.RED + 'Вы выиграли!')
    elif player == 'бумага' and computer == 'ножницы':
        print(Fore.RED + 'Вы проиграли!')
    elif player == 'ножницы' and computer == 'бумага':
        print(Fore.RED + 'Вы выиграли!')
    elif player == 'камень' and computer == 'ножницы':
        print(Fore.RED + 'Вы выиграли')
    elif player == 'ножницы' and computer == 'камень':
        print(Fore.RED + 'Вы проиграли!')
    time.sleep(1)
    clear()
    main()
main()
