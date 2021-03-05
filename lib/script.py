from capitals import states
import random

def name_capital_game():
    play_game=input('Do you want to play the guess your capitals game? y or n')
    
    score_right=0
    score_wrong=0
    incorrect=0
    
    round = score_right+score_wrong
    
    if play_game=='y':
        print ('Type the state capital for the state displayed ')
        random.shuffle(states)
        
        print(states[0]['name'])
        answer=input()
        if answer==states[0]['capital']:
            print('Correct!! Great Job.')
            score_right = score_right+1
            print(score_right)
            states.pop(0)
        else:
            print('Sorry, wrong answer')
            score_wrong = score_wrong+1
            print(score_wrong)
            states.pop(0)
        
    else:
        print('Goodbye, maybe we can play again')
    
    print('round')
    

name_capital_game()

#for i in states:
#print(states)