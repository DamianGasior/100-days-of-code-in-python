import random

from hangman_ascii_art import hangman

word_list=['aardvark', 'ubuebuue']

# 1. Randomly, choose a word froom the word_list and assign it to  a variable, chosen_word . Then print it
# 2.Ask the user to guess a letter and assign their answer to a variable called guess. Make a guess lowercase
# 3.Check if the letter theuser guessed ( guess) is one of the letters i the chosen_word . Print "Right" if it is, 
# "Wrong" if its not. 
#
#

chosen_word=random.choice(word_list)
print(chosen_word)
my_list=[]

for i in range(len(chosen_word)):
    print('_', end=" ")     # end="  - this allows you to print any character next to each other , instead of one below another one. 
    my_list.append('_')     # creating a list with  the number of underscores equal to the  length of the chosen_word



#attempts below will be later used to count the succesfull or failed number of attempts in guessing the letters

succesfull_attempts=0
failed_attempts=0

#run the wile loop till there will be still some unguessed ('_') in my_list, break it when 6 attempts reached 

while '_' in my_list and failed_attempts < 6:
    guess=input('\nChoose a letter: ').lower()

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

    if  failed_attempts <6:
        print(hangman[failed_attempts])
        print(my_word,'\n')
    elif failed_attempts == 6:
        print('You lose')
        print(hangman[failed_attempts])
        





    

if '_' not in my_word:
    print('You won!\n')


