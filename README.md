# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [X] **Describe the game's purpose.**
  A Streamlit number-guessing game where the player selects a difficulty (Easy, Normal, or Hard), receives a range of possible numbers, and tries to guess the secret number within a limited number of attempts. After each guess the game gives a directional hint ("Go HIGHER" or "Go LOWER") and tracks a running score that decreases the longer it takes to win.

- [x] **Detail which bugs you found.**
  1. **Reversed hints** — guessing below the secret number showed "Go LOWER" and guessing above showed "Go HIGHER", the exact opposite of correct.
  2. **Off-by-one attempts** — `st.session_state.attempts` was initialized to `1` instead of `0`, so on Normal difficulty the player only received 7 guesses even though the UI advertised 8.
  3. **Broken New Game button** — clicking New Game did not reset `status` back to `"playing"`, so after a win or loss the game stayed locked on the end screen and the success banner never appeared.

- [x] **Explain what fixes you applied.**
  1. Swapped the return values in `check_guess()` so `"📉 Go LOWER!"` is returned when `guess > secret` and `"📈 Go HIGHER!"` when `guess < secret`.
  2. Changed the attempts initializer from `1` to `0` so attempt counting starts correctly and the full advertised number of guesses is available.
  3. Updated the New Game handler to reset `st.session_state.status` to `"playing"` and clear `history` before calling `st.rerun()`, and used a `show_new_game_msg` flag to display the success banner after the rerun completes.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User selects Normal difficulty and the game picks a secret number between 1 and 100
2. User enters a guess of 50 → game returns "📉 Go LOWER!"
3. User enters a guess of 25 → game returns "📈 Go HIGHER!"
4. User enters a guess of 37 → game returns "📈 Go HIGHER!"
5. User enters a guess of 44 → game returns "📉 Go LOWER!"
6. User enters a guess of 42 → game returns "🎉 Correct!" and displays the final score
7. Score updates correctly after each guess based on attempt number
8. User clicks New Game → attempts and score reset, a fresh secret number is chosen, and the game is immediately ready to play

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
 pytest test/test_game_logic.py
========================= 8 passed in 0.05s =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
