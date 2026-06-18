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

- The app picks a secret number, the player submits guesses, and the game responds with feedback (whether to guess higher or lower) and tracks score
- **Bug 1:** Enter key didn't submit the guess; submitting felt like it took two steps.
Typing a guess and pressing Enter would commit the text input and trigger a rerun, but it would not trigger the separate Submit Guess button. As a result, the guess wasn't processed until the button was clicked separately. **FIX:** Wrapped the text input and submit button inside an st.form, using st.form_submit_button instead of a st.button. Inside a form, pressing Enter in a text input automatically triggers the form's submit button, so Enter and clicking now behave identically and the guess is processed in a single step. 
- **Bug 2:** Higher/lower feedback was reversed. When guessing above the secret number, the game would say "Go higher" instead of "Go lower" **FIX:** Corrected the outcome-to-message mapping so "higher" and "lower" feedback matches the actual comparison result. Also removed the code that alternated comparing the secret number as a string versus a number based on whether the attempt count was even or odd, so the secret is now consistently compared as a number on every attempt.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User enters a guess of 40 and presses Enter
2. Game returns "Too Low" and guess is logged
3. User enters a guess of 70 → "Too High"
4. Score updates correctly after each guess
5. Game ends after the correct guess

## 🧪 Test Results

```
================================================================== test session starts ==================================================================
platform win32 -- Python 3.13.13, pytest-9.0.3, pluggy-1.6.0
rootdir: C:\Users\Owner\ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.13.0
collected 3 items                                                                                                                                        

tests\test_game_logic.py ...                                                                                                                       [100%]

=================================================================== 3 passed in 0.10s ===================================================================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
