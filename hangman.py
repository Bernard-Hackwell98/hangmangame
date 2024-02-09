import random

print("Welcome to the Hangman Game")
words = ["ospreay", "omega", "okada"]
secret_word = random.choice(words)
display = [] 
counter = 0
print("You have 5 guesses")

for letter in secret_word:
    display += "_"  
print(display)

guesser = False
while not guesser:
    theword = input("Take a guess: ").lower()

    for position in range(len(secret_word)):
        letter = secret_word[position]
        if letter == theword:
            display[position] = letter  

    if theword not in secret_word:  
        counter += 1
        guesses_left = 5 - counter
        print(f"You have {guesses_left} guesses left")
        if counter >= 5:
            print("You lose")
            guesser = True

    print(display)

    if "_" not in display: 
        print("You win")
        guesser = True