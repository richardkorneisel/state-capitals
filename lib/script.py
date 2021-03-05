from capitals import states
import random

def name_capital_game():
    random.shuffle(states)
    print(states[0]['name'])
    print(states[0]['capital'])

name_capital_game()

#for i in states:
#print(states)