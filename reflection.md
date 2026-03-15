# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  The game had a settings page on the sidebar to adjust difficulty. The game has developer debug info which contains the secret number. You can enter your guess in a box and and there are buttons to submit your guess, start a new game, and a checkmark box to show hints on the bottom.
- List at least two concrete bugs you noticed at the start
  (for example: "the secret number kept changing" or "the hints were backwards").
  The game had a smaller range from 1-50 for hard difficulty than a larger range from 1-100 for normal difficulty.
  The hints were backward.
  Clicking on new game gives the wrong message that says you already won.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used Copilot and Claude on this project.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
The AI suggested to change the backward hint messages like changing  "Too High", "📈 Go HIGHER!" to "Too High", "📉 Go LOWER!" inside the check_guess function and I verified the result by generating tests in tests/test_game_logic.py in agent mode.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
I had an error running pytest after creating tests/test_game_logic.py and I pasted my terminal's error message into a new chat session. It read the error message and saw errors in the tests generated. I pasted the message below: "I can see the real problem: tests 1-3 expect check_guess to return just an outcome string, but the current implementation returns a tuple (outcome, message)." Thus, I asked it to update the test_game_logic.py and rerun the tests again to verify that they all pass.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I generated pytest cases and then verified myself through streamlit on the browser testing the game.
- Describe at least one test you ran (manual or using pytest)
  and what it showed you about your code.
  I used pytest to verify the get_range_for_difficulty function and it showed me how to verify each range's output and what the original bug was.
- Did AI help you design or understand any tests? How?
 AI helped me design the tests by generating them for me and telling me what they do and what they return.
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Streamlit reruns happen automatically by looking at user interactions and triggers the entire script to rerun from the beginning. Session state is like the app's short-term memory for a specific user session.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
