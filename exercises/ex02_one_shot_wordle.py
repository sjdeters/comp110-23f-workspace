"""EX02 - One Shot Wordle - Another step towards Wordle"""

__author__ = "730660578"

secret_word = "python"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

# Prompt user to input a guessed_word for the secret word.
guessed_word: str = input(f"What is your {len(secret_word)}-letter guessed_word? ")

# Variable to track which letter we are looking at. 
idx: int = 0
# Variable to show which letters are correct, in the wrong location, or incorrect. 
results: str = ("")

# Make sure the length of the guessed_word is the correct number of letters. 
while len(guessed_word) != len(secret_word): 
    guessed_word: str = input(f"That was not {len(secret_word)} letters! Try again: ")

# Look at each letter in the secret word. 
while idx < len(secret_word):
    # The letter in the guessed word is the same as the letter in the secret word. 
    if guessed_word[idx] == secret_word[idx]:
        results += GREEN_BOX
    # The letters do not match. 
    else:
        # Checks to see if a match has been found. 
        chr_test: bool = False
        # Keeps track of which letter we are looking at in the secrret word. 
        alt_idx: int = 0
        # Look at every other letter in the secret word. 
        while (chr_test != True) and (alt_idx < len(secret_word)):
            # Check to see if the letter is present somewhere else. 
            if secret_word[alt_idx] == guessed_word[idx]:
                chr_test = True
            else:
                alt_idx += 1
        # The letter in the guessed word can be found somewhere else in the secret word. 
        if chr_test == True:
            results += YELLOW_BOX
        # The letter in the guessed word is not in the secret word. 
        else:
            results += WHITE_BOX
    idx += 1

# Print which letters are in the correct space. 
print(results)

# Check to see if the guessed_word is the same as the secret word. 
if guessed_word == secret_word:
    # guessed_word is correct.
    print("Woo! You got it!")
else: 
    # guessed_word is incorrect. 
    print("Not quite. Play again soon!")