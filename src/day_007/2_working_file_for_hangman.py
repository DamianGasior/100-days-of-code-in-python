import random

from hangman_ascii_art import hangman
from hangman_logo import logo
from word_list import word_list

print(logo,'\n')



chosen_word=random.choice(word_list)
#print(chosen_word)   commetning the word for the user, for dev and testing purpose please uncomment it
my_list=[]

for i in range(len(chosen_word)):
    print('_', end=" ")     # end="  - this allows you to print any character next to each other , instead of one below another one. 
    my_list.append('_')     # creating a list with  the number of underscores equal to the  length of the chosen_word


print('\n')

#attempts below will be later used to count the succesfull or failed number of attempts in guessing the letters

succesfull_attempts=0
failed_attempts=0

#run the wile loop till there will be still some unguessed ('_') in my_list, break it when 6 attempts reached 

while '_' in my_list and failed_attempts < 6:
    guess=input('\nChoose a letter: ').lower()

    if guess not in my_list:
    #using function enumarate, where I can iterate throug my randomly chosen_word and I can have access to the 'index' and 'value' of the chosen_word

        for index, symbol in enumerate(chosen_word):
            
            if guess==symbol :
                my_list[index]=symbol
            elif guess!=symbol :
                if my_list[index]=='_':
                    my_list[index]='_'
                else:
                    continue
        #creating an empty string, where I will display letters and '_' each time after users guess
        my_word=''

        #adding all the elements from my_list to the my_word, so that we can print it out in a nice format to the user
        for i in my_list:
            my_word+=i

        if guess in my_word:
            succesfull_attempts+=1
        else:
            failed_attempts+=1
            print(f'\nYou guessed "{guess}", thats not in the word. You lose life.')

        
        remaining_lives=6-failed_attempts
        


        if  failed_attempts <6 :
            print(hangman[failed_attempts])
            print(f'\nYour guessed letters are: {my_word}\n')
            print(f'\n************************************************** {remaining_lives} out of 6 LIVES LEFT *************************************************************\n')
        elif failed_attempts == 6:
            print(hangman[failed_attempts])
            print(f'\nThe word which you needed to guess was: {chosen_word}')
            print(f'\n************************************************** {remaining_lives} out of 6 LIVES LEFT *************************************************************\n')
            print('\n*************************************************** YOU LOSE ******************************************************')
        
    
    # if the  the hosen letter was already guessed, print to the user the below message
    else:
        print(f'You guessed a "{guess}" letter, that is already there. You keep your life.Try again')    


if '_' not in my_word:
    print('*****************************************************YOU WIN******************************************************\n')


