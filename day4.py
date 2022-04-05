# Rock Paper Scissors

import random

rock = """ 
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

print("Welcome to Rock, Paper, Scissors game!")
choice = int(input("Type 0 for rock, 1 for paper, 2 for scissors: "))

if(choice == 0):
    print("You choosed:")
    print(rock)
elif(choice == 1):
    print("You choosed:")
    print(paper)
else:
    print("You choosed:")
    print(scissors)

random_number = random.randint(0,2)

if(random_number == 0):
    print("Computer choosed:")
    print(rock)
elif(random_number == 1):
    print("Computer choosed:")
    print(paper)
else:
    print("Computer choosed:")
    print(scissors)

if(random_number == choice):
    print("Its a draw!")
elif(choice == 0 and random_number == 1):
    print("You lose.")
elif(choice == 0 and random_number == 2):
    print("You win!")
elif(choice == 1 and random_number == 2):
    print("You lose.")
elif(choice == 1 and random_number == 0):
    print("You win!")
elif(choice == 2 and random_number == 0):
    print("You lose.")
elif(choice == 2 and random_number == 1):
    print("You win!")
