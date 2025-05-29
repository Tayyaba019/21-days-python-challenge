import random 
import time 

OPERATOR = ["+", "-", "*"] 
MIN_OPERAND = 3 
MAX_OPERAND = 12 
TOTAL_PROBLEM = 5

# Function to randomly generate a math problem
def generate_problem(): 
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND) 
    operator = random.choice(OPERATOR)
    expr = str(left) + " " + str(operator) + " " + str(right)
    answer = eval(expr)  # Calculate the result using eval
    return expr, answer  

wrong = 0 
start_time = time.time()

print("Press enter to start")
print("---------------------")

start_time = time.time()

# Loop through total number of problems
for i in range(TOTAL_PROBLEM): 
    expr, answer = generate_problem()  
    while True:
        guess = input("Problem #" + str(i+1) + " " + expr + " = ") 
        if guess == str(answer):
            break
        wrong += 1  # Increase wrong counter if answer is incorrect

end_time = time.time() 
Total_time = round(end_time - start_time)

print("---------------------")
print("Number of times you solved Wrong:", wrong)
print("Nice Work!", "You finished it in", Total_time, "seconds!")
