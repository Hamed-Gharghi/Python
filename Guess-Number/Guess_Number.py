# Author: Hamed Gharghi
# Date: 2024-07-26
# Description: A simple number guessing game where the player has 10 chances to guess a randomly generated number between 1 and 100.

from random import randint

# Generate a random number between 1 and 100
number = randint(1, 101)
chances = 10

# Start the guessing game
while chances > 0:
    guess = int(input("Guess a number between 1 and 100: "))

    if guess == number:
        print("Congratulations, you guessed the number!")
        print("You got it with " + str(chances) + " chances remaining!")
        break
    elif guess < number:
        print("Your guess is lower than the number. Let's try again.")
    else:
        print("Your guess is higher than the number. Let's try again.")

    # Decrease the number of chances
    chances -= 1

# Check if the player ran out of chances
if chances == 0:
    print("Sorry! You've used all your chances. The number was " + str(number) + ".")
