# Ceaser Cipher

import day8art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(day8art.logo)
key = True

while(key):
    method = input("Type 'encode' to encrypt and 'decode' to decrypt:\n")
    message = input("Type the message:\n").lower()
    shift = int(input("Type the number of shift:\n"))

    def ceaser(text_message, total_shift, method_of_direction):
        cipher_text = ""
        
        if(total_shift>26):
            total_shift = round(total_shift % 26)

        for char in text_message:
            if char in alphabet:
                position = alphabet.index(char)
                if(method_of_direction == 'encode'):
                    new_position = position + total_shift
                    if(new_position>26):
                        new_position -= 26
                elif(method_of_direction == 'decode'):   
                    new_position = position - total_shift
                    if(new_position<0):
                        new_position += 26 
                else:
                    print("Please input correctly!")
                text = alphabet[new_position]
                cipher_text += text
            else:
                cipher_text += char

        print(f"The {method_of_direction}d text is {cipher_text}")
        
    ceaser(text_message = message, total_shift = shift, method_of_direction = method)

    choice = input("Do you want to continue? Type 'yes' or 'no':\n")
    if(choice == 'yes'):
        key = True
    else:
        key = False 
        print("Goodbye")  