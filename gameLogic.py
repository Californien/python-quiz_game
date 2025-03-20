# Config

import time
import json
import keyboard
import random
import colorama
from colorama import Fore, Style

colors = {
    'GEOGRAPHIE': Fore.LIGHTGREEN_EX,
    'NATURWISSENSCHAFTEN': Fore.LIGHTCYAN_EX,
    'KUNST UND KULTUR': Fore.LIGHTMAGENTA_EX,
    'TECHNOLOGIE UND INNOVATION': Fore.LIGHTBLUE_EX
}

colorama.init()
with open('./assets/questions.json', 'r', encoding='utf-8') as file:
    questions = json.load(file)

# Buzzer function

def activateBuzzer(cfg, function, *args):
    print(
        f'\n\n{Fore.LIGHTWHITE_EX + Style.BRIGHT + '>>>>    '}{Fore.LIGHTCYAN_EX + Style.BRIGHT + 'BUZZER'}{Fore.LIGHTWHITE_EX + Style.BRIGHT + '    <<<<'}')
    players = cfg['players']
    chars = 30
    print('\n')
    for player in players:
        id_ = str(player['id'])
        name = player['name']
        nameL = len(name)
        bind = player['bind']
        print(f'{Fore.LIGHTWHITE_EX + Style.NORMAL + f'[{id_}]'} {Style.BRIGHT + name}' + ' ' * (
                    chars - nameL - 4) + Fore.LIGHTMAGENTA_EX + Style.BRIGHT + f'[{bind.upper()}]   <')

    def visualizeFirstBind(bind):
        list = cfg['players']
        for _ in range(len(list)):
            print('\033[F\033[K', end='')
        for player in list:
            id_ = player['id']
            name = player['name']
            bind = player['bind']
            if player['bind'] != buzzerBind:
                print(f'{Fore.LIGHTWHITE_EX + Style.NORMAL + f'[{id_}]'} {Style.BRIGHT + name}' + ' ' * (
                            chars - len(name) - 4) + Fore.LIGHTMAGENTA_EX + Style.BRIGHT + f'[{bind.upper()}]   <')
            else:
                print(f'{Fore.LIGHTWHITE_EX + Style.NORMAL + f'[{id_}]'} {Style.BRIGHT + name}' + ' ' * (
                            chars - len(name) - 4) + Fore.LIGHTCYAN_EX + Style.BRIGHT + f'[{bind.upper()}] <')

    shouldCheckBind = True
    while shouldCheckBind:
        for player in players:
            if keyboard.is_pressed(player['bind']):
                buzzerBind = player['bind']
                shouldCheckBind = False
                visualizeFirstBind(buzzerBind)
                time.sleep(1)
                responses = ['war am schnellsten!', 'hat den Buzzer gedrückt!',
                             'hat den Buzzer am schnellsten gedrückt!']
                random.shuffle(responses)
                print(Fore.LIGHTWHITE_EX + Style.BRIGHT + f'\n\n{player['name']} [{player['id']}] {responses[0]}')
                if function:
                    function(*args)
                return player

# Quiz logic

def runQuiz(arg1):
    print(Style.RESET_ALL)
    print(Fore.CYAN + "Okay, der Einstiegsbuzzertest wurde bestanden, jetzt geht's an's Quiz!\n")
    time.sleep(1)
    print(
        'Bereit? Dann drücke ' + Style.BRIGHT + 'S' + Style.NORMAL + ' zum starten und ' + Style.BRIGHT + 'A' + Style.NORMAL + ' zum abbrechen.\n')

    while True:
        if keyboard.is_pressed('s'):
            print(Fore.GREEN + Style.BRIGHT + "Los geht's!")
            break
        elif keyboard.is_pressed('a'):
            print(Fore.RED + Style.BRIGHT + 'Quiz abgebrochen.')
            return

    # Shuffled questions

    cfg = arg1
    qCount = cfg['qCount']                              # z.B.:   24  |  24 Fragen werden gestellt <-------------
    qCountPerCategory = qCount / 4                      # 24 / 4 = 6 Fragen pro Kategorie                       |
    qToRemovePerCategory = 10 - qCountPerCategory       # 10 - 6 = 4 Fragen werden entfernt                     |
                                                        #         ==> Somit bleiben 6 Fragen pro Kategorie      |
                                                        #             > 6 Fragen * 4 Kategorien = 24 Fragen  <---
    for category in questions:
        random.shuffle(category)
        for _ in range(int(qToRemovePerCategory)):
            category.pop()

    # Score object

    scores = {}
    for player in cfg['players']:
        scores[player['name']] = 0

    # Question

    def askQuestion(questionObject: object, num: int):
        category = questionObject['content']['category'].upper()
        time.sleep(1)
        question = questionObject['content']['question']
        qNum = str(num)
        questionLength = len(question)
        qId = Fore.LIGHTWHITE_EX + Style.BRIGHT + f'[{qNum}]'
        print(f'\n{qId}', end='', flush=True)
        time.sleep(0.5)
        for i in range(questionLength):
            qAnimationLog = question[:i + 1]
            print(f'{qId} {qAnimationLog}', end='\r', flush=True)
            time.sleep(0.05)
        print('\n')
        qType = questionObject['q_type']

        if qType == 'multiple_choice':
            startLine = Fore.LIGHTWHITE_EX + Style.BRIGHT + '? >> '
            choices = questionObject['content']['choices']
            for choice in choices:
                print(f'{startLine}{colors[category] + Style.NORMAL + choice}')
                time.sleep(0.3)

        player = activateBuzzer(cfg, None)
        while not player:
            if player:
                break
        time.sleep(0.35)

        if qType == 'input':
            answers_raw = questionObject['content']['answers']
            answers = []
            for el in answers_raw:
                answers.append(el.lower())
            answer = input(
                f'{colors[category] + '?'} {Fore.LIGHTWHITE_EX + Style.NORMAL + 'Wie lautet deine Antwort? '}' + Fore.LIGHTCYAN_EX + Style.NORMAL)
            if answer.lower() in answers:
                print(Fore.GREEN + Style.BRIGHT + 'Richtig!')
                scores[player['name']] += 1
            else:
                print(Fore.RED + Style.BRIGHT + 'Falsch!')
                print(Fore.LIGHTWHITE_EX + Style.NORMAL + 'Richtige Antwort: ' + colors[
                    category] + Style.BRIGHT + answers_raw[0])

        elif qType == 'multiple_choice':
            print(
                f'{Fore.LIGHTWHITE_EX + Style.NORMAL + 'Um deine Antwortmöglichkeit auszuwählen, drücke die Zahl 1, 2, 3 oder 4.'}')
            correct = questionObject['content']['correct']
            while True:
                if keyboard.is_pressed('1'):
                    answer = choices[0]
                    break
                elif keyboard.is_pressed('2'):
                    answer = choices[1]
                    break
                elif keyboard.is_pressed('3'):
                    answer = choices[2]
                    break
                elif keyboard.is_pressed('4'):
                    answer = choices[3]
                    break
            if answer == correct:
                print(Fore.GREEN + Style.BRIGHT + 'Richtig!')
                scores[player['name']] += 1
            else:
                print(Fore.RED + Style.BRIGHT + 'Falsch!')
                print(Fore.LIGHTWHITE_EX + Style.NORMAL + 'Richtige Antwort: ' + colors[
                    category] + Style.BRIGHT + correct)

    def defineCategory(category: str):
        upperCategory = category.upper()
        print(
            f'\n\n{colors[upperCategory] + Style.BRIGHT + '>>> ───'} {Fore.LIGHTWHITE_EX + Style.BRIGHT + upperCategory} {colors[upperCategory] + Style.BRIGHT + '─── <<<'}\n')

    time.sleep(1)

    for category in questions:
        qNum = 1
        currentCategory = category[0]['content']['category']
        defineCategory(currentCategory)
        for question in category:
            questionObject = question
            askQuestion(questionObject, qNum)
            qNum += 1

    print(Fore.LIGHTWHITE_EX + Style.BRIGHT + '\n\nSpiel beendet! Alle Fragen wurde gestellt.')
    time.sleep(3)
    print(f'Bereit für die Punkte? Maximal {cfg['qCount']} Punkte konnten pro Spieler vergeben werden.\n')
    time.sleep(3)
    for player in scores:
        entry = Fore.LIGHTYELLOW_EX + Style.BRIGHT + ' >>> '
        chars = 42
        print(
            f'{entry}{Fore.YELLOW + Style.BRIGHT + player}{' ' * (chars - len(player) - 5)}{Fore.LIGHTGREEN_EX + Style.BRIGHT + f'{scores[player]} P.'}')
        time.sleep(1)
    if len(cfg['players']) == 1:
        print(Fore.LIGHTGREEN_EX + Style.BRIGHT + 'Herzlichen Glückwunsch! Du hast das Quiz erfolgreich beendet.')
    else:
        max_points = max(scores.values())
        winners = [name for name, punkte in scores.items() if punkte == max_points]
        if len(winners) == 1:
            print(
                Fore.LIGHTBLUE_EX + Style.BRIGHT + f'\nDamit hat {winners[0]} das Quiz gewonnen! Herzlichen Glückwunsch!')
            time.sleep(2)
        else:
            print(Fore.LIGHTBLUE_EX + Style.BRIGHT + '\nWir haben ein Unentschieden! Die Gewinner sind:')
            for winner in winners:
                print(Fore.LIGHTWHITE_EX + Style.BRIGHT + f'>> {winner}')
            print(Fore.LIGHTBLUE_EX + Style.BRIGHT + '\nHerzlichen Glückwunsch!')
            time.sleep(2)
