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

- **Game Purpose:**
   - Learn how to debug state management issues, logic errors, type coercion bugs, and configuration errors.
   - Refactor game logic from the UI in `app.py` into `logic_utils.py` and test these changes.

- **Bugs Found:**
   - State management bug: the `new_game` function doesn't properly initialize or preserve the secret number across button clicks.
   - `st.session_state.attempts` is reset to 0 instead of the secret being properly stored and maintained in `st.session_state.secret`.
   - The `check_guess` function has the hints reversed.
   - On even number attempts, the `secret` variable is cast to a string instead of staying as an integer.
   - The difficulty settings have the wrong range.

- **Fixes Applied:**
   - The "New Game" button now correctly resets attempts to 1 and generates a new secret within the selected difficulty range.
   - If `guess > secret`: returns "Too High" with message "📉 Go LOWER!" If `guess < secret`: returns "Too Low" with message "📈 Go HIGHER!"
   - The `check_guess` function now handles type mismatches gracefully:
      - Attempts numeric comparison first.
      - If a `TypeError` occurs (when the secret was incorrectly cast to string on even attempts), it falls back to string comparison.
      - This prevents the mixed-type comparison that was breaking hints.
   - `get_range_for_difficulty` now returns:
      - Easy: 1–20
      - Normal: 1–100
      - Hard: 1–200 (now genuinely harder—larger range than Normal).
   - Refactored all game logic to `logic_utils.py`.

## 📸 Demo

- ![screenshot.jpg] [Insert a screenshot of your fixed, winning game here]

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
