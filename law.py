import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import random
import time
from PIL import Image, ImageTk
import os
import sys

class RockPaperScissorsTeacher:
    def __init__(self, root):
        self.root = root
        self.root.title("Learn Python: Rock Paper Scissors in 5 Minutes")
        self.root.geometry("900x700")
        self.root.resizable(True, True)
        self.root.configure(bg="#f0f0f0")
        
        # Set fullscreen mode
        self.root.attributes('-fullscreen', True)  # Add this line for fullscreen mode
        
        # Set app icon if available
        try:
            self.root.iconbitmap("python_icon.ico")
        except:
            pass
            
        # Apply theme
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure styles
        style.configure('TFrame', background='#f0f0f0')
        style.configure('Header.TLabel', font=('Arial', 24, 'bold'), background='#f0f0f0')
        style.configure('SubHeader.TLabel', font=('Arial', 18), background='#f0f0f0')
        style.configure('Body.TLabel', font=('Arial', 12), background='#f0f0f0')
        style.configure('Code.TLabel', font=('Courier', 12), background='#e8e8e8')
        style.configure('Timer.TLabel', font=('Arial', 14, 'bold'), foreground='#e74c3c', background='#f0f0f0')
        style.configure('Nav.TButton', font=('Arial', 12, 'bold'))
        style.configure('Game.TButton', font=('Arial', 14, 'bold'))
        
        # Variables
        self.current_page = 0
        self.pages = []
        self.time_remaining = 60
        self.timer_running = False
        self.timer_id = None
        
        # Game variables
        self.player_score = 0
        self.computer_score = 0
        self.quiz_score = 0
        
        # Create main frame
        self.main_frame = ttk.Frame(self.root, padding="20")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create header with progress bar
        self.header_frame = ttk.Frame(self.main_frame)
        self.header_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.timer_label = ttk.Label(self.header_frame, text="Time: 60s", style='Timer.TLabel')
        self.timer_label.pack(side=tk.RIGHT)
        
        self.progress = ttk.Progressbar(self.header_frame, length=400, mode="determinate")
        self.progress.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 20))
        
        # Create content frame
        self.content_frame = ttk.Frame(self.main_frame)
        self.content_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create navigation frame
        self.nav_frame = ttk.Frame(self.main_frame)
        self.nav_frame.pack(fill=tk.X, pady=(10, 0))
        
        self.prev_button = ttk.Button(self.nav_frame, text="Previous", style='Nav.TButton', command=self.go_to_previous)
        self.prev_button.pack(side=tk.LEFT)
        
        self.next_button = ttk.Button(self.nav_frame, text="Next", style='Nav.TButton', command=self.go_to_next)
        self.next_button.pack(side=tk.RIGHT)
        
        # Add exit button for fullscreen mode
        self.exit_button = ttk.Button(self.nav_frame, text="Exit Fullscreen (Esc)", style='Nav.TButton', 
                                    command=self.exit_fullscreen)
        self.exit_button.pack(side=tk.RIGHT, padx=10)
        
        # Bind Escape key to exit fullscreen
        self.root.bind("<Escape>", lambda event: self.exit_fullscreen())
        
        # Create pages
        self.create_introduction_page()
        self.create_variables_page()
        self.create_game_logic_page()
        self.create_game_loop_page()
        self.create_quiz_page()
        
        # Show first page
        self.show_page(0)
        self.start_timer()
    
    def exit_fullscreen(self):
        self.root.attributes('-fullscreen', False)
        self.root.geometry("900x700")
        
    def create_introduction_page(self):
        page = ttk.Frame(self.content_frame)
        
        # Title
        ttk.Label(page, text="Learn Python: Rock Paper Scissors", style='Header.TLabel').pack(pady=(0, 20))
        
        # Introduction text
        intro_text = """Welcome to our 5-minute Python tutorial! By the end, you'll have built 
your own Rock Paper Scissors game while learning key programming concepts.

This tutorial is divided into 5 sections, each taking about 1 minute:

1. Introduction (You are here!)
2. Variables and User Input
3. Game Logic
4. Creating a Game Loop
5. Quiz and Final Game

Rock Paper Scissors is an ideal first Python project because it teaches:
• Variables and data types
• User input and validation
• Conditional logic
• Random number generation
• Functions and program structure"""

        ttk.Label(page, text=intro_text, style='Body.TLabel', justify=tk.LEFT).pack(pady=(0, 20), anchor=tk.W)
        
        # Game rules
        ttk.Label(page, text="Game Rules:", style='SubHeader.TLabel').pack(anchor=tk.W)
        rules_text = """• Rock beats Scissors
• Scissors beats Paper
• Paper beats Rock"""
        ttk.Label(page, text=rules_text, style='Body.TLabel', justify=tk.LEFT).pack(pady=(0, 20), anchor=tk.W)
        
        self.pages.append(page)
        
    def create_variables_page(self):
        page = ttk.Frame(self.content_frame)
        
        # Title
        ttk.Label(page, text="Step 1: Variables and User Input", style='Header.TLabel').pack(pady=(0, 20))
        
        # Content
        ttk.Label(page, text="First, we need to set up our game variables:", style='SubHeader.TLabel').pack(anchor=tk.W)
        
        code_frame = ttk.Frame(page, padding=10)
        code_frame.pack(fill=tk.X, pady=10)
        code_frame.configure(style='Code.TLabel')
        
        code_text = """# Import the random module for computer choices
import random

# Game choices
choices = ['rock', 'paper', 'scissors']

# Score tracking
player_score = 0
computer_score = 0"""

        code_label = ttk.Label(code_frame, text=code_text, style='Code.TLabel', justify=tk.LEFT)
        code_label.pack(anchor=tk.W)
        
        ttk.Label(page, text="Next, we need to get the player's choice:", style='SubHeader.TLabel').pack(anchor=tk.W, pady=(20, 10))
        
        code_frame2 = ttk.Frame(page, padding=10)
        code_frame2.pack(fill=tk.X, pady=10)
        code_frame2.configure(style='Code.TLabel')
        
        code_text2 = """# Get player input
player_choice = input("Choose rock, paper, or scissors: ").lower()

# Validate the input
while player_choice not in choices:
    print("Invalid choice! Please try again.")
    player_choice = input("Choose rock, paper, or scissors: ").lower()

# Generate computer choice
computer_choice = random.choice(choices)
print(f"Computer chose {computer_choice}")"""

        code_label2 = ttk.Label(code_frame2, text=code_text2, style='Code.TLabel', justify=tk.LEFT)
        code_label2.pack(anchor=tk.W)
        
        # Interactive element
        ttk.Label(page, text="Try it yourself!", style='SubHeader.TLabel').pack(anchor=tk.W, pady=(20, 10))
        ttk.Label(page, text="What method converts user input to lowercase?", style='Body.TLabel').pack(anchor=tk.W)
        
        self.input_var = tk.StringVar()
        
        input_frame = ttk.Frame(page)
        input_frame.pack(fill=tk.X, pady=10)
        
        ttk.Label(input_frame, text="input('text').").pack(side=tk.LEFT)
        ttk.Entry(input_frame, textvariable=self.input_var, width=10).pack(side=tk.LEFT)
        ttk.Label(input_frame, text="()").pack(side=tk.LEFT)
        
        self.check_button = ttk.Button(page, text="Check Answer", command=self.check_lowercase_answer)
        self.check_button.pack(anchor=tk.W)
        
        self.result_var = tk.StringVar()
        self.result_label = ttk.Label(page, textvariable=self.result_var, style='Body.TLabel')
        self.result_label.pack(anchor=tk.W, pady=10)
        
        self.pages.append(page)
        
    def create_game_logic_page(self):
        page = ttk.Frame(self.content_frame)
        
        # Title
        ttk.Label(page, text="Step 2: Game Logic", style='Header.TLabel').pack(pady=(0, 20))
        
        # Content
        ttk.Label(page, text="Now we need to determine the winner of each round:", style='SubHeader.TLabel').pack(anchor=tk.W)
        
        code_frame = ttk.Frame(page, padding=10)
        code_frame.pack(fill=tk.X, pady=10)
        code_frame.configure(style='Code.TLabel')
        
        code_text = """def determine_winner(player, computer):
    # Check for a tie
    if player == computer:
        return "It's a tie!"
        
    # Check all winning conditions for player
    elif (player == 'rock' and computer == 'scissors') or \\
         (player == 'paper' and computer == 'rock') or \\
         (player == 'scissors' and computer == 'paper'):
        return "You win!"
        
    # Otherwise, computer wins
    else:
        return "Computer wins!"

# Use the function
result = determine_winner(player_choice, computer_choice)
print(result)

# Update scores
if result == "You win!":
    player_score += 1
elif result == "Computer wins!":
    computer_score += 1

print(f"Score: Player {player_score} - Computer {computer_score}")"""

        code_label = ttk.Label(code_frame, text=code_text, style='Code.TLabel', justify=tk.LEFT)
        code_label.pack(anchor=tk.W)
        
        # Interactive element
        ttk.Label(page, text="Test your understanding:", style='SubHeader.TLabel').pack(anchor=tk.W, pady=(20, 10))
        ttk.Label(page, text="Which of these correctly checks if rock beats scissors?", style='Body.TLabel').pack(anchor=tk.W)
        
        self.logic_var = tk.StringVar()
        
        ttk.Radiobutton(page, text="if player == 'rock' or computer == 'scissors':", 
                        variable=self.logic_var, value="wrong1").pack(anchor=tk.W)
        ttk.Radiobutton(page, text="if player == 'rock' and computer == 'scissors':", 
                        variable=self.logic_var, value="correct").pack(anchor=tk.W)
        ttk.Radiobutton(page, text="if player > computer:", 
                        variable=self.logic_var, value="wrong2").pack(anchor=tk.W)
        
        self.logic_check = ttk.Button(page, text="Check Answer", command=self.check_logic_answer)
        self.logic_check.pack(anchor=tk.W, pady=10)
        
        self.logic_result = tk.StringVar()
        ttk.Label(page, textvariable=self.logic_result, style='Body.TLabel').pack(anchor=tk.W)
        
        self.pages.append(page)
        
    def create_game_loop_page(self):
        page = ttk.Frame(self.content_frame)
        
        # Title
        ttk.Label(page, text="Step 3: Game Loop", style='Header.TLabel').pack(pady=(0, 20))
        
        # Content
        ttk.Label(page, text="Let's create a loop so players can play multiple rounds:", style='SubHeader.TLabel').pack(anchor=tk.W)
        
        code_frame = ttk.Frame(page, padding=10)
        code_frame.pack(fill=tk.X, pady=10)
        code_frame.configure(style='Code.TLabel')
        
        code_text = """def play_game():
    player_score = 0
    computer_score = 0
    
    while True:
        print("\\n===== ROCK PAPER SCISSORS =====")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Quit")
        print(f"Score: Player {player_score} - Computer {computer_score}")
        
        choice = input("\\nEnter your choice (1-4): ")
        
        # Handle quit option
        if choice == "4":
            print("Thanks for playing!")
            break
            
        # Convert choice to rock/paper/scissors
        if choice == "1":
            player_choice = "rock"
        elif choice == "2":
            player_choice = "paper"
        elif choice == "3":
            player_choice = "scissors"
        else:
            print("Invalid choice, please try again.")
            continue
            
        print(f"You chose {player_choice}")
        
        # Get computer choice and determine winner
        computer_choice = random.choice(choices)
        print(f"Computer chose {computer_choice}")
        
        result = determine_winner(player_choice, computer_choice)
        print(result)
        
        # Update scores
        if result == "You win!":
            player_score += 1
        elif result == "Computer wins!":
            computer_score += 1
            
        print(f"Score: Player {player_score} - Computer {computer_score}")

# Run the game
if __name__ == "__main__":
    play_game()"""

        code_text_widget = scrolledtext.ScrolledText(code_frame, width=60, height=20, font=('Courier', 12))
        code_text_widget.insert(tk.END, code_text)
        code_text_widget.config(state=tk.DISABLED)
        code_text_widget.pack(fill=tk.BOTH)
        
        # Interactive element
        ttk.Label(page, text="What statement exits the game loop?", style='SubHeader.TLabel').pack(anchor=tk.W, pady=(20, 10))
        
        self.loop_var = tk.StringVar()
        
        ttk.Radiobutton(page, text="exit()", variable=self.loop_var, value="wrong1").pack(anchor=tk.W)
        ttk.Radiobutton(page, text="return", variable=self.loop_var, value="wrong2").pack(anchor=tk.W)
        ttk.Radiobutton(page, text="break", variable=self.loop_var, value="correct").pack(anchor=tk.W)
        ttk.Radiobutton(page, text="continue", variable=self.loop_var, value="wrong3").pack(anchor=tk.W)
        
        self.loop_check = ttk.Button(page, text="Check Answer", command=self.check_loop_answer)
        self.loop_check.pack(anchor=tk.W, pady=10)
        
        self.loop_result = tk.StringVar()
        ttk.Label(page, textvariable=self.loop_result, style='Body.TLabel').pack(anchor=tk.W)
        
        self.pages.append(page)
        
    def create_quiz_page(self):
        page = ttk.Frame(self.content_frame)
        
        # Create notebook with tabs for quiz and game
        notebook = ttk.Notebook(page)
        notebook.pack(fill=tk.BOTH, expand=True)
        
        # Quiz tab
        quiz_frame = ttk.Frame(notebook)
        notebook.add(quiz_frame, text="Knowledge Quiz")
        
        ttk.Label(quiz_frame, text="Test Your Python Knowledge", style='Header.TLabel').pack(pady=(10, 20))
        
        # Quiz questions
        ttk.Label(quiz_frame, text="1. What Python function gets user input?", style='SubHeader.TLabel').pack(anchor=tk.W)
        
        self.q1_var = tk.StringVar()
        ttk.Radiobutton(quiz_frame, text="get_input()", variable=self.q1_var, value="wrong1").pack(anchor=tk.W)
        ttk.Radiobutton(quiz_frame, text="input()", variable=self.q1_var, value="correct").pack(anchor=tk.W)
        ttk.Radiobutton(quiz_frame, text="read()", variable=self.q1_var, value="wrong2").pack(anchor=tk.W)
        
        ttk.Label(quiz_frame, text="2. How do you generate a random choice from a list?", style='SubHeader.TLabel').pack(anchor=tk.W, pady=(20, 0))
        
        self.q2_var = tk.StringVar()
        ttk.Radiobutton(quiz_frame, text="list.random()", variable=self.q2_var, value="wrong1").pack(anchor=tk.W)
        ttk.Radiobutton(quiz_frame, text="random.select(list)", variable=self.q2_var, value="wrong2").pack(anchor=tk.W)
        ttk.Radiobutton(quiz_frame, text="random.choice(list)", variable=self.q2_var, value="correct").pack(anchor=tk.W)
        
        ttk.Label(quiz_frame, text="3. What's the correct way to check if two variables are equal?", style='SubHeader.TLabel').pack(anchor=tk.W, pady=(20, 0))
        
        self.q3_var = tk.StringVar()
        ttk.Radiobutton(quiz_frame, text="if a = b:", variable=self.q3_var, value="wrong1").pack(anchor=tk.W)
        ttk.Radiobutton(quiz_frame, text="if a == b:", variable=self.q3_var, value="correct").pack(anchor=tk.W)
        ttk.Radiobutton(quiz_frame, text="if a equals b:", variable=self.q3_var, value="wrong2").pack(anchor=tk.W)
        
        self.quiz_button = ttk.Button(quiz_frame, text="Submit Quiz", command=self.check_quiz)
        self.quiz_button.pack(pady=20)
        
        self.quiz_result = tk.StringVar()
        ttk.Label(quiz_frame, textvariable=self.quiz_result, style='Body.TLabel').pack()
        
        # Game tab
        game_frame = ttk.Frame(notebook)
        notebook.add(game_frame, text="Play the Game")
        
        ttk.Label(game_frame, text="Rock Paper Scissors Game", style='Header.TLabel').pack(pady=(10, 20))
        
        # Game instructions
        ttk.Label(game_frame, text="Make your choice:", style='SubHeader.TLabel').pack()
        
        # Game buttons frame
        buttons_frame = ttk.Frame(game_frame)
        buttons_frame.pack(pady=20)
        
        # Create game buttons
        rock_button = ttk.Button(buttons_frame, text="Rock", style='Game.TButton', 
                                 command=lambda: self.play_round("rock"))
        rock_button.pack(side=tk.LEFT, padx=10)
        
        paper_button = ttk.Button(buttons_frame, text="Paper", style='Game.TButton', 
                                  command=lambda: self.play_round("paper"))
        paper_button.pack(side=tk.LEFT, padx=10)
        
        scissors_button = ttk.Button(buttons_frame, text="Scissors", style='Game.TButton', 
                                     command=lambda: self.play_round("scissors"))
        scissors_button.pack(side=tk.LEFT, padx=10)
        
        # Display frame
        self.display_frame = ttk.Frame(game_frame)
        self.display_frame.pack(fill=tk.BOTH, expand=True, pady=20)
        
        # Player choice
        self.player_choice_var = tk.StringVar(value="Your choice: ")
        ttk.Label(self.display_frame, textvariable=self.player_choice_var, style='Body.TLabel').pack()
        
        # Computer choice
        self.computer_choice_var = tk.StringVar(value="Computer choice: ")
        ttk.Label(self.display_frame, textvariable=self.computer_choice_var, style='Body.TLabel').pack()
        
        # Result
        self.game_result_var = tk.StringVar(value="Result: ")
        ttk.Label(self.display_frame, textvariable=self.game_result_var, style='SubHeader.TLabel').pack(pady=10)
        
        # Score
        self.score_var = tk.StringVar(value="Score: Player 0 - Computer 0")
        ttk.Label(self.display_frame, textvariable=self.score_var, style='Body.TLabel').pack()
        
        # Reset button
        reset_button = ttk.Button(game_frame, text="Reset Score", command=self.reset_game)
        reset_button.pack(pady=10)
        
        self.pages.append(page)
    
    def check_lowercase_answer(self):
        answer = self.input_var.get().strip().lower()
        if answer == "lower":
            self.result_var.set("✓ Correct! .lower() converts the string to lowercase.")
        else:
            self.result_var.set("✗ Incorrect. The correct answer is 'lower'.")
    
    def check_logic_answer(self):
        answer = self.logic_var.get()
        if answer == "correct":
            self.logic_result.set("✓ Correct! We check if the player chose rock AND the computer chose scissors.")
        else:
            self.logic_result.set("✗ Incorrect. We need to check both conditions with AND.")
    
    def check_loop_answer(self):
        answer = self.loop_var.get()
        if answer == "correct":
            self.loop_result.set("✓ Correct! The 'break' statement exits the current loop.")
        else:
            self.loop_result.set("✗ Incorrect. The 'break' statement is used to exit loops.")
    
    def check_quiz(self):
        score = 0
        if self.q1_var.get() == "correct":
            score += 1
        if self.q2_var.get() == "correct":
            score += 1
        if self.q3_var.get() == "correct":
            score += 1
            
        self.quiz_score = score
        self.quiz_result.set(f"You scored {score}/3 on the quiz!")
        
        if score == 3:
            messagebox.showinfo("Quiz Complete", "Perfect score! You've mastered the basics of Python Rock Paper Scissors!")
        elif score >= 1:
            messagebox.showinfo("Quiz Complete", f"You scored {score}/3. Good job!")
        else:
            messagebox.showinfo("Quiz Complete", "You scored 0/3. Review the tutorial and try again!")
    
    def play_round(self, player_choice):
        # Get computer choice
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        
        # Determine winner
        if player_choice == computer_choice:
            result = "It's a tie!"
        elif ((player_choice == 'rock' and computer_choice == 'scissors') or
              (player_choice == 'paper' and computer_choice == 'rock') or
              (player_choice == 'scissors' and computer_choice == 'paper')):
            result = "You win!"
            self.player_score += 1
        else:
            result = "Computer wins!"
            self.computer_score += 1
        
        # Update display
        self.player_choice_var.set(f"Your choice: {player_choice}")
        self.computer_choice_var.set(f"Computer choice: {computer_choice}")
        self.game_result_var.set(f"Result: {result}")
        self.score_var.set(f"Score: Player {self.player_score} - Computer {self.computer_score}")
    
    def reset_game(self):
        self.player_score = 0
        self.computer_score = 0
        self.player_choice_var.set("Your choice: ")
        self.computer_choice_var.set("Computer choice: ")
        self.game_result_var.set("Result: ")
        self.score_var.set("Score: Player 0 - Computer 0")
    
    def start_timer(self):
        self.time_remaining = 60
        self.timer_running = True
        self.update_timer()
    
    def update_timer(self):
        if self.timer_running and self.time_remaining > 0:
            self.time_remaining -= 1
            self.timer_label.config(text=f"Time: {self.time_remaining}s")
            self.timer_id = self.root.after(1000, self.update_timer)
        elif self.timer_running and self.time_remaining <= 0:
            self.timer_label.config(text="Time: 0s")
            if self.current_page < len(self.pages) - 1:
                self.go_to_next()
    
    def reset_timer(self):
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
        self.start_timer()
    
    def show_page(self, index):
        # Hide all pages
        for page in self.pages:
            page.pack_forget()
        
        # Show selected page
        self.pages[index].pack(fill=tk.BOTH, expand=True)
        self.current_page = index
        
        # Update progress bar
        progress_value = (index / (len(self.pages) - 1)) * 100
        self.progress["value"] = progress_value
        
        # Update button states
        self.prev_button["state"] = "normal" if index > 0 else "disabled"
        if index == len(self.pages) - 1:
            self.next_button["state"] = "disabled"
        else:
            self.next_button["state"] = "normal"
    
    def go_to_next(self):
        if self.current_page < len(self.pages) - 1:
            self.show_page(self.current_page + 1)
            self.reset_timer()
    
    def go_to_previous(self):
        if self.current_page > 0:
            self.show_page(self.current_page - 1)
            self.reset_timer()

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsTeacher(root)
    root.mainloop()