import random
deck_of_cards=[11,2,3,4,5,6,7,8,9,10,10,10,10,11,2,3,4,5,6,7,8,9,10,10,10,10,11,2,3,4,5,6,7,8,9,10,10,10,10,11,2,3,4,5,6,7,8,9,10,10,10,10 ]
#updated_deck_of_cards=[]

def question_validaton_function(users_input): 
    while True:
        users_decision_formatted=input(users_input).strip().lower()
        if users_decision_formatted =='y' or users_decision_formatted=='n':
            return users_decision_formatted 
        else:
            print('Insert a valid entry')



welcome_statement=question_validaton_function("Do you want to play a game of Blackjack ? Type 'y' or 'n' :")


def first_two_cards(users_answer):
    players_deck_of_cards=[]
    updated_deck_of_cards=[]
    for _ in range (2):   # ciekawa iteracja przez petle, nie podajesz 'i' ale dajesz tylko '_'
        if users_answer=='y':
            
            choose_random_card=random.choice(deck_of_cards)
            deck_of_cards.remove(choose_random_card)
            players_deck_of_cards.append(choose_random_card)
            updated_deck_of_cards=deck_of_cards
    print(f'\nObecna talia kart to {updated_deck_of_cards},\n liczba kart to {len(updated_deck_of_cards)}\n')    
    return players_deck_of_cards , updated_deck_of_cards
    

            


players_deck_of_cards,updated_deck_of_cards=first_two_cards(welcome_statement)


def first_two_players_card(random_cards):
    players_total_score=0
    for i in random_cards:
        players_total_score+=i
    print(f'Your cards : {random_cards}, current score {players_total_score}')
    return players_total_score
     # w tej funkcji (?) bedzie trzeba dodac warunek ze jak players_total_score=21, to wtedy Player wygrywa i koniec gry 
    
players_total_score=first_two_players_card(players_deck_of_cards)






def first_two_dealers_card(updated_deck_of_cards,welcome_statement):
    dealers_total_score=0
    dealers_deck_of_cards=[]
    if welcome_statement=='y':
        for _ in range (2):   # ciekawa iteracja przez petle, nie podajesz 'i' ale dajesz tylko '_'         
            choose_random_card=random.choice(updated_deck_of_cards)
            updated_deck_of_cards.remove(choose_random_card)
            dealers_deck_of_cards.append(choose_random_card)
           
        for i in dealers_deck_of_cards:
            dealers_total_score+=i
        print(f'\nObecna talia kart to {updated_deck_of_cards},\n liczba kart to {len(updated_deck_of_cards)}\n')  
        print(f'Computers first card: {dealers_deck_of_cards[0]}, current score {dealers_total_score} - this is for Dev purpose only!!\n') 

        return  dealers_total_score

  
dealers_total_score=first_two_dealers_card(updated_deck_of_cards,welcome_statement)


#napisac warunki, taki plus ze potem ta funkcje bede sobie mogl wykorzystac pozniej juz za kazdym razem jak bede porownywal wyniki
def round_comparison(dealers_total_score,players_total_score,players_deck_of_cards):
    if players_total_score ==21 and len(players_deck_of_cards)==2: # check for the first round, if maybe the player did won
         return f'Player has won with :{players_total_score}'
         
    else: 
        if players_total_score > 21:
            print(f'Player has lost with :{players_total_score}')
            if players_total_score <= 21 and dealers_total_score >=21 and players_total_score > dealers_total_score :
                print(f'Player has won with :{players_total_score}')
            elif players_total_score <= 21 and dealers_total_score >=21 and players_total_score < dealers_total_score :
                print(f'Dealer has won with :{dealers_total_score}')
            elif players_total_score <= 21 and dealers_total_score >=21:
                if players_total_score == dealers_total_score :
                    print(f'There is a DRAW , Players score: {players_total_score}, Dealers score: {dealers_total_score}')
    
    

       

round_comparison(dealers_total_score,players_total_score,players_deck_of_cards)


continue_game_question=question_validaton_function("Type 'y' to get another card, type 'n' to pass: ")
""" 
    

"""