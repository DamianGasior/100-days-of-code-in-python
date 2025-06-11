import random

#using random and list, create a lottery , who will pay the bill
random_int=random.randint(0,4)
friends=['Alice','Bob','Charlie','David','Emanuel']
print(f"The bill is paid today by: {friends[random_int]} !")

# using random.choice based on the list 
lucky_guy=random.choice(friends)
print(f"The chosen one today is: {lucky_guy} !")