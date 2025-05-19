
print("Welcome to my computer quiz!")
playing = input("DO you want to play? ").lower()
if playing !='yes': 
    quit()
#  if equal to 'yes'
print("Okay ! Let's play :) ")

questions_list = ["What does CPU stand for? ","What does GPU stand for? ","What does RAM stand for? ","What does PSU stand for? "]
answers_list = ["central processing unit","graphics processing unit","random access memory","power supply unit"]
max_score = 0

for i in range(len(questions_list)):
    answer = input(questions_list[i]).lower()
    if answer == answers_list[i]: 
         print("Correct!")
         max_score += 1
    else: 
         print("Incorrect!")
    
print("You got " + str(max_score) + " Question Correct!")
print("You got " + str((max_score / 4 ) * 100) + " %")
    