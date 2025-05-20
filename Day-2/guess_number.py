import random 

# Take upper limit input from the user
guess_number = input("Type a number: ") 
if guess_number.isdigit(): 
    guess_number = int(guess_number)
    if guess_number <= 0: 
        print("Type a number larger than zero next time")
else: 
    print("Type digit next time")

# Generate a random number between 0 and the given limit
random_number = random.randrange(guess_number)
guess = 0

while True: 
    guess += 1
    user_number = input("Make a guess: ") 
    if user_number.isdigit(): 
        user_number = int(user_number)
        if user_number <= 0: 
            print("Type a number larger than zero next time!")
    else:
        print("please a number next time")
        continue
    if random_number == user_number: 
        print("You guess the number")
        break
    elif random_number > user_number: 
        print("Try greater Number") 
    
    else:
        print("Try below number")
# Show total number of guesses made       
print("you got it in ",guess,"guesses")