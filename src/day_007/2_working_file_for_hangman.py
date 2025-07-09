import random

word_list=['camel','fiat','nike', 'malibu']

# 1. Randomly, choose a word froom the word_list and assign it to  a variable, chosen_word . Then print it
# 2.Ask the user to guess a letter and assign their answer to a variable called guess. Make a guess lowercase
# 3.Check if the letter theuser guessed ( guess) is one of the letters i the chosen_word . Print "Right" if it is, 
# "Wrong" if its not. 
#
#

chosen_word=random.choice(word_list)
print(chosen_word)

guess=input('Choose a letter: ').lower()

print(guess)

for i in chosen_word:
    if guess==i:
        print('Right')
    else:
        print('Wrong')