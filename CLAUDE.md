# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
python -m streamlit run app.py

# Run tests
pytest

# Run a single test
pytest tests/test_game_logic.py::test_winning_guess
```

## Project Overview

This is an intentionally buggy number-guessing game built with Streamlit, used as a debugging exercise. The assignment is to find and fix the bugs, then refactor logic into `logic_utils.py`.

## Architecture

- `app.py` — Streamlit UI and game state management using `st.session_state`. Contains duplicated logic functions that need to be moved to `logic_utils.py`.
- `logic_utils.py` — Target module for refactored game logic. Currently has stub functions that raise `NotImplementedError`.
- `tests/test_game_logic.py` — Pytest tests that import from `logic_utils` (not `app.py`). Tests expect `check_guess` to return just the outcome string (e.g. `"Win"`), not a tuple.

## Known Bugs (intentional, for the exercise)

1. **State bug**: `new_game` resets `st.session_state.attempts` to `0` instead of using `st.session_state.secret` properly; the secret number regeneration in `new_game` ignores the selected difficulty range.
2. **Hint logic bug**: `check_guess` in `app.py` swaps Higher/Lower — guessing too high says "Go HIGHER!" instead of "Go LOWER!".
3. **Type coercion bug**: On even attempts, `secret` is cast to `str`, causing string comparison instead of integer comparison, breaking hint logic further.
4. **Difficulty range bug**: "Hard" maps to range 1–50 but should be harder (larger range) than "Normal" (1–100).

## Refactoring Task

Move the four functions from `app.py` into `logic_utils.py`, then update `app.py` to import from `logic_utils`. The test file already imports `check_guess` from `logic_utils` and expects it to return only the outcome string (first element of the tuple), so the API signature may need adjustment or tests may need updating.
