print('Welcome to Treasure Island.\n')
print('Your mission is to find the treasure')
print('\nYou are at crossroad. Where do you want to go ? ')

left_right=(input('type "left" or "right": ')).lower()

if left_right=='left':
    print('\nYou have come to a lake. There is an island in the middle of the laek')
    wait_swim=input('Type "wait" or  "swim" to swim across. ').lower()

    if wait_swim=='wait':
        print('\nYou arrive at the island unharmed. There is a house with 3 doors')
        colour=input('One "red", one "yellow" and one "blue". Which colour do you choose ? ').lower()

        if colour=='yellow':
            print('\nYou win!')

        elif colour=='blue':
            print('\nGAME OVER\nEaten by beasts')
            
        elif colour=='red':
              print('GAME OVER\nBurned by fire.')

    else:
            print('\nGAME OVER\nAttacked by trout')

else:
            print('GAME OVER\nFall into a hole')
    
    

