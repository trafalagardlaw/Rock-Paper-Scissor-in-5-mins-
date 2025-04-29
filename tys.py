import streamlit as st
import time

# Define lesson content
lessons = [
    "Welcome! Let's learn how to make a Rock Paper Scissors game in Python! 🎮",
    "Step 1: We'll use `import random` to get the computer's choice.",
    "Step 2: Use `input()` to get the player's choice.",
    "Step 3: Compare choices with `if`/`elif` statements to decide the winner.",
    "Step 4: Print the result and loop it to play again!"
]

quiz = {
    "question": "What module do we use to get the computer's choice?",
    "options": ["math", "random", "os"],
    "answer": "random"
}

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
            if st.button("🔁 Restart Game"):
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
    st.write(quiz["question"])
    choice = st.radio("Choose one:", quiz["options"])
    if st.button("Submit Answer"):
        if choice == quiz["answer"]:
            st.success("Correct! ✅ Now let's play the real game!")
            st.session_state.page += 1
            st.rerun()
        else:
            st.error("Oops! Try again.")

elif st.session_state.page == len(lessons) + 1:
    st.header("🎮 Let's Play Rock Paper Scissors!")

    if "player_score" not in st.session_state:
        st.session_state.player_score = 0
        st.session_state.computer_score = 0

    import random

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
