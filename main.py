# Importing questions; config

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

def startGameQuestions():
    players = configQuestion('Wie viele Spieler spielen mit?', 0)


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

# Quiz Logic

def runQuiz():
    print('Quiz start...')
    # score = 0
    # max_score = len(questions)
    # for q in questions:
    #     print(f'[{q['q_id']}] {q['content']['question']}')
