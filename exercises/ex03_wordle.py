"""EX03 - Wordle - The final step towards Wordle."""

__author__ = 730660578

# Variables for the box colors that will be our output. 
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

def contains_char(searched_thru_word: str, searched_for_char: str) -> str:
    """Determines if a given character appears at any index in the secret word."""
    # Ensure the length of the character is 1. 
    assert len(searched_for_char) == 1
    idx: int = 0
    char_check: bool = False
    # Run a loop until a match has been found or we run out of letters. 
    while (char_check is not True) and (idx < len(searched_thru_word)):
        # Check to see if the given index of the word matches the character we are checking.
        if searched_thru_word[idx] == searched_for_char:
            char_check = True
        else: # If the letter is not found at the idx of the word.
            idx += 1
    # The character has been found somewhere in the secret word. 
    if char_check == True:
        return True
    # The character is not found anywhere in the secret word. 
    else: 
        return False
    
def emojified(guess: str, secret: str) -> str:
    """Codifies the guessed word to show which characters appear elsewhere."""
    assert len(guess) == len(secret) 
    idx2: int = 0
    results: str = ""
    # Loop until all indices of the secret word have been checked. 
    while idx2 < len(secret): 
        # The corresponding characters are an exact match. 
        if guess[idx2] == secret[idx2]: 
            results += GREEN_BOX
        # The character in the guessed word appears in the secret word, but the location is wrong. 
        elif contains_char(secret, guess[idx2]) is True:
            results += YELLOW_BOX
        # The character does not appear anywhere in the secret word. 
        else: 
            results += WHITE_BOX
        idx2 += 1
    return results

def input_guess(word_length: int) -> int: 
    """Ensures that the guessed word is of equal lenght with the secret word."""
    # Prompt user for a guess.
    input_word: str = input(f"Enter a {word_length} character word: ")
    # Continue to prompt for a guess until the correct number of characters is entered. 
    while len(input_word) != word_length:
        input_word: str = input(f"That wasn't {word_length} chars! Try again: ")
    return input_word

def main() -> None:
    """The entrypoint of the program and main game loop."""
    turn_idx: int = 1
    todays_secret_word: str = "codes"
    win_check: bool = False
    # Run the game until all turns have been used or the correct word is guessed. 
    while (turn_idx < 7) and  (win_check is not True):
        # Print the current turn number. 
        print(f"=== Turn {turn_idx}/6 ===")
        # Prompt user for a guess of correct length and store it as a variable. 
        users_guess = input_guess(len(todays_secret_word))
        # Codify the emoji results of the users guess versus the secret. 
        print(emojified(users_guess, todays_secret_word))
        # Check to see if the users guess was correct. 
        if users_guess == todays_secret_word:
            # The user won!
            win_check = True
        else:
            # Increase the turn number
            turn_idx += 1
    # Tell the user that they have won! 
    if win_check is True:
        print(f"You won in {turn_idx}/6 turns!")
    # Tell the user to come back tomorrow. 
    else:
        print("X/6 - Sorry, try again tomorrow!")

# Allow for the program to be run as a module. 
if __name__ == "__main__":
    main()