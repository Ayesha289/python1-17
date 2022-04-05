# Blackjack

import random
import os 
clear = lambda: os.system('cls')  

from day11art import logo

conti_game = True
while(conti_game):
    
    def blackjack():
        print(logo)
        user_card = []
        comp_card = []
        
        def new_card():
            cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
            card = random.choice(cards)
            return card
        
        for i in range(0,2):
            user_card.append(new_card())
        for i in range(0,2):
            comp_card.append(new_card())

        def score(card):
            sum = 0
            if sum > 21 and 11 in card:
                card.remove(11)
                card.append(1)
            for x in card:
                sum += x
            if 10 in card and 11 in card and sum == 21:
                return 0
            return sum
            
        user_score = score(user_card)
        comp_score = score(comp_card)

        def winning_score(user_score, comp_score):
            if user_score == comp_score:
                print("It's a draw!")
            elif user_score == 0:
                print("You win with a Blackjack!")
            elif comp_score == 0:
                print("Opponent has a blackjack! you lose!")
            elif comp_score > 21 and user_score > 21:
                print("Oops! Both are over 21, Play again to win!")
            elif user_score > 21:
                print("You went over, you lose!")
            elif comp_score > 21:
                print("Opponent went over, you win!")
            elif user_score > comp_score:
                print("You win!")
            else:
                print("You lose!")

        while(comp_score<17):
            comp_card.append(new_card())
            comp_score = score(comp_card)

        next_move = True
        while(next_move):
            if user_score > 21:
                print(f"    Your final hand: {user_card}, final score = {user_score}")
                print(f"    Opponent's cards: {comp_card}, final score = {comp_score}")
                winning_score(user_score, comp_score)
                next_move = False
            else:
                print(f"    Your cards: {user_card}, current score = {user_score}")
                print(f"    Computer's first card: {comp_card[0]}")
                next_step = input("Type 'y' to get another card, type 'n' to pass: ")
                if next_step == 'y':
                    user_card.append(new_card())
                    user_score = score(user_card)
                else:
                    print(f"    Your final hand: {user_card}, final score = {user_score}")
                    print(f"    Opponent's cards: {comp_card}, final score = {comp_score}")
                    winning_score(user_score, comp_score)
                    next_move = False

    choice = input("\nDo you want to play Blackjack? Type 'y' or 'n': ")
    if choice == 'y':
        clear()
        blackjack()
    else:
        conti_game = False