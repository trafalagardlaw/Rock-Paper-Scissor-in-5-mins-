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

# Ask for age at start
if "age_checked" not in st.session_state:
    st.title("Welcome to Mohammad Obaid's Rock Paper Scissor Tutorial in Under 5 Minutes! ( Beginners Variation )  🎉")
    age = st.number_input("How old are you?", min_value=1, max_value=120, step=1)
    if st.button("Start!"):
        if age < 12:
            st.error("Sorry buddy, these next parts are too hard for you right now :) Come back when you're a bit older!")
            st.stop()
        else:
            st.session_state.age_checked = True
            st.session_state.page = 0
            st.rerun()
    st.stop()

# Expanded lesson content with examples and coding exercises
lessons = [
    {"text": """Welcome! 🎉 Today you'll learn how to build a Rock Paper Scissors game in Python.

This game will teach you:
- User input with `input()`
- Making decisions using `if`, `elif`, and `else`
- Using randomness with `random.choice()`
- Storing and updating scores

👉 Python is a beginner-friendly programming language. It's used in data science, game development, and web development!

Each page will guide you step-by-step. You'll type real code and answer questions at the end!
""", "code": None},

    {"text": """📘 First, let's import the Python library we'll use for randomness.

This gives our game the ability to make choices like a real opponent!

👉 `import` brings in other code libraries.

Example:
```python
import random
```
""", "code": "import random"},

    {"text": """🧠 Now let's get input from the player!

👉 `input()` allows the user to type something.
👉 `player_choice` stores what they typed.

Example:
```python
player_choice = input("Enter rock, paper, or scissors: ")
```
""", "code": "player_choice = input(\"Enter rock, paper, or scissors: \")"},

    {"text": """🎲 Time for the computer to choose a move!

👉 `random.choice()` picks something randomly from a list.

Example:
```python
computer_choice = random.choice(["rock", "paper", "scissors"])
```
""", "code": "computer_choice = random.choice([\"rock\", \"paper\", \"scissors\"])"},

    {"text": """⚖️ Let's compare the two choices!

👉 `if`, `elif`, and `else` let you make decisions.
👉 Use `==` to compare values.
👉 Combine conditions with `and`.

Example:
```python
if player_choice == computer_choice:
    print("It's a tie!")
elif player_choice == 'rock' and computer_choice == 'scissors':
    print("You win!")
else:
    print("You lose.")
```
""", "code": "if player_choice == computer_choice:\n    print(\"It's a tie!\")\nelif player_choice == 'rock' and computer_choice == 'scissors':\n    print(\"You win!\")\nelse:\n    print(\"You lose.\")"},

    {"text": """🔁 Want to play again and again? Use a loop!

👉 `while True:` means repeat forever (until you `break` it).
👉 Use a score variable to keep track of wins!

Example:
```python
player_score = 0
computer_score = 0

while True:
    # Get choices
    # Compare and print results
    # Ask if player wants to stop
```
""", "code": "player_score = 0\ncomputer_score = 0\n\nwhile True:\n    # Get choices\n    # Compare and print results\n    # Ask if player wants to stop"},

    {"text": """🎨 Congrats! You've seen how to build a game.

This is just the beginning. You can keep adding features like:
- Emojis 🧡
- Backgrounds 🌈
- Sound effects 🔊
- Scores and stats 📊

Now it's quiz time to review!""", "code": None}
]

quiz = [
    {"question": "What does `input()` do in Python?", "options": ["Print text", "Get user input", "Store numbers"], "answer": "Get user input"},
    {"question": "Which keyword starts a decision in code?", "options": ["print", "if", "random"], "answer": "if"},
    {"question": "What module lets us make random choices?", "options": ["random", "math", "datetime"], "answer": "random"}
]

# Store player answers for feedback
if "answers" not in st.session_state:
    st.session_state.answers = []

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
                st.session_state.answers = []
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
    lesson = lessons[st.session_state.page]
    st.header(f"Lesson {st.session_state.page + 1}")
    st.markdown(lesson["text"])

    if lesson["code"]:
        user_code = st.text_area("Type the code example below:", height=150, key=f"code_{st.session_state.page}")
        if user_code.strip() == lesson["code"]:
            st.success("Correct! 🎉")
        else:
            st.info("Try matching the code exactly, including quotes and indentation.")

    if st.button("Next Page"):
        st.session_state.page += 1
        st.rerun()

elif st.session_state.page == len(lessons):
    st.header("📝 Quiz Time!")
    if "quiz_index" not in st.session_state:
        st.session_state.quiz_index = 0
        st.session_state.quiz_score = 0

    if st.session_state.quiz_index < len(quiz):
        q = quiz[st.session_state.quiz_index]
        st.write(q["question"])
        choice = st.radio("Choose one:", q["options"], key=f"quiz_q_{st.session_state.quiz_index}")

        if st.button("Submit Answer"):
            st.session_state.answers.append((q["question"], choice, q["answer"]))
            if choice == q["answer"]:
                st.session_state.quiz_score += 1
                st.success("Correct! ✅")
            else:
                st.error(f"Incorrect. The correct answer was '{q['answer']}'. ❌")

            st.session_state.quiz_index += 1
            st.rerun()
    else:
        st.success(f"Quiz completed! You got {st.session_state.quiz_score}/{len(quiz)} correct.")
        st.session_state.page += 1
        st.rerun()

elif st.session_state.page == len(lessons) + 1:
    st.header("📊 Quiz Summary")
    for idx, (question, user_ans, correct_ans) in enumerate(st.session_state.answers):
        if user_ans == correct_ans:
            st.markdown(f"**Q{idx+1}: {question}**\n- Your answer: ✅ {user_ans}")
        else:
            st.markdown(f"**Q{idx+1}: {question}**\n- Your answer: ❌ {user_ans}\n- Correct answer: ✅ {correct_ans}")

    if st.button("Continue to Game"):
        st.session_state.page += 1
        st.rerun()

elif st.session_state.page == len(lessons) + 2:
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
