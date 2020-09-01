from capitals import states
import random
random.shuffle(states)


def play_game():
    print("Welcome to the game!")

    correct = 0
    incorrect = 0
    total_states = 0
    for state in states:
        user_input = input(
            "What is the capital of {0}? ".format(state["name"]))
        if user_input == state["capital"]:
            correct += 1
            total_states = correct + incorrect
            print("Correct! correct: {0}, incorrect: {1}, Total Score: {2}".format(
                correct, incorrect, total_states))
        else:
            incorrect += 1
            total_states = correct + incorrect
            print("Wrong! correct: {0}, incorrect: {1}, Total Score: {2}".format(
                correct, incorrect, total_states))

    replay()


def replay():
    keep_playing = input("Keep playing? Y or N ")
    play_game() if keep_playing == "Y" else print("See ya!")


play_game()
