import random
import math

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Enter a valid integer.")

def get_bounds():
    while True:
        a = get_int("Enter Lower Bound (A): ")
        b = get_int("Enter Upper Bound (B): ")
        if a < b:
            return a, b
        print("A must be less than B.")

def get_difficulty():
    levels = {"easy": 0, "medium": 1, "hard": 2}
    while True:
        level = input("Choose difficulty (Easy/Medium/Hard): ").lower()
        if level in levels:
            return levels[level]
        print("Invalid choice.")

def hint_message(guess, number):
    diff = abs(guess - number)
    if diff <= 5:
        return "Very close!"
    elif diff <= 10:
        return "Close!"
    else:
        return "Far away!"

def play_game():
    a, b = get_bounds()
    number = random.randint(a, b)
    max_tries = math.ceil(math.log2(b - a + 1))
    difficulty = get_difficulty()
    hint = input("Enable hint mode? (y/n): ").lower() == "y"

    tries = 0
    prev_guesses = set()

    print("\nGuess the number between", a, "and", b, ". You have", max_tries, "attempts.")

    while tries < max_tries:
        try:
            guess = int(input("Your guess: "))
        except ValueError:
            print("Invalid input.")
            if difficulty > 0:
                tries += difficulty
            continue

        if guess == number:
            print("Correct! You guessed it in", tries + 1, "trials")
            return

        if guess < a or guess > b:
            print("Out of range!")
            tries += difficulty
        elif guess in prev_guesses:
            print("You already guessed that!")
            tries += 1
        else:
            tries += 1
            if hint:
                print(hint_message(guess, number))
            prev_guesses.add(guess)

    print(" Game Over! The number was ." ,number)

if __name__ == "__main__":
    play_game()
