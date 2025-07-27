
import random
import sys
import logging
logging.basicConfig(level=logging.DEBUG) #to see following lines with logging.debug change to: logging.basicConfig(level=logging.DEBUG), to remove logs set to: logging.basicConfig(level=logging.WARNING)

deck_of_cards=[11,2,3,4,5,6,7,8,9,10,10,10,10,11,2,3,4,5,6,7,8,9,10,10,10,10,11,2,3,4,5,6,7,8,9,10,10,10,10,11,2,3,4,5,6,7,8,9,10,10,10,10 ]

def welcome_validaton_function(users_input):
    """function dedicated for the validation of the first welcome statement
    in else, not using reocurrence , but a normal input ( more efficient for memory, simple
        to understand and use, easier to build on the top of the below in the future"""

    while True:
        users_decision_formatted=users_input.strip().lower()
        if users_decision_formatted =='y':
            return users_decision_formatted
        if  users_decision_formatted=='n':
            return users_decision_formatted 
        else:
            print('Insert a valid entry')
            users_input = input("Enter only 'y' or 'n': ")





def question_validaton_function(users_input):
    """function dedicated for the validation of the next question to the user, if thee continue 'y' to play or not 'n'""" 
    while True:
        users_decision_formatted=input(users_input).strip().lower()
        if users_decision_formatted in ('y','n'):
            return users_decision_formatted
        print('Insert a valid entry')

def card_lottery():
    """function used in case we need to choose a card from the deck for the dealer or the player.It also is removing the chosen card from the deck / pool of cards"""
    choose_random_card=random.choice(deck_of_cards)
    deck_of_cards.remove(choose_random_card)
    return choose_random_card

def first_two_players_card(welcome_statement):
    players_total_score=0
    players_deck_of_cards=[]
    if welcome_statement=='y': 
        for _ in range (2):   # ciekawa iteracja przez petle, nie podajesz 'i' ale dajesz tylko '_'
            choose_random_card =card_lottery()
            players_deck_of_cards.append(choose_random_card)
        for card_score in players_deck_of_cards:
            players_total_score+=card_score
    logging.debug('Obecna talia kart to %s,\n liczba kart to %d',deck_of_cards,len(deck_of_cards))      
    print(f'Your cards : {players_deck_of_cards}, current score {players_total_score}\n')
    return players_total_score,players_deck_of_cards



def first_two_dealers_card(welcome_statement):
    dealers_total_score=0
    dealers_deck_of_cards=[]
    if welcome_statement=='y':
        for _ in range (2):   # ciekawa iteracja przez petle, nie podajesz 'i' ale dajesz tylko '_'
            choose_random_card =card_lottery()
            dealers_deck_of_cards.append(choose_random_card)         
        for card_score in dealers_deck_of_cards:
            dealers_total_score+=card_score
        logging.debug('Computers current deck of cards: %s',dealers_deck_of_cards)  
        print(f'Computers first card: {dealers_deck_of_cards[0]}') 
        logging.debug(' Computers current score %d\n',dealers_total_score)

        return  dealers_total_score, dealers_deck_of_cards
  
# dealers_total_score,dealers_deck_of_cards=first_two_dealers_card(deck_of_cards,welcome_statement)


def round_comparison(dealers_total_score,players_total_score,players_deck_of_cards,dealers_deck_of_cards):
    print(f'Your final hand: {players_deck_of_cards}, final score:{players_total_score}')
    print(f'Computers finals hand: {dealers_deck_of_cards}, final score: {dealers_total_score}')
          
    if players_total_score ==21 and dealers_total_score != 21  : # check for the first round, if maybe the player did won
        return 'Opponent went over.You win'
    
    elif players_total_score !=21 and dealers_total_score == 21  : # check for the first round, if maybe the player did won
        return 'You went over. You lose'
   
    elif players_total_score > 21 and dealers_total_score <players_total_score :
        return 'You went over. You lose'
          
    elif players_total_score <= 21 and players_total_score> dealers_total_score :
        return 'Opponent went over.You win'

    elif dealers_total_score > 21 and dealers_total_score > players_total_score :
        return 'Opponent went over.You win'

    elif dealers_total_score <= 21 and players_total_score < dealers_total_score :
        return 'You went over. You lose'
       
    elif dealers_total_score==players_total_score :
       return 'We have a DRAW'
  

def ace_treatment(total_score,ace_card):
    """ace conversion function, to be more in line with general black jack rules """ 
    if ace_card==11 and total_score > 21:
        logging.debug('Ace conversion from 11 to 1')
        total_new_score=total_score-ace_card+1
        return total_new_score
    elif ace_card==11 and total_score <= 21:
        logging.debug('Ace conversion from 1 to 11')
        total_new_score=total_score-ace_card+11
        return total_new_score
    else:
        return total_score

def next_card_round(players_deck_of_cards,players_total_score,dealers_total_score,dealers_deck_of_cards):
     
    while dealers_total_score <=21 and players_total_score <= 21:
        continue_game_question=question_validaton_function("Type 'y' to get another card, type 'n' to pass: ")       
        if continue_game_question=='y' and players_total_score <21 and dealers_total_score <21:
            choose_random_card=card_lottery()
            players_deck_of_cards.append(choose_random_card)
            players_total_score+=choose_random_card
            players_total_score=ace_treatment(players_total_score,choose_random_card)
            print(f'Your cards : {players_deck_of_cards}, current score {players_total_score}')
            print(f'Computers first card: {dealers_deck_of_cards[0]}') 
            logging.debug('Computers current deck of cards: %s',dealers_deck_of_cards)
            logging.debug(' Computers current score %d\n',dealers_total_score)
            if players_total_score > 21:
                result_comparison=round_comparison(dealers_total_score,players_total_score,players_deck_of_cards,dealers_deck_of_cards)
                print(result_comparison)            
                return

        elif continue_game_question=='n' and dealers_total_score >= 17 and players_total_score <= 21:
            print(f'Computers first card: {dealers_deck_of_cards[0]}') 
            logging.debug('Computers current deck of cards: %s',dealers_deck_of_cards)  
            logging.debug(' Computers current score %d\n',dealers_total_score)
            result_comparison=round_comparison(dealers_total_score,players_total_score,players_deck_of_cards,dealers_deck_of_cards)
            print(result_comparison)
            return
            
        while continue_game_question=='n' and dealers_total_score <17 :
                choose_random_card=card_lottery()
                dealers_deck_of_cards.append(choose_random_card)
                dealers_total_score+=choose_random_card
                dealers_total_score=ace_treatment(dealers_total_score,choose_random_card)
                print(f'Computers first card: {dealers_deck_of_cards[0]}') 
                logging.debug('Computers current deck of cards: %s',dealers_deck_of_cards)  
                logging.debug(' Computers current score %d\n',dealers_total_score)                
                if dealers_total_score >= 17:
                    #print(f'Computers first card: {dealers_deck_of_cards[0]},\ncurrent score {dealers_total_score} - this is for Dev purpose only!!\n')
                    result_comparison=round_comparison(dealers_total_score,players_total_score,players_deck_of_cards,dealers_deck_of_cards)
                    print(result_comparison)
                    return


def main():

    welcome_statement=welcome_validaton_function(input("Do you want to play a game of Blackjack ? Type 'y' or 'n' : "))
    print('\n')
    if welcome_statement=='n':
        print('End of Game')
        sys.exit()
    players_total_score,players_deck_of_cards=first_two_players_card(welcome_statement)
    dealers_total_score,dealers_deck_of_cards=first_two_dealers_card(welcome_statement)
    next_card_round(players_deck_of_cards,players_total_score,dealers_total_score,dealers_deck_of_cards)

if __name__=="__main__":
    main()