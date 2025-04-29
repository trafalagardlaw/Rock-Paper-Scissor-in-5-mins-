import streamlit as st
import time
import random

# Custom background - Sky Theme
page_bg_img = '''
<style>
body {
background-image: linear-gradient(to right, #89f7fe 0%, #66a6ff 100%);
background-attachment: fixed;
background-size: cover;
font-family: 'Comic Sans MS', cursive, sans-serif;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

# Expanded lesson content with examples
lessons = [
    """Welcome! 🎉 Today you'll learn how to build a Rock Paper Scissors game in Python.

This game will teach you user input, control flow, loops, and randomness — core skills in any coding journey!
Let's dive in!""",

    """📘 First, let's import the Python library we'll use for randomness.

```python
import random
```
This gives our game the ability to make choices like a real opponent!""",

    """🧠 Next, we ask the user for a move using `input()`:

```python
player_choice = input("Enter rock, paper, or scissors: ")
```
We store the player's move in a variable for later use.""",

    """🎲 The computer can make a choice using `random.choice()`:

```python
computer_choice = random.choice(["rock", "paper", "scissors"])
```
This picks one of the three options at random each time the game runs!""",

    """⚖️ Then we compare choices using conditions!

```python
if player_choice == computer_choice:
    print("It's a tie!")
elif player_choice == "rock" and computer_choice == "scissors":
    print("You win!")
else:
    print("You lose.")
```

This logic handles all game outcomes.""",

    """🔁 To make it replayable, use a loop and track the scores:

```python
player_score = 0
computer_score = 0

while True:
    # Get choices
    # Compare choices
    # Update and show scores
    # Break if player wants to quit
```

This creates a real game experience!""",

    """🎨 Bonus: Add visuals and sounds! Use emojis in output or sound effects using libraries like `pygame` or Streamlit’s `st.audio()`.

Now you're ready to build and play your own game!"""
]

quiz = [
    {
        "question": "Which module do we use to generate the computer's choice?",
        "options": ["math", "random", "os"],
        "answer": "random"
    },
    {
        "question": "Which Python statement lets us compare conditions?",
        "options": ["for", "if", "import"],
        "answer": "if"
    },
    {
        "question": "Which function is used to get user input in the terminal?",
        "options": ["print()", "input()", "get()"],
        "answer": "input()"
    }
]

def page_timer(page_idx):
    if f"start_time_{page_idx}" not in st.session_state:
        st.session_state[f"start_time_{page_idx}"] = time.time()

    elapsed = time.time() - st.session_state[f"start_time_{page_idx}"]
    remaining = max(0, 60 - int(elapsed))
    st.write(f"⏳ Time remaining on this page: {remaining}s")

    if remaining <= 0:
        st.warning("⏰ Time's up for this page!")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🔁 Restart Lesson"):
                st.session_state.page = 0
                for i in range(len(lessons)):
                    st.session_state.pop(f"start_time_{i}", None)
                st.rerun()
        with col2:
            if st.button("➡️ Go to Next Page"):
                st.session_state.page += 1
                st.rerun()
        st.stop()

# Initialize session state
if "page" not in st.session_state:
    st.session_state.page = 0

st.title("🧠 Learn to Code: Rock Paper Scissors")

if st.session_state.page < len(lessons):
    page_timer(st.session_state.page)
    st.header(f"Lesson {st.session_state.page + 1}")
    st.markdown(lessons[st.session_state.page])
    if st.button("Next Page"):
        st.session_state.page += 1
        st.rerun()

elif st.session_state.page == len(lessons):
    st.header("📝 Quiz Time!")
    if "quiz_index" not in st.session_state:
        st.session_state.quiz_index = 0
        st.session_state.quiz_score = 0

    q = quiz[st.session_state.quiz_index]
    st.write(q["question"])
    choice = st.radio("Choose one:", q["options"], key=f"quiz_q_{st.session_state.quiz_index}")

    if st.button("Submit Answer"):
        if choice == q["answer"]:
            st.session_state.quiz_score += 1
            st.success("Correct! ✅")
        else:
            st.error("Oops! That's incorrect. ❌")

        st.session_state.quiz_index += 1
        if st.session_state.quiz_index >= len(quiz):
            st.success(f"Quiz completed! You got {st.session_state.quiz_score}/{len(quiz)} correct.")
            st.balloons()
            st.session_state.page += 1
        st.rerun()

elif st.session_state.page == len(lessons) + 1:
    st.header("🎮 Let's Play Rock Paper Scissors!")

    if "player_score" not in st.session_state:
        st.session_state.player_score = 0
        st.session_state.computer_score = 0

    st.write(f"**Player**: {st.session_state.player_score} | **Computer**: {st.session_state.computer_score}")

    choices = ["rock", "paper", "scissors"]
    emojis = {"rock": "👊", "paper": "✋", "scissors": "✌️"}
    player_choice = st.radio("Choose your move:", choices, format_func=lambda x: f"{emojis[x]} {x.title()}")

    if st.button("Play!"):
        computer_choice = random.choice(choices)
        st.write(f"You chose {emojis[player_choice]} | Computer chose {emojis[computer_choice]}")

        result = ""
        if player_choice == computer_choice:
            result = "It's a tie! 🤝"
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper"):
            st.session_state.player_score += 1
            result = "You win! ✅"
        else:
            st.session_state.computer_score += 1
            result = "Computer wins! ❌"

        st.success(result)

    if st.button("Reset Scores"):
        st.session_state.player_score = 0
        st.session_state.computer_score = 0
        st.rerun()
