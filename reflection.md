# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
    - The hints were backwards. For example, I guessed 58 when the secret number was 71, and the game told me to "Go LOWER"
    - The "New Game" does not reload the page/restart the game properly
    - The game says 8 attempts allowed but only gives the user 7 attempts

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

|    Input     | Expected Behavior  | Actual Behavior | Console Output / Error |
|--------------|-------------------|-----------------|------------------------|
|Guess of 58 when the secret number was 71 | The game should display "Too Low" or "Go Higher" because 58 is less than 71 | The game displayed "Go Lower" even though the guess was below the secret number | None |

|Clicked "New Game" after finishing a round | The game should restart with a new secret number, reset score, and reset attempts |The game did not restart or reload properly | None|

|Made 7 guesses on Normal difficulty | If the game says "Attempts Allowed: 8", the player should receive 8 attempts before the game ends | The game ended after 7 attempts even though it claimed 8 attempts were allowed | None |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? 

I used both Claude and ChatGPT during this project. I primarily used Claude inside VS Code to help identify and fix bugs in the game code. I also used ChatGPT to help me understand pytest errors, implement the functions in logic_utils.py, and interpret the test results.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

One example of a correct AI suggestion came from Claude. Claude helped identify several bugs in the game, including the reversed high/low hints, the incorrect number of attempts, and issues with the New Game functionality. Claude also helped refactor the game logic from app.py into logic_utils.py. I verified these suggestions by running the game, testing the behavior manually, and running python -m pytest after making the changes.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

One example of an incorrect or misleading AI suggestion also came from Claude. When pytest produced a ModuleNotFoundError for logic_utils.py, Claude suggested creating a conftest.py file to modify the Python path. However, the actual problem was that the functions inside logic_utils.py still contained NotImplementedError and had not been implemented yet. I used ChatGPT to help investigate the test failures, implemented the missing functions, and verified the solution by running python -m pytest, which eventually resulted in all 8 tests passing.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

I decided a bug was fixed by both manually testing the game and running automated tests with pytest. For example, I tested the hint system by entering guesses that were above and below the secret number. If the hints matched the guesses correctly, I knew the bug had been fixed.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

One test I ran was python -m pytest. Initially, the tests failed because the functions in logic_utils.py still contained NotImplementedError. After implementing the functions, most of the tests passed, but two tests still failed because the messages did not contain the expected words "LOWER" and "HIGHER" in uppercase. After updating the messages, all 8 tests passed successfully.

- Did AI help you design or understand any tests? How?

AI helped me understand and debug the tests. Claude helped identify some of the original game bugs and assisted with refactoring the code into logic_utils.py. ChatGPT helped me understand the pytest error messages, implement the missing functions, and interpret the failed tests. The AI suggestions helped me design and verify the tests, but I confirmed the final results by running the game and executing python -m pytest.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
