# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it? First issue I noticed was the the enter button did not submit the guess like it said it would, I had to click on the submit guess button. As I was playing the game it kept telling me to go higher until I guessed 100 which at that point it told me to go lower even though I had guessed 99 just before. New Game button does not work.
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
    - Some issue with enter button, doesn't submit guess. Seems like you have to click the submit guess button twice, one for hint and once to log into history, before you can guess again
    - Doesn't correct rank numbers (guess was 97, asked to go higher, secret number was 14..), seems like it is flipped.
    - New game button does not reset game
    - Difficulty doesn't change anything

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| 50    |  LOWER            |  HIGHER         |  none                  | 
| 70    |  LOWER            |  HIGHER         |  none                  | 
| 30    |  HIGHER           |  LOWER          |  none                  | 
| 35    |  HIGHER           |  LOWER          |  none                  | 
| 35    |  HIGHER           |  LOWER          |  none                  | 
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? Claude
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result). One of the bugs I found was with the submit button/enter. The functions worked as two seperate features when it seems like there were supposed to be one. Claude explained that the root of the issue had to do with the Streamlit and sessions states. When a guess is submitted, the way the starter code was set up, you would have to press Enter then hit Submit because Streamlit commits the value first the reruns the script to finally submit the guess. Claude wrapped both functions into one form so that it collapsed the two-step behavior into one.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result). It didn't really give me anything misleading or inccorrect but I did notice when I was fixing the hint bug it missed that in the code, when a guess was too high, it was occassionally award points instead of deduct them.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed? I read through the code any it seemed like it made sense so I tested and it worked.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code. I had to manuelly test the Enter/Submit bug because there isn't a way to test that through pytest and it worked which showed me that the bug was fixed
- Did AI help you design or understand any tests? How? It designed the tests for the hint bug.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit? Streamlit reruns the entire file every time you interect with the page and state helps store values that you would want to keep during the reruns. 

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects? Before I turn to AI I will try to figure how to solve the bug on my own. And when asking AI for help I need to be very speficic is what I need help with and what I want done.
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task? I think before working with AI to solve bug I will make sure I have a good understanding of the entire project because I kept getting lost when it would solve bugs
- In one or two sentences, describe how this project changed the way you think about AI generated code. I think it is very helpful but I also think it is good to understand what is going on. AI should be used as a crutch not a wheelchair.
