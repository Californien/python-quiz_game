# config

import time
import colorama
import keyboard
from colorama import Fore, Style
from gameLogic import runQuiz, activateBuzzer
colorama.init()

# Title

c_b = Fore.CYAN + Style.BRIGHT
c = Fore.CYAN
lc_b = Fore.LIGHTCYAN_EX + Style.BRIGHT
lc = Fore.LIGHTCYAN_EX
reset = Style.RESET_ALL

space = '                   '
print(lc_b + space + '╭──────────────────────────────────────────────────────────────╮')
print(space + '│                        < WILLKOMMEN >                        │')
print(space + '│                           Quizgame                           │')
print(space + '╰──────────────────────────────────────────────────────────────╯' + reset)

print(c_b + space + '               Willkommen beim besten Quiz-Spiel!' + reset)
print('\n')

# Game configuration Questions

gameConfig = {}

def configQuestion(question, ready):
    if ready == 'ready':
        n1 = Fore.LIGHTMAGENTA_EX + Style.BRIGHT + '? '
    else:
        n1 = Fore.LIGHTRED_EX + Style.BRIGHT + '? '
    n2 = reset + Style.BRIGHT + question
    answer = input(f'{n1} {n2} ' + Style.NORMAL + Fore.CYAN)
    return answer

def runSingleplayerCfg():
    print(reset)
    time.sleep(0.5)
    print(Fore.LIGHTCYAN_EX + Style.BRIGHT + '<---  SINGLEPLAYER MODUS  --->\n\n')
    time.sleep(0.5)
    name = configQuestion('Wie heißt du?', 0)
    time.sleep(0.5)
    print(f'{Fore.LIGHTRED_EX + Style.BRIGHT + '? '} {reset + Style.BRIGHT + 'Wie viele Fragen möchtest du beantworten?'}')
    print(f'{Fore.LIGHTBLUE_EX + Style.NORMAL + "Drücke '1' für 12 Fragen, '2' für 24 Fragen, '3' für 40 Fragen."}')
    qCount = 0
    while True:
        if keyboard.is_pressed('1'):
            qCount = 12
            break
        elif keyboard.is_pressed('2'):
            qCount = 24
            break
        elif keyboard.is_pressed('3'):
            qCount = 40
            break
    print(Fore.LIGHTGREEN_EX + Style.BRIGHT + '✓ ' + Fore.LIGHTWHITE_EX + Style.NORMAL + f'{qCount} Fragen.')
    time.sleep(0.5)
    print(Fore.LIGHTWHITE_EX + Style.NORMAL + f'\n\nOkay {name}, das Quiz mit {str(qCount)} Fragen geht gleich los. Sobald du die Antwort weißt, drücke den Buzzer (Taste ' + Style.BRIGHT + 'B' + Style.NORMAL + '), um deine Antwort abzugeben.')
    time.sleep(6)
    print(Fore.LIGHTGREEN_EX + Style.NORMAL + '\nAlles verstanden?')
    time.sleep(3)
    print('Sobald du bereit bist, ...')
    time.sleep(2.5)
    gameConfig = {
        'players': [
            {
                'id': 1,
                'name': name,
                'bind': 'b'
            }
        ],
        'qCount': qCount
    }
    activateBuzzer(gameConfig, runQuiz, gameConfig)

def runMultiplayerCfg(count):
    print(reset)
    print(Fore.LIGHTCYAN_EX + Style.BRIGHT + f'<---  MULTIPLAYER MODUS ({str(count)} P.)  --->\n\n')
    time.sleep(0.5)
    print(f'{Fore.LIGHTRED_EX + Style.BRIGHT + '? '} {reset + Style.BRIGHT + 'Wie viele Fragen möchtet ihr beantworten?'}')
    print(f'{Fore.LIGHTBLUE_EX + Style.NORMAL + "\nDrücke '1' für 12 Fragen, '2' für 24 Fragen, '3' für 40 Fragen."}\n')
    qCount = 0
    while True:
        if keyboard.is_pressed('1'):
            qCount = 12
            break
        elif keyboard.is_pressed('2'):
            qCount = 24
            break
        elif keyboard.is_pressed('3'):
            qCount = 40
            break
    print(Fore.LIGHTGREEN_EX + Style.BRIGHT + '✓ ' + Fore.LIGHTWHITE_EX + Style.NORMAL + f'{qCount} Fragen.')
    time.sleep(0.25)
    binds = ['q', 'x', 'n', 'p']
    names = []
    for i in range(1, (count + 1)):
        name = configQuestion(f'Spieler {i}, wie heißt du?', 0)
        names.append(name)
        print(Fore.LIGHTGREEN_EX + Style.BRIGHT + '✓ ' + Fore.LIGHTWHITE_EX + Style.NORMAL + f'Okay {name}, du bist Spieler {i} und erhälst den Buzzer {binds[i - 1].upper()}')
        time.sleep(2)
    print(Fore.LIGHTWHITE_EX + Style.NORMAL + f'\n\nOkay, das Quiz mit {str(qCount)} Fragen geht gleich los. Sobald einer von euch die Antwort weißt, drücke dieser Spieler den ihm zugewiesenem Buzzer, um deine Antwort abzugeben.')
    time.sleep(6)
    print(Fore.LIGHTGREEN_EX + Style.NORMAL + '\nAlles verstanden?')
    time.sleep(3)
    print('Sobald ihr bereit seit, ...')
    time.sleep(2.5)
    gameConfig = {
        'players': [],
        'qCount': qCount
    }
    idTmp = 1
    for name in names:
        gameConfig['players'].append({
            'id': idTmp,
            'name': name,
            'bind': binds[idTmp - 1]
        })
        idTmp += 1
    activateBuzzer(gameConfig, runQuiz, gameConfig)

def startGameQuestions():
    wrong_answers = 0
    while True:
        try:
            players = int(configQuestion('Wie viele Spieler spielen mit? (1-4)', 0))
            if wrong_answers > 0:
                print(Fore.LIGHTGREEN_EX + 'Geht doch!')
                time.sleep(0.5)
            if players > 1 and players <= 4:
                runMultiplayerCfg(players)
                break
            elif players == 1:
                runSingleplayerCfg()
                break
            elif players != 1 and players != 2 and players != 3 and players != 4:
                print(Fore.YELLOW + 'Warte...')
                time.sleep(1)
                print(Fore.RED + 'Nope das geht nicht.')
                time.sleep(0.5)
                print(Fore.RED + Style.BRIGHT + 'Spiel vorbei.')
                break
        except ValueError:
            if wrong_answers == 0:
                print(Fore.LIGHTRED_EX + 'Hey! Gib mal jetzt richtige Antworten ein!')
                wrong_answers = wrong_answers + 1
            elif wrong_answers == 1:
                print(Fore.RED + 'Wer sich vor dem Quiz schon so anstellt, kann im Quiz selbst nicht weit kommen...')
                wrong_answers = wrong_answers + 1
            elif wrong_answers > 1:
                print(Fore.RED + 'Ne komm, du meinst es nicht ernst...')
                time.sleep(0.5)
                print(Fore.RED + Style.BRIGHT + 'Spiel vorbei.')
                break

wrong_answers = 0
ready = configQuestion('Möchtest Du anfangen? (Y / N):', 'ready')
while ready != 0:
    if ready == 'Y' or ready == 'y':
        ready = 0
        startGameQuestions()
        break
    elif ready != 'N' and ready != 'n':
        print(Fore.YELLOW + 'Wie kann man vor dem Quiz Fragen bereits falsch beantworten??')
        if wrong_answers > 0:
            print(Fore.RED + 'Ne komm, du meinst es nicht ernst...')
            time.sleep(0.5)
            print(Fore.RED + Style.BRIGHT + 'Spiel vorbei.')
            break
        wrong_answers = wrong_answers + 1
        ready = configQuestion('Möchtest Du anfangen? (Y / N):', 'ready')
    else:
        print(Fore.RED + Style.BRIGHT + 'Spiel vorbei.')
        break
