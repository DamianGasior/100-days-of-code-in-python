# Welcome statement
# user random module
# import data from the higher_lower_data.py, list of ditionaries
# you will need to apply a radnom from the tems from the list of dicationaries for two variables :
# Compare A, provide all the data from the dictioary
# vs Compare B
# Userr will need to answer the below query, by Typiing A or B
# Answer form the query will drive a comparison between the  two "follower_count" ( A vs B) , higher score wins.
# the score which has won, is  moinvg to the first place, and then a second random choice is picked up from the list
# the list is not amended (  items are not removed from the list, the one which were arleady chosen)
# Validation of the who has more followers question. Apply lower() strip() and implement a validation that only 'A' or 'B' are required
# Each time the user will get the guess, and  one point to his score and present it in this way: 'You are right! Current score: XX'

import sys
import random
from higher_lower_data import data
import logging

logging.basicConfig(
    level=logging.DEBUG
)  # to see following lines with logging.debug change to: logging.basicConfig(level=logging.DEBUG), to remove logs set to: logging.basicConfig(level=logging.WARNING)



def data_decomposition(variable_data):
    return f"{variable_data['name']}, a {variable_data['description']}, from {variable_data['country']}"


def follower_count(variable_data):
    return variable_data["follower_count"]  # returns int """


def question_to_user():
    while True:
        users_decision = (
            input("\nWho has more followers? Type 'A' or 'B':  ").lower().strip()
        )
        if users_decision in ("a", "b"):
            users_guess = users_decision
            return users_guess
        else:
            print("'Type only 'A' or 'B'.")


# refactoring kodu ponizej
def followers_count_comparison(users_guess, follower_count_a, follower_count_b, current_score,play_again):

    if users_guess == "a":
        if follower_count_a > follower_count_b:
            current_score += 1
            return current_score,play_again
        else:
            print(
                f"Sorry, that's wrong. Final score: {current_score}"
            )  # problem with current score, if the suser wants to play again, we need to reset the current_score to '0'
            play_again = play_again_question_validation()
            return current_score,play_again
           

    elif users_guess == "b":
        if follower_count_a < follower_count_b:
            current_score += 1
            return current_score,play_again
        else:
            print(
                f"Sorry, that's wrong. Final score: {current_score}"
            )  # problem with current score, if the suser wants to play again, we need to reset the current_score to '0'
            play_again = play_again_question_validation()
            return current_score,play_again
           


def play_again_question_validation():

    while True:
        play_again = (
            input("Do you want to play again ? Type 'yes' or 'no' only: ")
            .lower()
            .strip()
        )
        if play_again in ("yes", "no"):
            return play_again
        else:
            print("Type 'yes' or 'no' only")




def first_round_only():
    play_again=None
    current_score = 0  # variable initialized, so that each time when the user decides to play again within the same session, the variable is reset to 0 in the first round
    custom_a_b = []
    custom_a_b = random.sample(data, k=2)
    custom_a = data_decomposition(custom_a_b[0])
    custom_b = data_decomposition(custom_a_b[1])
    print(f"Compare A: {custom_a}\n")
    follower_count_a = follower_count(custom_a_b[0])
    logging.debug("follower_count A: %d ", follower_count_a)
    print(f"Against B: {custom_b}\n")
    follower_count_b = follower_count(custom_a_b[1])
    logging.debug("follower_count B:  %d", follower_count_b)
    users_guess = question_to_user()
    current_score,play_again = followers_count_comparison(users_guess, follower_count_a, follower_count_b, current_score,play_again)
    print(f"\nYou are right! Current score: {current_score}\n")
    return follower_count_a, follower_count_b, custom_a, custom_b, current_score,play_again


def next_rounds(custom_a, custom_b, follower_count_a, follower_count_b, current_score,play_again):
    while True:
        custom_a = custom_b
        print(f"Compare A: {custom_a}")
        follower_count_a = follower_count_b  # follower_count(custom_a)
        logging.debug("follower_count A: %d ", follower_count_a)
        custom_b = random.choice(data)
        follower_count_b = follower_count(custom_b)
        logging.debug("follower_count B :  %d", follower_count_b)
        custom_b = data_decomposition(custom_b)
        print(f"\nAgainst B: {custom_b}")
        users_guess = question_to_user()
        current_score,play_again = followers_count_comparison(
            users_guess, follower_count_a, follower_count_b, current_score,play_again 
        )
        print(f"\nYou are right! Current score: {current_score}\n")
        if play_again!=None:
            return play_again


def main():
 
    print("\nWelcome to higher lower game!\n")

        
    follower_count_a, follower_count_b, custom_a, custom_b, current_score,play_again = first_round_only()
   
    while True:
        if play_again==None:
            play_again=next_rounds(custom_a, custom_b, follower_count_a, follower_count_b, current_score,play_again )
        
        elif play_again == "yes":
            print("\nWelcome to higher lower game!\n")
            follower_count_a, follower_count_b, custom_a, custom_b, current_score,play_again = first_round_only()
            if play_again==None:
                play_again=next_rounds(custom_a, custom_b, follower_count_a, follower_count_b, current_score,play_again )
                # play_again=next_rounds(custom_a, custom_b, follower_count_a, follower_count_b, current_score)
            elif play_again == "no":
                print("\nThank you for playing our higher_lower game!")
                sys.exit()


if __name__ == "__main__":
    main()
