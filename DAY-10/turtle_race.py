import turtle 
import time
import random

WIDTH, HEIGHT = 500, 500 
COLORS = ['red','green','blue','orange','yellow','black','purple','pink','brown','cyan']

def get_number_of_racers(): 
    racers = 0
    while True: 
        racers = input("Enter the number between (2-10): ")  
        if racers.isdigit():  
            racers = int(racers)
            if 2 <= racers <= 10: 
                return racers
            else: 
                print("Number not in range. Try Again!") 
        else: 
            print("Input is not numeric. Try Again!")

def race(color):
    turtles = create_turtle(color)
    while True: 
        for racer in turtles: 
            distance = random.randrange(1, 20)  # Each turtle moves a random distance
            racer.forward(distance)
            x, y = racer.pos() 
            if y >= HEIGHT // 2 - 10:  # Check if any turtle has reached the top
                return color[turtles.index(racer)]  # Return the winning turtle color


def create_turtle(color): 
    turtles = []
    spacingx = WIDTH // (len(color) + 1)  # Space turtles evenly across screen width
    for i, color in enumerate(color): 
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)  # Turn turtle to face upwards
        racer.penup()
        racer.setpos(-WIDTH // 2 + (i + 1) * spacingx, -HEIGHT // 2 + 20)
        racer.pendown()
        turtles.append(racer)

    return turtles

def init_turtle(): 
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Turtle Racing Game')

# --- Main Program ---
racer = get_number_of_racers()

init_turtle()
random.shuffle(COLORS)
color = COLORS[:racer]
winner = race(color)
print("The winner is the turtle with color:", winner)
time.sleep(5)

turtle.done()
