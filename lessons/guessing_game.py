"""Program that loops until correct number is guessed."""

from random import randint

secret_number: int = randint(1,10)
guess: int = int(input("Guess a number between 1 and 10: "))
number_of_tries: int = 1
max_tries: int = 3

while (guess != secret_number) and (number_of_tries < max_tries):
    print("Wrong!")
    # If guess is out of bounds, let them know. 
    if (guess < 1) or (guess > 10):
        print("That's not between 1 and 10!")
    # If guess is too low, tell them. 
    elif guess < secret_number:
        print("Too low!")
    # If guess is too high, tell them.  
    else: 
        print("Too high!")
    # Ask for a different guess. 
    guess = int(input("Guess again: "))
    number_of_tries += 1

# If I've reached this point, guess == secret_word. 
if guess == secret_number:
    print("You guessed correctly!")
else: 
    print("You lose. :(")

print(f"The secret number was {secret_number}.")