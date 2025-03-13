import random


print("Welcome to the Number Guessing Game!")
target = random.randint(1, 20)

while True:
    guess = input("Guess a number from 1 - 20  or enter 'quit' to exit ): ")

    if guess.lower() == 'quit':
        print("Thanks for playing")
    elif not guess.isdigit():
        print("Invalid input")
        continue
    guess = int(guess)
    if target==guess:
        print("You won!")
        break
    elif target>guess:
        print("Too low... try again")
    else:
        print("Too high... try again") 
        pass

print("Game over!")
    