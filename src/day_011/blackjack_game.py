
def question_validaton_function(users_input): 
    while True:
        users_decision_formatted=input(users_input).strip().lower()
        if users_decision_formatted =='y' or users_decision_formatted=='n':
            break
        else:
            print('Insert a valid entry')



welcome_statement=question_validaton_function("Do you want to play a game of Blackjack ? Type 'y' or 'n' :")


continue_game_question=question_validaton_function("Type 'y' to get another card, type 'n' to pass: ")
