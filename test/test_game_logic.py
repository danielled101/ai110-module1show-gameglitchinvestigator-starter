from logic_utils import check_guess, update_score


# --- Bug 1: check_guess returned swapped hint messages ---
# Before fix: "Too High" said "Go HIGHER!" and "Too Low" said "Go LOWER!"

def test_winning_guess():
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_too_high_hint_says_lower():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message, f"Too High should say LOWER, got: {message!r}"

def test_too_low_hint_says_higher():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message, f"Too Low should say HIGHER, got: {message!r}"

def test_too_high_hint_does_not_say_higher():
    _, message = check_guess(99, 1)
    assert "HIGHER" not in message, f"Too High must not say HIGHER, got: {message!r}"

def test_too_low_hint_does_not_say_lower():
    _, message = check_guess(1, 99)
    assert "LOWER" not in message, f"Too Low must not say LOWER, got: {message!r}"


# --- Bug 2: attempts counter initialized to 1 instead of 0 ---
# Because attempts started at 1, the first guess was passed to update_score
# as attempt_number=2, awarding 70 points instead of the correct 80.

def test_win_on_first_attempt_scores_80():
    score = update_score(0, "Win", attempt_number=1)
    assert score == 80, f"First-attempt win should score 80, got {score}"

def test_win_on_second_attempt_scores_70():
    score = update_score(0, "Win", attempt_number=2)
    assert score == 70, f"Second-attempt win should score 70, got {score}"

def test_buggy_attempts_init_would_have_given_wrong_score():
    buggy_score = update_score(0, "Win", attempt_number=2)
    correct_score = update_score(0, "Win", attempt_number=1)
    assert correct_score > buggy_score, "First-attempt win should outscore second-attempt win"


# --- Bug 3: new game reset did not clear status or history ---
# This bug lives entirely in Streamlit session-state UI code and cannot be
# covered by a pure unit test. It requires an integration/UI test (e.g.
# Playwright or streamlit AppTest) to verify that pressing New Game resets
# status to "playing" and clears the history list.
