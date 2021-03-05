from capitals import states
import random

def start_game():
    start_game=input('Welcome! Would you like to play our guess the state capital game y or n? ')
    if start_game=='y':
        #print('Type in the state capital for:')
        score_correct = 0
        score_incorrect = 0
        round=0
        random.shuffle(states)
        for i in range(3):
            if len(states)!=0:
                round=round+1
                print(f'Round {round}:')
                print('Type in the state capital for:')
                print(states[0]['name'])
                user_answer=input()
                if user_answer==states[0]['capital']:
                    print('You are correct!!!')
                    score_correct=score_correct+1
                    states.pop(0)
                else:
                    score_incorrect=score_incorrect+1
                    print('Sorry, wrong answer')
                    states.pop(0)
            print(f'Your correct answers total: {score_correct}')
            print(f'Your incorrect answers total: {score_incorrect}')
       
    else:
        print('Goodbye')
    
    play_again()

def play_again():
    play_again = input("Would you like to play again? y or n ")
    start_game() if play_again == "y" else print("Let's play again soon")

start_game()