# Number Guessing Game
import random
from day12art import logo

print(logo)
print("\nWelcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 - 100.")

NUMBER = random.randint(1,100)

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == 'easy':
    x = 10
    while x > 0:
        print(f"You have {x} attempts to guess the number.")
        guess = int(input("Make a guess: "))
        if guess < NUMBER and x > 1:
            print("Too low.")
            print("Guess again.")
        elif guess > NUMBER and x > 1:
            print("Too high.")
            print("Guess again.")
        elif guess == NUMBER:
            print(f"You got it! The answer was {NUMBER}")
            break
        x -= 1
        if (x == 0):
            print(f"You lose! The correct guess was {NUMBER}")
            break

elif difficulty == 'hard':
    x = 5
    while x > 0:
        print(f"You have {x} attempts to guess the number.")
        guess = int(input("Make a guess: "))
        if guess < NUMBER and x > 1:
            print("Too low.")
            print("Guess again.")
        elif guess > NUMBER and x > 1:
            print("Too high.")
            print("Guess again.")
        elif guess == NUMBER:
            print(f"You got it! The answer was {NUMBER}")
            break
        x -= 1
        if (x == 0):
            print(f"You lose! The correct guess was {NUMBER}")
            break