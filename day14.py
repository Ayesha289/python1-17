# Higher Lower Game

from day14art import logo, vs_logo  
from day14data import data
import random

score = 0
data2 = random.choice(data)

import os
def clear(): 
    os.system('cls')

def display_data(account):
    account_name = account['name']
    account_info = account['description']
    account_place = account['country']
    return f"{account_name}, a {account_info}, from {account_place}."

def score_count(choice, num1, num2):
    if (num1 > num2):
        if choice == 'a':
            return True
        else:
            return False
    else:
        if choice == 'b':
            return True
        else:
            return False

print(logo)
start = True

while(start):
    data1 = data2
    data2 = random.choice(data)
    if(data1 == data2):
        data2 = random.choice(data)

    num1 = data1['follower_count']
    num2 = data2['follower_count']

    print(f"Compare A: {display_data(data1)}")
    print(vs_logo)
    print(f"Against B: {display_data(data2)}")
    choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    
    clear()
    print(logo)

    if(score_count(choice, num1, num2)):
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        print(f"Sorry, you're wrong. Current score: {score}.")
        start = False