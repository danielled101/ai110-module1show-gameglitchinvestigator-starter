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
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
