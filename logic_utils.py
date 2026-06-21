def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 50
    elif difficulty == "Normal":
        return 1, 100
    elif difficulty == "Hard":
        return 1, 200
    else:
        return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    try:
        guess = int(raw)
        return True, guess, None
    except ValueError:
        return False, None, "Please enter a valid number."


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).
    """
    if guess == secret:
        return "Win", "Correct!"
    elif guess > secret:
        return "Too High", "Guess LOWER"
    else:
        return "Too Low", "Guess HIGHER"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        return current_score + (90 - attempt_number * 10)

    return current_score