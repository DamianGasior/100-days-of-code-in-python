print("Welcome to Pizza Deliveries!\n")
size=input('What size pizza do you want? S, M or L: ')
pepporoni=input('Do you want pepperoni on your pizza? Y or N: ')
extra_cheese = input('Do you want extra cheese ? Y or N: ')

price_pizza=0

if size=='S':
    price_pizza=15
elif size=='M':
    price_pizza=20
elif size=='L':
    price_pizza=25
else:
    print('type incorrect pizza size')

if pepporoni=='Y':
    if size=='S':
        price_pizza+=2
    else:
        price_pizza+=3

if extra_cheese=='Y':
    price_pizza+=1

print(f'Your final bill is: ${price_pizza}')



