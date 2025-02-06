import time
import keyboard

def activateBuzzer():
    print('buzzer')
    while True:
        if keyboard.is_pressed('b'):
            return 'b' 

def runQuiz():
    print('Quiz start...')
    # score = 0
    # max_score = len(questions)
    # for q in questions:
    #     print(f'[{q['q_id']}] {q['content']['question']}')
