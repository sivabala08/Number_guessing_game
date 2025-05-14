import random

# Function to get a valid integer input
def get_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

# Function to get valid lower and upper bounds
def get_bounds():
    while True:
        lower = get_integer("Enter the lower bound: ")
        upper = get_integer("Enter the upper bound: ")
        if lower < upper:
            return lower, upper
        else:
            print("Lower bound must be less than upper bound. Try again.")

# Main game function
def play_game():
    print("Welcome to the Number Guessing Game!")

    # Get range from user
    lower, upper = get_bounds()

    # Generate a random number in the given range
    secret_number = random.randint(lower, upper)

    # Set a fixed number of attempts (e.g., 5)
    attempts = 5

    print(f"\nGuess the number between {lower} and {upper}. You have {attempts} attempts.")

    for attempt in range(1, attempts + 1):
        guess = get_integer(f"Attempt {attempt}: Your guess: ")

        if guess < lower or guess > upper:
            print("Your guess is out of range.")
        elif guess == secret_number:
            print(f"Congratulations! You guessed the number in {attempt} attempts.")
            break
        elif guess < secret_number:
            print("Too low.")
        else:
            print("Too high.")
    else:
        print(f"Game over! The number was {secret_number}.")

# Run the game
if __name__ == "__main__":
    play_game()
