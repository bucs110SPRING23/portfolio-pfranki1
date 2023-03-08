import random 
n=random.randrange(1,10)
g=int(input("Guess a number 1-10:"))
for i in range(2):
    if g>n:
        print("Too high:")
        g=int(input("Guess again:"))
    elif g<n:
        print("Too low:")
        g=int(input("One more guess:"))
    else:
        print("you got it")
        break 
