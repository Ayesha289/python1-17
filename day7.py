# Hangman

import random
import day7data
import day7art

num = 5

word = random.choice(day7data.word_list)

blank_list = []
for i in range(0, len(word)):
    blank_list.append('_')
winning = False

print(hangmanArt.logo)

while(winning == False):
    guess_word = input("Guess a letter: ").lower()
    
    if guess_word in blank_list:
        print("You already guessed " + guess_word + " choose again!")
    
    for i in range(0, len(word)):
        if guess_word == word[i]:
            blank_list[i] = guess_word
            
    print(blank_list)
    
    if guess_word not in word:
        print("You guessed " + guess_word + " which is incorrect. You lose a life!")
        print(day7art.stages[num])
        num -= 1
        if num == 0:
            winning = True
            print("You Lose!")
        
    if '_' not in blank_list:
        winning = True
        print("You Won!")   