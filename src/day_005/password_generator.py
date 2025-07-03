import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']



print('Welcome to the PyPassword Generator!')


while True:
    try:
        number_of_letters=int(input('How many letters would you like in your password?\n'))
        break #if user does provide the correcnt input break the loop 
    except ValueError:
        print('Incorrect input.Please insert a natural number\n')


while True:
    try:
        number_of_symbols=int(input('\nHow many symbols would you like in your password??\n'))
        break #if user does provide the correcnt input break the loop 
    except ValueError:
        print('Incorrect input.Please insert a natural number\n')



while True:
    try:
        number_of_numbers=int(input('\nHow many number would you like in your password?\n'))
        break #if user does provide the correcnt input break the loop
    except ValueError:
        print('Incorrect input.Please insert a natural number\n')




"""Creating below three lists which will be taking  a random number of paremters  from each list.
The amount of  random parameteres will be detrmined by users input"""

r_letters=random.sample(letters,number_of_letters)
r_symbols=random.sample(symbols,number_of_symbols)
r_numbers=random.sample(numbers,number_of_numbers)

"""Simple 'order' for the parameters in the password. Frist letter, then symbols and the end numbers.
In result a 'new_ordered_password' is created with the above sequence """

new_ordered_password=""

for i in r_letters:
    new_ordered_password+=i

for i in r_symbols:
    new_ordered_password+=i

for i in r_numbers:
    new_ordered_password+=i


print(f'\nYour new ordered password is : {new_ordered_password}')
print(f'Your password has {len(new_ordered_password)} characters\n')

"""More complex or disordered order in the 'new_disordered_password' but using the same parameters like for 'new_ordered_password'"""

combined_list_of_three=r_letters+r_symbols+r_numbers



random.shuffle(combined_list_of_three) # the same list , its just shuffled , / order of the characters in the list is changed to be random



new_disordered_password=""

for x in  combined_list_of_three:
    new_disordered_password+=x

print(f'Your new disordered password is : {new_disordered_password}')
print(f'Your password has {len(new_disordered_password)} characters\n')

