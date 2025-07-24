import random
import sys
deck_of_cards=[11,2,3,4,5,6,7,8,9,10,10,10,10,11,2,3,4,5,6,7,8,9,10,10,10,10,11,2,3,4,5,6,7,8,9,10,10,10,10,11,2,3,4,5,6,7,8,9,10,10,10,10 ]

def welcome_validaton_function(users_input):
    """function dedicated for the validation of the first welcome statement"""
    while True:
        users_decision_formatted=input(users_input).strip().lower()
        if users_decision_formatted =='y':
            return users_decision_formatted
        if  users_decision_formatted=='n':
            print('End of Game')
            sys.exit()
        else:
            print('Insert a valid entry')





def question_validaton_function(users_input):
    """function dedicated for the validation of the next question to the user, if thee continue 'y' to play or not 'n'""" 
    while True:
        users_decision_formatted=input(users_input).strip().lower()
        if users_decision_formatted in ('y','n'):
            return users_decision_formatted
        print('Insert a valid entry')

# welcome_statement=welcome_validaton_function("Do you want to play a game of Blackjack ? Type 'y' or 'n' :")



def card_lottery():
    """function used in case we need to choose a card from the deck for the dealer or the player.It also is removing the chosen card from the deck / pool of cards"""
    #deck_of_cards
    choose_random_card=random.choice(deck_of_cards)
    deck_of_cards.remove(choose_random_card)
    return choose_random_card,deck_of_cards


def first_two_players_card(deck_of_cards,welcome_statement):
    players_total_score=0
    players_deck_of_cards=[]
    if welcome_statement=='y': 
        for _ in range (2):   # ciekawa iteracja przez petle, nie podajesz 'i' ale dajesz tylko '_'     
            choose_random_card ,deck_of_cards=card_lottery()
            players_deck_of_cards.append(choose_random_card)
        for card_score in players_deck_of_cards:
            players_total_score+=card_score
    print(f'\nObecna talia kart to {deck_of_cards},\n liczba kart to {len(deck_of_cards)}\n')       
    print(f'Your cards : {players_deck_of_cards}, current score {players_total_score}')
    return players_total_score,players_deck_of_cards
     
# players_total_score,players_deck_of_cards=first_two_players_card(deck_of_cards,welcome_statement)



def first_two_dealers_card(deck_of_cards,welcome_statement):
    dealers_total_score=0
    dealers_deck_of_cards=[]
    if welcome_statement=='y':
        for _ in range (2):   # ciekawa iteracja przez petle, nie podajesz 'i' ale dajesz tylko '_'     
            choose_random_card ,deck_of_cards=card_lottery()
            dealers_deck_of_cards.append(choose_random_card)         
        for card_score in dealers_deck_of_cards:
            dealers_total_score+=card_score
        print(f'\nObecna talia kart to {deck_of_cards},\n liczba kart to {len(deck_of_cards)}\n')  
        print(f'Computers first card: {dealers_deck_of_cards[0]}, \n current score {dealers_total_score} - this is for Dev purpose only!!\n') 
        return  dealers_total_score,dealers_deck_of_cards
  
# dealers_total_score,dealers_deck_of_cards=first_two_dealers_card(deck_of_cards,welcome_statement)


def round_comparison(dealers_total_score,players_total_score,players_deck_of_cards,dealers_deck_of_cards):
    if players_total_score ==21 and dealers_total_score != 21  : # check for the first round, if maybe the player did won
        print(f'Your final hand: {players_deck_of_cards}, final score:{players_total_score}')
        print(f'Computers finals hand: {dealers_deck_of_cards}, final score: {dealers_total_score}')
        return print(f'Opponent went over.You win')
    
    elif players_total_score !=21 and dealers_total_score == 21  : # check for the first round, if maybe the player did won
        print(f'Your final hand: {players_deck_of_cards}, final score:{players_total_score}')
        print(f'Computers finals hand: {dealers_deck_of_cards}, final score: {dealers_total_score}')
        return print('You went over. You lose')   
   
    elif players_total_score > 21 and dealers_total_score <players_total_score :
        print(f'Your final hand: {players_deck_of_cards}, final score:{players_total_score}')
        print(f'Computers finals hand: {dealers_deck_of_cards}, final score: {dealers_total_score}')
        return print('You went over. You lose')

            
    elif players_total_score <= 21 and players_total_score> dealers_total_score :
        print(f'Your final hand: {players_deck_of_cards}, final score:{players_total_score}')
        print(f'Computers finals hand: {dealers_deck_of_cards}, final score: {dealers_total_score}')
        return print(f'Opponent went over. You win')

    elif dealers_total_score > 21 and dealers_total_score > players_total_score :
        print(f'Your final hand: {players_deck_of_cards}, final score:{players_total_score}')
        print(f'Computers finals hand: {dealers_deck_of_cards}, final score: {dealers_total_score}')
        return print('Opponent went over. You win')

    elif dealers_total_score <= 21 and players_total_score < dealers_total_score :
        print(f'Your final hand: {players_deck_of_cards}, final score:{players_total_score}')
        print(f'Computers finals hand: {dealers_deck_of_cards}, final score: {dealers_total_score}')
        return print('You went over. You lose')
       
    elif dealers_total_score==players_total_score :
        print(f'Your final hand: {players_deck_of_cards}, final score:{players_total_score}')
        print(f'Computers finals hand: {dealers_deck_of_cards}, final score: {dealers_total_score}')
        return print('We have a DRAW')

    


def next_card_round(players_deck_of_cards,players_total_score,dealers_total_score,dealers_deck_of_cards):
     
    while True and dealers_total_score <=21 and players_total_score <= 21:
        continue_game_question=question_validaton_function("Type 'y' to get another card, type 'n' to pass: ")       
        if continue_game_question=='y' and players_total_score <21 and dealers_total_score <21:
            #players_deck_of_cards
            choose_random_card=card_lottery()
            players_deck_of_cards.append(choose_random_card[0])
            players_total_score+=choose_random_card[0]
            print(f'Your cards : {players_deck_of_cards}, current score {players_total_score}')
            print(f'Computers first card: {dealers_deck_of_cards[0]},\ncurrent score {dealers_total_score} - this is for Dev purpose only!!\n')
            if players_total_score > 21:
                return round_comparison(dealers_total_score,players_total_score,players_deck_of_cards,dealers_deck_of_cards)   #// user needs to say 'n' so taht we can quit the game
            continue
        elif continue_game_question=='n' and dealers_total_score >= 17 and players_total_score <= 21:
            print(f'Computers first card: {dealers_deck_of_cards[0]},\ncurrent score {dealers_total_score} - this is for Dev purpose only!!\n')
            round_comparison(dealers_total_score,players_total_score,players_deck_of_cards,dealers_deck_of_cards)
            
        while True:
            if continue_game_question=='n' and dealers_total_score <17 :
                #dealers_deck_of_cards
                choose_random_card=card_lottery()
                dealers_deck_of_cards.append(choose_random_card[0])
                dealers_total_score+=choose_random_card[0]
                print(f'Computers first card: {dealers_deck_of_cards[0]},\ncurrent score {dealers_total_score} - this is for Dev purpose only!!\n')
                if dealers_total_score > 17:
                    #print(f'Computers first card: {dealers_deck_of_cards[0]},\ncurrent score {dealers_total_score} - this is for Dev purpose only!!\n')
                    return round_comparison(dealers_total_score,players_total_score,players_deck_of_cards,dealers_deck_of_cards)


# next_car_round(players_deck_of_cards,players_total_score,dealers_total_score,dealers_deck_of_cards)


def main():

    welcome_statement=welcome_validaton_function("Do you want to play a game of Blackjack ? Type 'y' or 'n' :")
    players_total_score,players_deck_of_cards=first_two_players_card(deck_of_cards,welcome_statement)
    dealers_total_score,dealers_deck_of_cards=first_two_dealers_card(deck_of_cards,welcome_statement)
    next_card_round(players_deck_of_cards,players_total_score,dealers_total_score,dealers_deck_of_cards)




if __name__=="__main__":
    main()