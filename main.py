# Importing questions; config

from gameLogic import runQuiz
import json
import colorama
from colorama import Fore, Style
colorama.init()
with open('./assets/questions.json', 'r', encoding='utf-8') as file:
    questions = json.load(file)

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

def runSingleplayerCfg():
    print('Singleplayer cfg...')

def runMultiplayerCfg(count):
    print('Multiplayer cfg', count)

def startGameQuestions():
    wrong_answers = 0
    while True:
        try:
            players = int(configQuestion('Wie viele Spieler spielen mit? (1-4)', 0))
            if wrong_answers > 0:
                print(Fore.LIGHTGREEN_EX + 'Geht doch!')
            if players > 1:
                runMultiplayerCfg(players)
                break
            elif players == 1:
                runSingleplayerCfg()
                break
            elif players != 1 and players != 2 and players != 3 and players != 4:
                print(Fore.YELLOW + 'Warte...')
                print(Fore.RED + 'Nope das geht nicht.')
                print(Fore.RED + Style.BRIGHT + 'Spiel vorbei.')
                break
        except ValueError:
            if wrong_answers == 0:
                print(Fore.LIGHTRED_EX + 'Hey! Gib mal jetzt richtige Antworten ein!')
            elif wrong_answers == 1:
                print(Fore.RED + 'Wer sich vor dem Quiz schon so anstellt, kann im Quiz selbst nicht weit kommen...')
            elif wrong_answers > 1:
                print(Fore.RED + 'Ne komm, du meinst es nicht ernst...')
                print(Fore.RED + Style.BRIGHT + 'Spiel vorbei.')
                break

def configQuestion(question, ready):
    if ready == 'ready':
        n1 = Fore.LIGHTMAGENTA_EX + Style.BRIGHT + '? '
    else:
        n1 = Fore.LIGHTRED_EX + Style.BRIGHT + '? '
    n2 = reset + Style.BRIGHT + question
    answer = input(f'{n1} {n2} ' + Style.NORMAL + Fore.CYAN)
    return answer

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
            print(Fore.RED + Style.BRIGHT + 'Spiel vorbei.')
            break
        wrong_answers = wrong_answers + 1
        ready = configQuestion('Möchtest Du anfangen? (Y / N):', 'ready')
    else:
        print(Fore.RED + Style.BRIGHT + 'Spiel vorbei.')
        break


