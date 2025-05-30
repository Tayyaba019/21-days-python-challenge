import random 

# Function to simulate rolling a dice
def roll(): 
    min = 1 
    max = 6
    dice_roll = random.randint(min, max)
    return dice_roll 

# Input: number of players
while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit(): 
        players = int(players)
        if 2 <= players <= 4: 
            break
        else: 
            print("Number must be between (2-4)") 
    else: 
        print("Invalid Number")

max_score = 50       
player_scores = [0 for _ in range(players)]  # Initialize scores for all players

# Main game loop
while max(player_scores) < max_score:
    for player_idx in range(players): 
        print("\nPlayer number", player_idx+1, "turn has just started\n") 
        current_score = 0 
        while True:
            should_roll = input("Would you like to roll? (y): ") 
            if should_roll.lower() != 'y':
                break 

            value = roll() 
            if value == 1:  # If dice roll is 1, end turn with 0 points
                print("You rolled a 1, turn done")
                current_score = 0 
                break 
            else: 
                current_score += value 
                print("You rolled a", value)
            print("Your current score is", current_score)

        player_scores[player_idx] += current_score
        print("Your total score is", player_scores[player_idx])
