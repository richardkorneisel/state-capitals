from capitals import states
import random

def play_game():
  random.shuffle(states)
  score = 0
  counter = 0

  for state in states:
    counter += 1
    print('What is the capital of: ' + state['name'])
    
    user_answer = input().lower()

    if user_answer == state['capital'].lower():
      score += 1
      print(f"Correct! Your score is {score}/{counter} or {int(score/counter * 100)}%") 
    else:
      print(f"You missed that one, it's {state['capital']}. Your score is now {int(score/counter * 100)}%")

    if counter == 3:
      print('Would you like to play again y or n?')
      play_again = input().lower()
      
      if play_again == 'y':
        play_game()
      else:
        print('Goodbye!')
        quit()

print('Hello, welcome to the state capitals game')
play_game()
