import random

num = random.randint(1,20)
guess = int(input("Guess a number I'm thinking... It's less than 20 "))

while num!=guess :
    if guess>num:
        print("Think lesser...")
    else :
        print("Think higher...")

print("You Won !")
