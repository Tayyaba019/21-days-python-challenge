import string 
import random

# Function to generate a secure password
def generate_password(min_length, numbers=True, special_character=True):
    letter = string.ascii_letters 
    digits = string.digits
    specials = string.punctuation  

    characters = letter 
    if numbers: 
        characters += digits
    if special_character: 
        characters += specials

    pwd = ''
    meet_criteria = False 
    has_number = False 
    has_special = False 

    while not meet_criteria or len(pwd) < min_length: 
        new_char = random.choice(characters)
        pwd +=  new_char  

        # Check if the character is a digit or special symbol
        if new_char in digits: 
            has_number = True
        elif new_char in specials: 
            has_special = True 

        # Ensure the password meets selected criteria
        meet_criteria = True 
        if numbers: 
            meet_criteria = has_number
        if special_character: 
            meet_criteria = meet_criteria and has_special 

    return pwd 

# Get user input for password preferences
min_length = int(input("Enter the minimum length: ")) 
has_number = input("Do you want to have numbers (y/n)? ").lower() == 'y'
has_special = input("Do you want to have special characters (y/n)? ").lower() == 'y'

# Generate and print the password
password = generate_password(min_length, has_number, has_special)
print("The generated password is:", password)
