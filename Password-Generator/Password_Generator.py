# Author: Hamed Gharghi
# Date: 2024-07-26
# Description: A simple password generator that creates a random password with a mix of uppercase letters, lowercase letters, digits, and special characters.

import random
import string

def generate_password(length):
    #Generate a random password of a specified length between 8 and 16 characters.
    if length < 8 or length > 16:
        return "Password length must be between 8 and 16 characters."

    # Define character sets
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special_chars = string.punctuation

    # Ensure the password contains at least one character from each set
    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(special_chars)
    ]

    # Fill the rest of the password length with random choices from all character sets
    all_chars = uppercase + lowercase + digits + special_chars
    remaining_length = length - 4
    while remaining_length > 0:
        password.append(random.choice(all_chars))
        remaining_length -= 1

    # Shuffle the list to ensure random order
    random.shuffle(password)
    
    # Convert list to string
    return ''.join(password)

print("Welcome to the Password Generator!")
length = int(input("Enter the desired password length (8 to 16): "))
print(f"Generated password: {generate_password(length)}")
