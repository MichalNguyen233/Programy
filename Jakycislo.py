import random

# Program to guess a random number

# Function to start the guessing game
def guess_number():
    # Generate a random number between 1 and 100
    number = random.randint(1, 100)
    
    print("Welcome to the Guessing Game!")
    print("I have picked a number between 1 and 100. Try to guess it!")
    
    # Loop until the user guesses correctly
    attempts = 0
    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1
        
        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {number} in {attempts} attempts.")
            break

# Start the game
guess_number()