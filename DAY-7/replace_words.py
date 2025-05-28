with open("story.txt", 'r') as f: 
    story = f.read()  # Read the story content from the file

words = set() 
start_of_word = -1 

target_start = '<'
target_end = '>'

# Extract all placeholder words inside < > brackets
for i, char in enumerate(story): 
    if char == target_start: 
        start_of_word = i
    if char == target_end and start_of_word != -1: 
        search_word = story[start_of_word:i+1]
        words.add(search_word)

answers = {} 

# Ask the user to enter a value for each placeholder
for word in words:
    answer = input("Enter a word for " + word + ": ")
    answers[word] = answer 

# Replace all placeholders with the user-provided words
for word in words: 
    story = story.replace(word, answers[word])

print(story)  # Print the final story with words filled in
