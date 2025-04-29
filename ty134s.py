import streamlit as st
import time
import random
import base64

# Sound effect loader (optional, if supported by browser)
def load_sound(file_path):
    with open(file_path, "rb") as sound_file:
        data = sound_file.read()
        b64 = base64.b64encode(data).decode()
        return f"data:audio/wav;base64,{b64}"

# Define lesson content (expanded)
lessons = [
    "Welcome! 🎉 Today you'll learn how to build a Rock Paper Scissors game in Python. Let's dive in!",
    "📘 First, import necessary libraries. We use `import random` to get random choices for the computer.",
    "🧠 Next, use `input()` to get user input. This lets the player type rock, paper, or scissors.",
    "⚖️ Use `if`, `elif`, and `else` to compare the player's choice with the computer's. Decide who wins!",
    "🔁 Wrap it in a loop to let players play multiple rounds, and use a score counter to track wins!",
    "🎨 You can even add emojis, colors, or sound effects to make the game more exciting!"
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

    if elapsed > 60:
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
    st.write(lessons[st.session_state.page])
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
            sound = "tie.wav"
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper"):
            st.session_state.player_score += 1
            result = "You win! ✅"
            sound = "win.wav"
        else:
            st.session_state.computer_score += 1
            result = "Computer wins! ❌"
            sound = "lose.wav"

        st.success(result)

        # Optional sound effect
        st.audio(load_sound(sound), format="audio/wav")

    if st.button("Reset Scores"):
        st.session_state.player_score = 0
        st.session_state.computer_score = 0
        st.rerun()
