name = input("Enter your name: ") 
print("Welcome", name, "to this adventure")

# Asking the player for their first decision: left or right
answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

if answer == 'left': 
    # Handling the 'left' path choice
    answer = input("You come to a river, you can walk around or swim across: ").lower()
    if answer == 'walk': 
        print("You walked many miles, ran out of water and you lost the game")
    elif answer == 'swim':
        print("You swam across and were eaten by an alligator.")
    else: 
        print('Not a valid option. You lose.')

elif answer == 'right': 
    # Handling the 'right' path choice
    answer = input('You come to a bridge, it looks wobbly. Do you want to cross it or head back (cross/back)? ').lower()
    if answer == 'back': 
        print("You go back and lose.")
    elif answer == 'cross':
        answer = input("You cross the bridge and meet a stranger. Do you talk to them (yes/no)? ").lower() 
        if answer == 'yes': 
            print("You talk to the stranger and they give you gold. You WIN!")
        elif answer == 'no':  
            print("You ignored the stranger and they are offended and you lose.")
        else: 
            print('Not a valid option. You lose.')
    else: 
        print('Not a valid option. You lose.')

else: 
    print("Not a valid option. You lose.")

# End of the game
print("Thank you for trying", name)
