import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import random
import time
from PIL import Image, ImageTk
import os
import sys

class ColorfulRockPaperScissorsTeacher:
    def __init__(self, root):
        self.root = root
        self.root.title("🎮 Learn Python: Rock Paper Scissors in 5 Minutes 🎮")
        self.root.geometry("950x750")
        self.root.resizable(True, True)
        
        # Set vibrant color scheme
        self.colors = {
            "background": "#2e3440",   # Dark blue-gray
            "header": "#88c0d0",       # Light blue
            "accent1": "#8fbcbb",      # Teal
            "accent2": "#a3be8c",      # Light green
            "accent3": "#ebcb8b",      # Yellow
            "accent4": "#d08770",      # Orange
            "text": "#eceff4",         # Off-white
            "code_bg": "#3b4252",      # Darker blue-gray
            "button_hover": "#5e81ac"  # Bright blue
        }
        
        self.root.configure(bg=self.colors["background"])
        
        # Set app icon if available
        try:
            self.root.iconbitmap("python_icon.ico")
        except:
            pass
            
        # Configure styles
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Configure advanced styles
        self.configure_styles()
        
        # Game emojis for visual representation
        self.game_emojis = {
            "rock": "✊",
            "paper": "✋",
            "scissors": "✌️"
        }
        
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
        
        # Create main frame with colorful border
        self.main_frame = tk.Frame(self.root, bg=self.colors["accent1"], padx=5, pady=5)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Create inner frame with dark background
        self.inner_frame = tk.Frame(self.main_frame, bg=self.colors["background"], padx=15, pady=15)
        self.inner_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create header with progress bar and animation
        self.header_frame = tk.Frame(self.inner_frame, bg=self.colors["background"])
        self.header_frame.pack(fill=tk.X, pady=(0, 15))
        
        # Add colorful title
        self.title_label = tk.Label(self.header_frame, text="Python RPS 🎮", 
                                  font=("Comic Sans MS", 18, "bold"), 
                                  fg=self.colors["accent3"],
                                  bg=self.colors["background"])
        self.title_label.pack(side=tk.LEFT, padx=(0, 20))
        
        # Animated timer with colorful background
        self.timer_frame = tk.Frame(self.header_frame, bg=self.colors["accent4"], padx=8, pady=3, bd=0)
        self.timer_frame.pack(side=tk.RIGHT)
        
        self.timer_label = tk.Label(self.timer_frame, text="⏱️ 60s", 
                                  font=("Arial", 14, "bold"), 
                                  fg=self.colors["text"],
                                  bg=self.colors["accent4"])
        self.timer_label.pack()
        
        # Colorful progress bar
        self.progress_frame = tk.Frame(self.header_frame, bg=self.colors["background"], pady=5)
        self.progress_frame.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 20))
        
        self.progress = ttk.Progressbar(self.progress_frame, length=400, mode="determinate", 
                                      style="Colorful.Horizontal.TProgressbar")
        self.progress.pack(fill=tk.X, expand=True)
        
        # Create content frame
        self.content_frame = tk.Frame(self.inner_frame, bg=self.colors["background"])
        self.content_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create navigation frame with fancy buttons
        self.nav_frame = tk.Frame(self.inner_frame, bg=self.colors["background"], pady=10)
        self.nav_frame.pack(fill=tk.X, pady=(15, 0))
        
        self.prev_button = tk.Button(self.nav_frame, text="◀ Previous", 
                                   font=("Arial", 12, "bold"),
                                   bg=self.colors["accent1"],
                                   fg=self.colors["text"],
                                   activebackground=self.colors["button_hover"],
                                   activeforeground=self.colors["text"],
                                   padx=15, pady=5, bd=0,
                                   command=self.go_to_previous)
        self.prev_button.pack(side=tk.LEFT)
        
        self.next_button = tk.Button(self.nav_frame, text="Next ▶", 
                                   font=("Arial", 12, "bold"),
                                   bg=self.colors["accent1"],
                                   fg=self.colors["text"],
                                   activebackground=self.colors["button_hover"],
                                   activeforeground=self.colors["text"],
                                   padx=15, pady=5, bd=0,
                                   command=self.go_to_next)
        self.next_button.pack(side=tk.RIGHT)

        # Create fun footer with emoji
        self.footer_frame = tk.Frame(self.inner_frame, bg=self.colors["background"])
        self.footer_frame.pack(fill=tk.X, pady=(10, 0))
        
        self.footer_label = tk.Label(self.footer_frame, 
                                   text="🐍 Made with Python & Tkinter 🐍", 
                                   font=("Comic Sans MS", 10),
                                   fg=self.colors["accent2"],
                                   bg=self.colors["background"])
        self.footer_label.pack()
        
        # Create pages
        self.create_introduction_page()
        self.create_variables_page()
        self.create_game_logic_page()
        self.create_game_loop_page()
        self.create_quiz_page()
        
        # Show first page
        self.show_page(0)
        self.start_timer()
        
        # Button hover effects
        self.add_button_hover_effects()
        
    def configure_styles(self):
        # Configure custom styles with new colors
        self.style.configure('TFrame', background=self.colors["background"])
        self.style.configure('Header.TLabel', font=('Comic Sans MS', 24, 'bold'), 
                           foreground=self.colors["header"], background=self.colors["background"])
        self.style.configure('SubHeader.TLabel', font=('Comic Sans MS', 18), 
                           foreground=self.colors["accent3"], background=self.colors["background"])
        self.style.configure('Body.TLabel', font=('Arial', 12), 
                           foreground=self.colors["text"], background=self.colors["background"])
        self.style.configure('Code.TLabel', font=('Courier', 12), 
                           foreground=self.colors["accent3"], background=self.colors["code_bg"])
        
        # Configure colorful progressbar
        self.style.configure("Colorful.Horizontal.TProgressbar", 
                          troughcolor=self.colors["background"],
                          background=self.colors["accent2"],
                          thickness=15)
        
    def add_button_hover_effects(self):
        # Add hover effects to buttons
        def on_enter(e, button, bg_color):
            button['background'] = self.colors["button_hover"]
            
        def on_leave(e, button, bg_color):
            button['background'] = bg_color
            
        self.prev_button.bind("<Enter>", lambda e: on_enter(e, self.prev_button, self.colors["accent1"]))
        self.prev_button.bind("<Leave>", lambda e: on_leave(e, self.prev_button, self.colors["accent1"]))
        
        self.next_button.bind("<Enter>", lambda e: on_enter(e, self.next_button, self.colors["accent1"]))
        self.next_button.bind("<Leave>", lambda e: on_leave(e, self.next_button, self.colors["accent1"]))
        
    def create_introduction_page(self):
        page = tk.Frame(self.content_frame, bg=self.colors["background"])
        
        # Colorful title with emojis
        title_label = tk.Label(page, text="🎮 Learn Python: Rock Paper Scissors 🎮", 
                            font=("Comic Sans MS", 24, "bold"),
                            fg=self.colors["header"],
                            bg=self.colors["background"])
        title_label.pack(pady=(0, 20))
        
        # Create fun animation frame showing the game
        animation_frame = tk.Frame(page, bg=self.colors["background"])
        animation_frame.pack(pady=(0, 20))
        
        rock_label = tk.Label(animation_frame, text="✊", font=("Arial", 40), 
                           fg=self.colors["accent1"], bg=self.colors["background"])
        rock_label.pack(side=tk.LEFT, padx=15)
        
        paper_label = tk.Label(animation_frame, text="✋", font=("Arial", 40), 
                            fg=self.colors["accent2"], bg=self.colors["background"])
        paper_label.pack(side=tk.LEFT, padx=15)
        
        scissors_label = tk.Label(animation_frame, text="✌️", font=("Arial", 40), 
                               fg=self.colors["accent3"], bg=self.colors["background"])
        scissors_label.pack(side=tk.LEFT, padx=15)
        
        # Introduction text in a fancy frame
        intro_frame = tk.Frame(page, bg=self.colors["code_bg"], bd=2, relief="ridge", padx=15, pady=15)
        intro_frame.pack(fill=tk.X, pady=(0, 20))
        
        intro_text = """Welcome to our colorful 5-minute Python tutorial! By the end, you'll have built 
your own Rock Paper Scissors game while learning key programming concepts.

This tutorial is divided into 5 fun sections, each taking about 1 minute:

1️⃣ Introduction (You are here!)
2️⃣ Variables and User Input
3️⃣ Game Logic
4️⃣ Creating a Game Loop
5️⃣ Quiz and Play the Game

Rock Paper Scissors is an ideal first Python project because it teaches:
🔹 Variables and data types
🔹 User input and validation
🔹 Conditional logic
🔹 Random number generation
🔹 Functions and program structure"""

        intro_label = tk.Label(intro_frame, text=intro_text, font=("Arial", 12), 
                            fg=self.colors["text"], bg=self.colors["code_bg"], 
                            justify=tk.LEFT, padx=10, pady=10)
        intro_label.pack(anchor=tk.W)
        
        # Game rules in colorful boxes
        rules_label = tk.Label(page, text="Game Rules:", font=("Comic Sans MS", 18), 
                            fg=self.colors["accent3"], bg=self.colors["background"])
        rules_label.pack(anchor=tk.W, pady=(0, 10))
        
        rules_frame = tk.Frame(page, bg=self.colors["background"])
        rules_frame.pack(fill=tk.X)
        
        # Rule 1
        rule1_frame = tk.Frame(rules_frame, bg=self.colors["accent1"], padx=10, pady=10, bd=0)
        rule1_frame.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)
        rule1_text = f"{self.game_emojis['rock']} beats {self.game_emojis['scissors']}"
        rule1_label = tk.Label(rule1_frame, text=rule1_text, font=("Arial", 14, "bold"), 
                            fg=self.colors["text"], bg=self.colors["accent1"])
        rule1_label.pack()
        
        # Rule 2
        rule2_frame = tk.Frame(rules_frame, bg=self.colors["accent2"], padx=10, pady=10, bd=0)
        rule2_frame.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)
        rule2_text = f"{self.game_emojis['scissors']} beats {self.game_emojis['paper']}"
        rule2_label = tk.Label(rule2_frame, text=rule2_text, font=("Arial", 14, "bold"), 
                            fg=self.colors["text"], bg=self.colors["accent2"])
        rule2_label.pack()
        
        # Rule 3
        rule3_frame = tk.Frame(rules_frame, bg=self.colors["accent3"], padx=10, pady=10, bd=0)
        rule3_frame.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)
        rule3_text = f"{self.game_emojis['paper']} beats {self.game_emojis['rock']}"
        rule3_label = tk.Label(rule3_frame, text=rule3_text, font=("Arial", 14, "bold"), 
                            fg=self.colors["text"], bg=self.colors["accent3"])
        rule3_label.pack()
        
        self.pages.append(page)
        
    def create_variables_page(self):
        page = tk.Frame(self.content_frame, bg=self.colors["background"])
        
        # Title with emoji
        title_label = tk.Label(page, text="Step 1: Variables and User Input 📝", 
                            font=("Comic Sans MS", 24, "bold"),
                            fg=self.colors["header"],
                            bg=self.colors["background"])
        title_label.pack(pady=(0, 20))
        
        # Content in a colorful frame
        content_label = tk.Label(page, text="First, we need to set up our game variables:", 
                              font=("Comic Sans MS", 16),
                              fg=self.colors["accent3"],
                              bg=self.colors["background"])
        content_label.pack(anchor=tk.W)
        
        # Code frame with syntax highlighting effect 
        code_frame = tk.Frame(page, bg=self.colors["accent1"], padx=3, pady=3)
        code_frame.pack(fill=tk.X, pady=10)
        
        code_inner_frame = tk.Frame(code_frame, bg=self.colors["code_bg"], padx=15, pady=15)
        code_inner_frame.pack(fill=tk.X)
        
        code_text = """# Import the random module for computer choices
import random

# Game choices
choices = ['rock', 'paper', 'scissors']  # 🎮

# Score tracking
player_score = 0  # 👨‍💻
computer_score = 0  # 🖥️"""

        code_label = tk.Label(code_inner_frame, text=code_text, font=("Consolas", 12), 
                           fg=self.colors["text"], bg=self.colors["code_bg"], 
                           justify=tk.LEFT)
        code_label.pack(anchor=tk.W)
        
        # Second section
        content2_label = tk.Label(page, text="Next, we need to get the player's choice:", 
                               font=("Comic Sans MS", 16),
                               fg=self.colors["accent3"],
                               bg=self.colors["background"])
        content2_label.pack(anchor=tk.W, pady=(20, 10))
        
        # Second code frame with different accent color
        code_frame2 = tk.Frame(page, bg=self.colors["accent2"], padx=3, pady=3)
        code_frame2.pack(fill=tk.X, pady=10)
        
        code_inner_frame2 = tk.Frame(code_frame2, bg=self.colors["code_bg"], padx=15, pady=15)
        code_inner_frame2.pack(fill=tk.X)
        
        code_text2 = """# Get player input 🎮
player_choice = input("Choose rock, paper, or scissors: ").lower()

# Validate the input ✅
while player_choice not in choices:
    print("Invalid choice! Please try again.")
    player_choice = input("Choose rock, paper, or scissors: ").lower()

# Generate computer choice 🖥️
computer_choice = random.choice(choices)
print(f"Computer chose {computer_choice}")"""

        code_label2 = tk.Label(code_inner_frame2, text=code_text2, font=("Consolas", 12), 
                            fg=self.colors["text"], bg=self.colors["code_bg"], 
                            justify=tk.LEFT)
        code_label2.pack(anchor=tk.W)
        
        # Interactive element with colorful background
        interact_frame = tk.Frame(page, bg=self.colors["accent4"], padx=3, pady=3)
        interact_frame.pack(fill=tk.X, pady=(20, 10))
        
        interact_inner = tk.Frame(interact_frame, bg=self.colors["code_bg"], padx=15, pady=15)
        interact_inner.pack(fill=tk.X)
        
        question_label = tk.Label(interact_inner, text="🧩 Try it yourself! 🧩", 
                               font=("Comic Sans MS", 16, "bold"),
                               fg=self.colors["accent3"],
                               bg=self.colors["code_bg"])
        question_label.pack(anchor=tk.W, pady=(0, 10))
        
        question_text = tk.Label(interact_inner, text="What method converts user input to lowercase?", 
                              font=("Arial", 12),
                              fg=self.colors["text"],
                              bg=self.colors["code_bg"])
        question_text.pack(anchor=tk.W)
        
        self.input_var = tk.StringVar()
        
        input_frame = tk.Frame(interact_inner, bg=self.colors["code_bg"])
        input_frame.pack(fill=tk.X, pady=10)
        
        prefix_label = tk.Label(input_frame, text="input('text').", 
                             font=("Consolas", 12),
                             fg=self.colors["accent2"],
                             bg=self.colors["code_bg"])
        prefix_label.pack(side=tk.LEFT)
        
        answer_entry = tk.Entry(input_frame, textvariable=self.input_var, width=10, 
                             font=("Consolas", 12),
                             bg=self.colors["background"],
                             fg=self.colors["accent3"],
                             insertbackground=self.colors["accent3"])
        answer_entry.pack(side=tk.LEFT)
        
        suffix_label = tk.Label(input_frame, text="()", 
                             font=("Consolas", 12),
                             fg=self.colors["accent2"],
                             bg=self.colors["code_bg"])
        suffix_label.pack(side=tk.LEFT)
        
        # Colorful check button
        self.check_button = tk.Button(interact_inner, text="✅ Check Answer", 
                                   font=("Arial", 12, "bold"),
                                   bg=self.colors["accent2"],
                                   fg=self.colors["text"],
                                   activebackground=self.colors["button_hover"],
                                   activeforeground=self.colors["text"],
                                   padx=10, pady=5, bd=0,
                                   command=self.check_lowercase_answer)
        self.check_button.pack(anchor=tk.W)
        
        self.result_var = tk.StringVar()
        self.result_label = tk.Label(interact_inner, textvariable=self.result_var, 
                                  font=("Arial", 12, "bold"),
                                  fg=self.colors["accent3"],
                                  bg=self.colors["code_bg"])
        self.result_label.pack(anchor=tk.W, pady=10)
        
        self.pages.append(page)
        
    def create_game_logic_page(self):
        page = tk.Frame(self.content_frame, bg=self.colors["background"])
        
        # Title with emoji
        title_label = tk.Label(page, text="Step 2: Game Logic 🧠", 
                            font=("Comic Sans MS", 24, "bold"),
                            fg=self.colors["header"],
                            bg=self.colors["background"])
        title_label.pack(pady=(0, 20))
        
        # Content
        content_label = tk.Label(page, text="Now we need to determine the winner of each round:", 
                              font=("Comic Sans MS", 16),
                              fg=self.colors["accent3"],
                              bg=self.colors["background"])
        content_label.pack(anchor=tk.W)
        
        # Code frame with nice border
        code_frame = tk.Frame(page, bg=self.colors["accent1"], padx=3, pady=3)
        code_frame.pack(fill=tk.X, pady=10)
        
        code_inner_frame = tk.Frame(code_frame, bg=self.colors["code_bg"])
        code_inner_frame.pack(fill=tk.X)
        
        # Scrollable code area with colorful text
        code_text = """def determine_winner(player, computer):
    # Check for a tie 🤝
    if player == computer:
        return "It's a tie!"
        
    # Check all winning conditions for player 🏆
    elif (player == 'rock' and computer == 'scissors') or \\
         (player == 'paper' and computer == 'rock') or \\
         (player == 'scissors' and computer == 'paper'):
        return "You win!"
        
    # Otherwise, computer wins 💻
    else:
        return "Computer wins!"

# Use the function
result = determine_winner(player_choice, computer_choice)
print(result)

# Update scores 📊
if result == "You win!":
    player_score += 1
elif result == "Computer wins!":
    computer_score += 1

print(f"Score: Player {player_score} - Computer {computer_score}")"""

        code_text_widget = scrolledtext.ScrolledText(code_inner_frame, width=60, height=18, 
                                                  font=('Consolas', 12),
                                                  bg=self.colors["code_bg"],
                                                  fg=self.colors["text"],
                                                  insertbackground=self.colors["accent3"])
        code_text_widget.pack(fill=tk.BOTH)
        code_text_widget.insert(tk.END, code_text)
        code_text_widget.config(state=tk.DISABLED)
        
        # Add cute graphics showing game logic
        graphics_frame = tk.Frame(page, bg=self.colors["background"])
        graphics_frame.pack(fill=tk.X, pady=10)
        
        # Rock beats scissors
        r_beats_s = tk.Frame(graphics_frame, bg=self.colors["background"])
        r_beats_s.pack(side=tk.LEFT, expand=True)
        
        rock_label = tk.Label(r_beats_s, text="✊", font=("Arial", 30), 
                           fg=self.colors["accent1"], bg=self.colors["background"])
        rock_label.pack()
        
        beats_label1 = tk.Label(r_beats_s, text="beats", font=("Arial", 12), 
                             fg=self.colors["text"], bg=self.colors["background"])
        beats_label1.pack()
        
        scissors_label = tk.Label(r_beats_s, text="✌️", font=("Arial", 30), 
                               fg=self.colors["accent4"], bg=self.colors["background"])
        scissors_label.pack()
        
        # Scissors beats paper
        s_beats_p = tk.Frame(graphics_frame, bg=self.colors["background"])
        s_beats_p.pack(side=tk.LEFT, expand=True)
        
        scissors_label2 = tk.Label(s_beats_p, text="✌️", font=("Arial", 30), 
                                fg=self.colors["accent2"], bg=self.colors["background"])
        scissors_label2.pack()
        
        beats_label2 = tk.Label(s_beats_p, text="beats", font=("Arial", 12), 
                             fg=self.colors["text"], bg=self.colors["background"])
        beats_label2.pack()
        
        paper_label = tk.Label(s_beats_p, text="✋", font=("Arial", 30), 
                            fg=self.colors["accent4"], bg=self.colors["background"])
        paper_label.pack()
        
        # Paper beats rock
        p_beats_r = tk.Frame(graphics_frame, bg=self.colors["background"])
        p_beats_r.pack(side=tk.LEFT, expand=True)
        
        paper_label2 = tk.Label(p_beats_r, text="✋", font=("Arial", 30), 
                             fg=self.colors["accent3"], bg=self.colors["background"])
        paper_label2.pack()
        
        beats_label3 = tk.Label(p_beats_r, text="beats", font=("Arial", 12), 
                             fg=self.colors["text"], bg=self.colors["background"])
        beats_label3.pack()
        
        rock_label2 = tk.Label(p_beats_r, text="✊", font=("Arial", 30), 
                            fg=self.colors["accent4"], bg=self.colors["background"])
        rock_label2.pack()
        
        # Interactive element
        interact_frame = tk.Frame(page, bg=self.colors["accent3"], padx=3, pady=3)
        interact_frame.pack(fill=tk.X, pady=(10, 0))
        
        interact_inner = tk.Frame(interact_frame, bg=self.colors["code_bg"], padx=15, pady=15)
        interact_inner.pack(fill=tk.X)
        
        test_label = tk.Label(interact_inner, text="🧪 Test your understanding:", 
                           font=("Comic Sans MS", 16, "bold"),
                           fg=self.colors["accent3"],
                           bg=self.colors["code_bg"])
        test_label.pack(anchor=tk.W, pady=(0, 10))
        
        question_label = tk.Label(interact_inner, text="Which of these correctly checks if rock beats scissors?", 
                               font=("Arial", 12),
                               fg=self.colors["text"],
                               bg=self.colors["code_bg"])
        question_label.pack(anchor=tk.W)
        
        self.logic_var = tk.StringVar()
        
        # Colorful radio buttons
        radio_frame = tk.Frame(interact_inner, bg=self.colors["code_bg"], pady=10)
        radio_frame.pack(fill=tk.X)
        
        # Custom radio buttons with colors
        self.create_colorful_radio(radio_frame, "if player == 'rock' or computer == 'scissors':", 
                                "wrong1", self.logic_var, self.colors["accent1"])
        
        self.create_colorful_radio(radio_frame, "if player == 'rock' and computer == 'scissors':", 
                                "correct", self.logic_var, self.colors["accent2"])
        
        self.create_colorful_radio(radio_frame, "if player > computer:", 
                                "wrong2", self.logic_var, self.colors["accent3"])
        
        # Check button
        self.logic_check = tk.Button(interact_inner, text="🔍 Check Answer", 
                                  font=("Arial", 12, "bold"),
                                  bg=self.colors["accent2"],
                                  fg=self.colors["text"],
                                  activebackground=self.colors["button_hover"],
                                  activeforeground=self.colors["text"],
                                  padx=10, pady=5, bd=0,
                                  command=self.check_logic_answer)
        self.logic_check.pack(anchor=tk.W, pady=10)
        
        self.logic_result = tk.StringVar()
        self.logic_result_label = tk.Label(interact_inner, textvariable=self.logic_result, 
                                        font=("Arial", 12, "bold"),
                                        fg=self.colors["accent3"],
                                        bg=self.colors["code_bg"])
        self.logic_result_label.pack(anchor=tk.W)
        
        self.pages.append(page)
        
    def create_colorful_radio(self, parent, text, value, variable, color):
        """Create a custom colorful radio button"""
        frame = tk.Frame(parent, bg=self.colors["code_bg"], padx=5, pady=2)
        frame.pack(anchor=tk.W)
        
        radio = tk.Radiobutton(frame, text=text, variable=variable, value=value,
                           font=("Consolas", 12),
                           fg=color,
                           selectcolor=self.colors["background"],
                           bg=self.colors["code_bg"])
        radio.pack(anchor=tk.W)
        
    def create_game_loop_page(self):
        page = tk.Frame(self.content_frame, bg=self.colors["background"])
        
        # Title with emoji
        title_label = tk.Label(page, text="Step 3: Game Loop 🔄", 
                            font=("Comic Sans MS", 24, "bold"),
                            fg=self.colors["header"],
                            bg=self.colors["background"])
        title_label.pack(pady=(0, 20))
        
        # Content
        content_label = tk.Label(page, text="Let's create a loop so players can play multiple rounds:", 
                              font=("Comic Sans MS", 16),
                              fg=self.colors["accent3"],
                              bg=self.colors["background"])
        content_label.pack(anchor=tk.W)
        
        # Code frame with gradient-like effect
        code_frame = tk.Frame(page,