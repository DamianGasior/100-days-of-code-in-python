import random
import logging
logging.basicConfig(level=logging.WARNING) #to see following lines with logging.debug change to: logging.basicConfig(level=logging.DEBUG), to remove logs set to: logging.basicConfig(level=logging.WARNING)


def single_game():
    level=level_validation()
    comparison_result=game_play(level)  
    if comparison_result==1:
        print("Perfect match! You won the game!\n")
    elif comparison_result==0:
        print("You've run out of guesses. You lost.")


def level_validation(): 
        while True:
                level=input("Choose a difficulty level. Type 'easy' or 'hard' : ").lower().strip()
                if level in ('hard','easy'):
                    return level
                else:
                    print("You can type  'easy' or 'hard' only ")



def guess_validation():
     while True:
                try:
                    users_guess=int(input('Make a guess: '))
                    return users_guess
                except ValueError:
                    print('Please insert a number only')
           


def game_play(level):
    number_to_guess=random.randint(1,100)
    if logging.getLogger().isEnabledFor(logging.DEBUG):
        print()  
    logging.debug('\nNumber to guess is: %d\n', number_to_guess)
   
    if level=="hard":
        attempts=5
    elif level=="easy":
        attempts=10
    for attempt in range(attempts,0,-1):
        print(f'\nYou have {attempt} attempts remaining to guess the number')
        users_guess=guess_validation() 
        if users_guess>number_to_guess:
            comparison_result="Too high.\nGuess again"
            print(comparison_result)
            if attempt==1:
                comparison_result=0
                return comparison_result
        elif users_guess<number_to_guess:
            comparison_result="Too low.\nGuess again"
            print(comparison_result)
            if attempt==1:
                comparison_result=0
                return comparison_result
        elif users_guess==number_to_guess:
            comparison_result=1
            return comparison_result




def play_again(continue_game):
    while True:
        if continue_game in ('yes','no'):
            return  continue_game
        else:
            print('Invalid entry')
            continue_game=input("Type only  'yes' or 'no' : ").lower().strip()



def main():
    print("""Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100""")  
    
    single_game()

    continue_game=play_again(input("Do you want  play again ? Type 'yes' or 'no': ").lower().strip())
    
    while True:
        if continue_game=='yes':
            single_game()
            continue_game=play_again(input("Do you want  play again ? Type 'yes' or 'no': ").lower().strip())
        else:
            print("Thank you for playing 'Number Guessing Game'")
            break




if __name__ =="__main__":
    main()

