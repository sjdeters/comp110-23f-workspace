"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730660578"

word_input: str = input("Enter a 5-character word: ")
# This prompts user to input a word, then sets variable (word_input) to the word enterred.

if len(word_input) != 5:
    print("Error: Word must contain 5 characters")
    exit()
# This checks to see if the word length is equal to 5. 

character_input: str = input("Enter a single character: ")
# This prompts user to input a character, then sets variable (character_input) to the character entered.

if len(character_input) != 1:
    print("Error: Character must be a single character.")
    exit()
# This checks to see if the character length is equal to 1. 

num_of_characters: int = 0
# This is the variable that is being used to track the number of times the character is in the word.

print("Searching for " + character_input + " in " + word_input)

if word_input[0] == character_input:
    print(character_input + " found at index 0")
if word_input[1] == character_input:
    print(character_input + " found at index 1")
if word_input[2] == character_input:
    print(character_input + " found at index 2")
if word_input[3] == character_input:
    print(character_input + " found at index 3")
if word_input[4] == character_input:
    print(character_input + " found at index 4")
# The above section is finding at which indices the character is found.

if (word_input[0] == character_input):
    num_of_characters = num_of_characters + 1
if (word_input[1] == character_input):
    num_of_characters = num_of_characters + 1
if (word_input[2] == character_input):
    num_of_characters = num_of_characters + 1
if (word_input[3] == character_input):
    num_of_characters = num_of_characters + 1
if (word_input[4] == character_input):
    num_of_characters = num_of_characters + 1
# The above section is counting the number of times the character appears in the word.

if num_of_characters == 0:
    print("No instances of " + character_input + " found in " + word_input)
if num_of_characters == 1:
    print(str(num_of_characters) + " instance of " + character_input + " found in " + word_input)
if num_of_characters > 1:
    print(str(num_of_characters) + " instances of " + character_input + " found in " + word_input)
# The above section states how many times the character appears in the word. 