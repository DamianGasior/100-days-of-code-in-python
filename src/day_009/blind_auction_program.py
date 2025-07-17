print("Welcome to the secret action program\n")

other_bidders=''
all_bid_prices={}



def blind_auction_game():

    users_name=input('What is your name ? :')
  
    while True:
        users_bid_price=input("What's your bid? : $ ")
        try:
            bid_price=float(users_bid_price)
            if bid_price>=0:
                break
            else:
                print('Please populate a number')
        except ValueError:
            print('Insert a valid number')
    
    all_bid_prices[users_name]=users_bid_price
    return all_bid_prices

blind_auction_game()
    
while True:
    other_bidders=input("\nAre there any other bidders? Type 'yes' or 'no':").lower()
    if other_bidders=='yes':
        print('\n' * 100)
        blind_auction_game()
    elif other_bidders=='no':
        #check with the below the data type in the dictionary, you will see its str in value, example : 
        #type for dam1 -> type : <class 'str'>, for value : 100 -> type :<class 'str'>
        #type for dam2 -> type : <class 'str'>, for value : 20 -> type :<class 'str'>
        #type for dam3 -> type : <class 'str'>, for value : 5 -> type :<class 'str'>

        """ for key,value in all_bid_prices.items():
            print(f'type for {key} -> type : {type(key)}, for value : {value} -> type :{type(value)} ') """

        print('\nGAME OVER\n')
        
        winner_value=max(all_bid_prices.items(), key=lambda item: float(item[1])) # float necessary to compare numbers, not strings..
       
        print(f'The winner is: {winner_value[0]} with a bid of $: {winner_value[1]} \n')
        break

    else:
        print('Invalid answer, please answer again.') 

