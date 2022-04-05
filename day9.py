import day9art
import os

print(day9art.logo)
print("Welcome to the secret auction program.")
loop_bid = True

bidders = {}

def clear(): 
    os.system('cls')
    
max_bet = 0
bet_name = ""

while(loop_bid):   
    name = input("What is your name? ")
    amount = int(input("What's your bid: $"))
    bidders[name] = amount
    
    for bidding in bidders:
        bidding_amount = bidders[name]
        if(bidding_amount>max_bet):
            max_bet = bidding_amount
        bet_name = bidding

    continue_bid = input("Are there any other bidders? Type 'yes' or 'no'. \n")
    if(continue_bid == 'yes'):
        clear()
        continue
    else:
        clear() 
        print(f"The winner is {bet_name} with a bet of ${max_bet}")
        loop_bid = False