#3

import random

#based on random.random method print "Heads" or "Tails"
random_number=random.random()
if random_number >= 0.5:
    print("Now you have gotten: heads")
else:
    print("Now you have gotten: tails")


# or in onother way , just simplyfing ( 0 or 1)


random_integer=random.randint(0,1)
if random_integer ==1:
    print("Now you've drawn: heads")
else:
    print("Now you've drawn: tails")


