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

def configQuestion(question):
    n1 = Fore.LIGHTMAGENTA_EX + Style.BRIGHT + '? '
    n2 = reset + Style.BRIGHT + question
    answer = input(f'{n1} {n2} ')
    return answer

answer = configQuestion('Wie heißt du?')

# Quiz Logic

score = 0
max_score = len(questions)
for q in questions:
    print(f'[{q['q_id']}] {q['content']['question']}')
