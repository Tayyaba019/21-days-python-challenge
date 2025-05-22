import random 

user_scores = 0 
computer_scores = 0
range_of_computer = ["rock", "paper", "scissor"]

while True: 
    # Ask for user input and convert it to lowercase for consistency
    user_input = input("Type Rock/Paper/Scissor or q to quit: ").lower() 

    if user_input == 'q': 
        break

    #  Skip invalid input that is not rock/paper/scissor
    if user_input not in range_of_computer: 
        continue

    range_of_computer = ["rock", "paper", "scissor"]  # reset list (not necessary to reset every time)
    computer_play = random.randrange(0, 3)
    computer_input = range_of_computer[computer_play]

    #  Check win conditions for the user
    if user_input == "rock" and computer_input == 'scissor':
        print("You Win!")
        user_scores += 1
        
    elif user_input == 'paper' and computer_input == 'rock': 
        print("You Win!")
        user_scores += 1
         
    elif user_input == 'scissor' and computer_input == 'paper': 
        print("You Win!")
        user_scores += 1
    else: 
        print("You lost!")
        computer_scores += 1

#  Show final scores when the user quits the game
print("You won", user_scores, "times")
print("The computer won", computer_scores, "times")
print("Goodbye")
