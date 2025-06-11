import random
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))



#importing/referring to specific variables only , easiest way to get the asscii's
from common.rpis_ascii_art import rock, paper, scissors

users_value=input('''Dear user, please populate following number 0, 1  0r 2.\n
0 - rock
1 - paper
2 - scissors\n
Your input is: ''')

#changing users input string into an int
users_value=int(users_value)


#matching users input withe one of the three options 

if users_value==0:
    users_value_chosen= rock
elif users_value==1:
    users_value_chosen= paper
elif users_value==2:
    users_value_chosen=  scissors
else:
    users_value_chosen='Users value is incorret'

print(f'What is equal to: {users_value_chosen}')

#Computers guess out of three available options in the list 

computers_options=[rock, paper, scissors]
computers_guess=random.choice(computers_options)




print(f'Computers input is: {computers_guess} ')


if computers_guess == users_value_chosen :
    print('There is a draw !')
elif computers_guess == paper and  users_value_chosen == rock :
    print('Computer won!')
elif computers_guess == rock and  users_value_chosen == scissors:
    print('Computer won!')
elif  computers_guess == scissors and  users_value_chosen == paper :
     print('Computer won!')
elif users_value not in [0,1,2]:  # adding  a seperate notification in case users input will not one of those three  : 0,1 or 2
    print('Computer won due to users incorrect input !')
else : 
     print('You won!')