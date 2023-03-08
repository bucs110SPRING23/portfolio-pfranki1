import random 
n=random.randrange(1,1000)
g=int(input("Guess a number 1-1000:"))
count=0
for i in range(1000):
    if g>n:
        print("Too high:")
        g=int(input("Guess again:"))
        count+=1
    elif g<n:
        print("Too low:")
        g=int(input("Try again:"))
        count+=1
    else:
        print("You figured it out in", str(count), "attempts")
        break
