# Password Generator

import random

letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
character = ['!', '@', '#', '$', '%', '&', '*', '(', ')']

print("Welcome to Password Generator")
length = int(input("How long do you want your password? "))
letter_choice = int(input("How many alphabets do you want? "))
number_choice = int(input("How many numbers do you want? "))
character_choice = int(input("How many characters do you want? "))

password = []
for x in range(0, letter_choice):
    random_number = random.randint(0, letter_choice-1)
    password.append(letter[random_number])

for y in range(0, number_choice):
    random_number = random.randint(0, number_choice-1)
    number[random_number] = str(number[random_number])
    password.append(number[random_number])

for z in range(0, character_choice):
    random_number = random.randint(0, character_choice-1)
    password.append(character[random_number])

random.shuffle(password)
print("Your password is: " + ''.join(password))
