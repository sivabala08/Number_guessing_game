Number Guessing Game (Python)
The player selects a valid range, and the system randomly chooses a number within that range.
The player must guess the number within a limited number of attempts.

Features
- User-defined number range (e.g., 1 to 100)
- Random number generation using `random` module
- Guess validation (no strings, no out-of-range values)
- Limited number of attempts based on `ceil(log2(B - A + 1))`
- Feedback for each guess (Too high, Too low, Correct)
- Tracks invalid guesses and repeated guesses
- Optional: Hint mode (distance-based feedback)
- Optional: Leaderboard tracking (name, result, attempts)

How It Works
1. User inputs a lower and upper bound (A < B).
2. System generates a number `X` between [A, B].
3. Allowed guesses = `ceil(log2(B - A + 1))`
4. Player tries to guess `X` within allowed attempts.

Language
Python 3

How to Run
```bash python number_guessing_game.py
