import time
import json
import keyboard
import random
import colorama
from colorama import Fore, Style

colorama.init()
with open('./assets/questions.json', 'r', encoding='utf-8') as file:
    questions = json.load(file)

def activateBuzzer(cfg, function, *args):
    print(f'\n\n{Fore.LIGHTWHITE_EX + Style.BRIGHT + '>>>>    '}{Fore.LIGHTCYAN_EX + Style.BRIGHT + 'BUZZER'}{Fore.LIGHTWHITE_EX + Style.BRIGHT + '    <<<<'}')
    players = cfg['players']
    chars = 30
    print('\n')
    for player in players:
        id_ = str(player['id'])
        name = player['name']
        nameL = len(name)
        bind = player['bind']
        print(f'{Fore.LIGHTWHITE_EX + Style.NORMAL + f'[{id_}]'} {Style.BRIGHT + name}' + ' ' * (chars - nameL - 4) + Fore.LIGHTMAGENTA_EX + Style.BRIGHT + f'[{bind.upper()}]   <')

    def visualizeFirstBind(bind):
        list = cfg['players']
        for _ in range(len(list)):
            print('\033[F\033[K', end='')
        for player in list:
            id_ = player['id']
            name = player['name']
            bind = player['bind']
            if player['bind'] != buzzerBind:
                print(f'{Fore.LIGHTWHITE_EX + Style.NORMAL + f'[{id_}]'} {Style.BRIGHT + name}' + ' ' * (chars - len(name) - 4) + Fore.LIGHTMAGENTA_EX + Style.BRIGHT + f'[{bind.upper()}]   <')
            else:
                print(f'{Fore.LIGHTWHITE_EX + Style.NORMAL + f'[{id_}]'} {Style.BRIGHT + name}' + ' ' * (chars - len(name) - 4) + Fore.LIGHTCYAN_EX + Style.BRIGHT + f'[{bind.upper()}] <')

    shouldCheckBind = True
    while shouldCheckBind:
        for player in players:
            if keyboard.is_pressed(player['bind']):
                buzzerBind = player['bind']
                shouldCheckBind = False
                visualizeFirstBind(buzzerBind)
                time.sleep(1)
                responses = ['war am schnellsten!', 'hat den Buzzer gedrückt!', 'hat den Butter am schnellsten gedrückt!']
                random.shuffle(responses)
                print(Fore.LIGHTWHITE_EX + Style.BRIGHT + f'\n\n{player['name']} [{player['id']}] {responses[0]}')
                if function:
                    function(*args)
                return player['bind']


def runQuiz(arg1):
    print(Style.RESET_ALL + '\n\n')
    print(Fore.CYAN + "Okay, der Einstiegstest wurde bestanden, jetzt geht's an's Quiz!\n\n")
    print(f'{arg1}')

    # Shuffled questions
    
    cfg = arg1
    qCount: float = cfg['qCount']
    qCountPerCategory = qCount / 4
    qToRemovePerCategory: float = 10 - qCountPerCategory
    for category in questions:
        random.shuffle(category)
        for _ in range(qToRemovePerCategory):
            category.pop()

    print(questions)

    # Score object

    scores = {}
    for player in cfg['players']:
        scores[player['name']] = {
            'score': 0
        }
    
    # Question

    def question(object):
        print(Style.RESET_ALL + '\n\n')
        print()

    for el in questions:
        question(el)
