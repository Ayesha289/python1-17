# Treasure Finder

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

road = input('You are at a cross road. Where do you want to go? Type "left" or "right".\n')
if (road == 'left'):
    action = input('You come to a lake. There is an island in the middle of the lake. Do you want to wait for the boat or swim across? Type "wait" for a boat or "swim" to swim! \n')
    if(action == 'wait'):
        door = input('You reached island safely. Now you come across a big wall with three doors colored blue, yellow, red. Which door do you choose? "red", "blue", "yellow"? \n ')
        if(door == 'blue'):
            print("Congratulations!! You find the treasure!!!!")
        elif(door == 'red'):
            print("You got caught by the people of island! Game Over!")
        else:
            print("You got caged in between the four walls with nothing to survive! Game Over!")
    else:
        print("You were eaten by the crocodiles in the lake! Game Over!")
else:
    print("You reached jungle, where there are lots of wild animals with no way of return! Game Over!")