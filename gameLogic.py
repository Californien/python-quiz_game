import time
import keyboard
import random
from colorama import Fore, Style

def activateBuzzer(buttons, function, *args):
    print(f'\n{Fore.LIGHTWHITE_EX + Style.BRIGHT + '>>>>    '}{Fore.LIGHTCYAN_EX + Style.BRIGHT + 'BUZZER'}{Fore.LIGHTWHITE_EX + Style.BRIGHT + '    <<<<'}')
    i = 1
    for el in buttons:
        print(f'{Fore.LIGHTBLACK_EX + Style.NORMAL + f'Spieler {i}:'} {Fore.LIGHTMAGENTA_EX + Style.BRIGHT + f'[{el.upper()}] <'}')
        i += 1

def runQuiz(arg1):
    print('Quiz start...')
    print(f'{arg1}')
    # score = 0
    # max_score = len(questions)
    # for q in questions:
    #     print(f'[{q['q_id']}] {q['content']['question']}')
