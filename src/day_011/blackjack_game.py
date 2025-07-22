
deck_of_cards=[11,2,3,4,5,6,7,8,9,10,10,10,10,11,2,3,4,5,6,7,8,9,10,10,10,10,11,2,3,4,5,6,7,8,9,10,10,10,10,11,2,3,4,5,6,7,8,9,10,10,10,10 ]


def question_validaton_function(users_input): 
    while True:
        users_decision_formatted=input(users_input).strip().lower()
        if users_decision_formatted =='y' or users_decision_formatted=='n':
            return users_decision_formatted 
        else:
            print('Insert a valid entry')



welcome_statement=question_validaton_function("Do you want to play a game of Blackjack ? Type 'y' or 'n' :")

continue_game_question=question_validaton_function("Type 'y' to get another card, type 'n' to pass: ")


