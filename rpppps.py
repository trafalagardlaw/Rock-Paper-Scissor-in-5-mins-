import tkinter as tk
import random

class GameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Rock Paper Scissors Game")
        self.root.geometry("800x700")
        
        # Set up colors
        self.colors = {
            "background": "#f0f0f0",
            "header": "#2c3e50",
            "text": "#ffffff",
            "accent1": "#3498db",
            "accent2": "#e74c3c",
            "accent3": "#2ecc71",
            "accent4": "#9b59b6",
            "code_bg": "#ffffff",
            "button_hover": "#16a085"
        }
        
        # Set up game variables
        self.game_emojis = {
            "rock": "👊",
            "paper": "✋",
            "scissors": "✌️"
        }
        
        self.player_score = 0
        self.computer_score = 0
        self.quiz_score = 0
        
        # Set up main container
        self.main_frame = tk.Frame(root, bg=self.colors["background"])
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Content frame to hold pages
        self.content_frame = tk.Frame(self.main_frame, bg=self.colors["background"])
        self.content_frame.pack(fill=tk.BOTH, expand=True)
        
        # Setup pages
        self.pages = []
        self.create_quiz_page()
        
        # Show the quiz page
        self.show_page(0)
    
    def show_page(self, index):
        # Hide all pages
        for page in self.pages:
            page.pack_forget()
        
        # Show the selected page
        if 0 <= index < len(self.pages):
            self.pages[index].pack(fill=tk.BOTH, expand=True)
    
    def create_colorful_radio(self, parent, text, value, variable, fg_color):
        radio = tk.Radiobutton(
            parent,
            text=text,
            variable=variable,
            value=value,
            font=("Arial", 12),
            fg=self.colors["accent2"],
            bg=self.colors["code_bg"],
            selectcolor=self.colors["code_bg"]
        )
        radio.pack(anchor=tk.W)
        return radio
    
    def check_loop_answer(self):
        if self.loop_var.get() == "correct":
            self.loop_result.set("✅ Correct! 'break' exits the current loop.")
            self.quiz_score += 1
        else:
            self.loop_result.set("❌ Try again! The correct answer is 'break'.")

    def create_quiz_page(self):
        page = tk.Frame(self.content_frame, bg=self.colors["background"])
        
        # Title with emoji
        title_label = tk.Label(page, text="Final Step: Quiz & Play! 🎯", 
                            font=("Comic Sans MS", 24, "bold"),
                            fg=self.colors["header"],
                            bg=self.colors["background"])
        title_label.pack(pady=(0, 20))
        
        # Quiz intro
        quiz_label = tk.Label(page, text="Test your Python knowledge with a quick quiz:", 
                           font=("Comic Sans MS", 16),
                           fg=self.colors["accent3"],
                           bg=self.colors["background"])
        quiz_label.pack(anchor=tk.W, pady=(0, 10))
        
        # Create quiz frame
        quiz_frame = tk.Frame(page, bg=self.colors["accent1"], padx=3, pady=3)
        quiz_frame.pack(fill=tk.X, pady=10)
        
        quiz_inner = tk.Frame(quiz_frame, bg=self.colors["code_bg"], padx=15, pady=15)
        quiz_inner.pack(fill=tk.X)
        
        # Quiz questions
        q1_label = tk.Label(quiz_inner, text="1. Which Python function generates a random choice?", 
                         font=("Arial", 12, "bold"),
                         fg=self.colors["accent2"],
                         bg=self.colors["code_bg"])
        q1_label.pack(anchor=tk.W, pady=(0, 5))
        
        self.q1_var = tk.StringVar()
        
        q1_frame = tk.Frame(quiz_inner, bg=self.colors["code_bg"], pady=5)
        q1_frame.pack(fill=tk.X)
        
        self.create_colorful_radio(q1_frame, "random.select()", "wrong1", self.q1_var, self.colors["text"])
        self.create_colorful_radio(q1_frame, "random.choice()", "correct", self.q1_var, self.colors["text"])
        self.create_colorful_radio(q1_frame, "random.pick()", "wrong2", self.q1_var, self.colors["text"])
        
        # Question 2
        q2_label = tk.Label(quiz_inner, text="2. How do you convert user input to lowercase?", 
                         font=("Arial", 12, "bold"),
                         fg=self.colors["accent2"],
                         bg=self.colors["code_bg"])
        q2_label.pack(anchor=tk.W, pady=(10, 5))
        
        self.q2_var = tk.StringVar()
        
        q2_frame = tk.Frame(quiz_inner, bg=self.colors["code_bg"], pady=5)
        q2_frame.pack(fill=tk.X)
        
        self.create_colorful_radio(q2_frame, "input.lowercase()", "wrong1", self.q2_var, self.colors["text"])
        self.create_colorful_radio(q2_frame, "lowercase(input)", "wrong2", self.q2_var, self.colors["text"])
        self.create_colorful_radio(q2_frame, "input.lower()", "correct", self.q2_var, self.colors["text"])
        
        # Question 3
        q3_label = tk.Label(quiz_inner, text="3. How do you end a game loop?", 
                         font=("Arial", 12, "bold"),
                         fg=self.colors["accent2"],
                         bg=self.colors["code_bg"])
        q3_label.pack(anchor=tk.W, pady=(10, 5))
        
        self.q3_var = tk.StringVar()
        
        q3_frame = tk.Frame(quiz_inner, bg=self.colors["code_bg"], pady=5)
        q3_frame.pack(fill=tk.X)
        
        self.create_colorful_radio(q3_frame, "exit()", "wrong1", self.q3_var, self.colors["text"])
        self.create_colorful_radio(q3_frame, "break", "correct", self.q3_var, self.colors["text"])
        self.create_colorful_radio(q3_frame, "stop", "wrong2", self.q3_var, self.colors["text"])
        
        # Submit quiz button
        self.quiz_button = tk.Button(quiz_inner, text="📝 Submit Quiz", 
                                  font=("Arial", 12, "bold"),
                                  bg=self.colors["accent3"],
                                  fg=self.colors["text"],
                                  activebackground=self.colors["button_hover"],
                                  activeforeground=self.colors["text"],
                                  padx=10, pady=5, bd=0,
                                  command=self.check_quiz)
        self.quiz_button.pack(anchor=tk.W, pady=10)
        
        # Results display
        self.quiz_result = tk.StringVar()
        self.quiz_result_label = tk.Label(quiz_inner, textvariable=self.quiz_result, 
                                       font=("Arial", 12, "bold"),
                                       fg=self.colors["accent3"],
                                       bg=self.colors["code_bg"])
        self.quiz_result_label.pack(anchor=tk.W)
        
        # Play game frame
        play_frame = tk.Frame(page, bg=self.colors["accent2"], padx=3, pady=3)
        play_frame.pack(fill=tk.X, pady=(20, 10))
        
        play_inner = tk.Frame(play_frame, bg=self.colors["code_bg"], padx=15, pady=15)
        play_inner.pack(fill=tk.X)
        
        play_label = tk.Label(play_inner, text="🎮 Let's Play Rock Paper Scissors! 🎮", 
                           font=("Comic Sans MS", 18, "bold"),
                           fg=self.colors["accent3"],
                           bg=self.colors["code_bg"])
        play_label.pack(pady=(0, 10))
        
        # Game buttons with emojis
        buttons_frame = tk.Frame(play_inner, bg=self.colors["code_bg"])
        buttons_frame.pack(pady=10)
        
        rock_button = tk.Button(buttons_frame, text=f"{self.game_emojis['rock']} Rock", 
                             font=("Arial", 16, "bold"),
                             bg=self.colors["accent1"],
                             fg=self.colors["text"],
                             activebackground=self.colors["button_hover"],
                             activeforeground=self.colors["text"],
                             padx=20, pady=10, bd=0,
                             command=lambda: self.play_round("rock"))
        rock_button.pack(side=tk.LEFT, padx=10)
        
        paper_button = tk.Button(buttons_frame, text=f"{self.game_emojis['paper']} Paper", 
                              font=("Arial", 16, "bold"),
                              bg=self.colors["accent2"],
                              fg=self.colors["text"],
                              activebackground=self.colors["button_hover"],
                              activeforeground=self.colors["text"],
                              padx=20, pady=10, bd=0,
                              command=lambda: self.play_round("paper"))
        paper_button.pack(side=tk.LEFT, padx=10)
        
        scissors_button = tk.Button(buttons_frame, text=f"{self.game_emojis['scissors']} Scissors", 
                                 font=("Arial", 16, "bold"),
                                 bg=self.colors["accent3"],
                                 fg=self.colors["text"],
                                 activebackground=self.colors["button_hover"],
                                 activeforeground=self.colors["text"],
                                 padx=20, pady=10, bd=0,
                                 command=lambda: self.play_round("scissors"))
        scissors_button.pack(side=tk.LEFT, padx=10)
        
        # Game results display
        self.game_result_var = tk.StringVar()
        self.game_result_var.set("Make your choice to start playing!")
        
        self.game_result_label = tk.Label(play_inner, textvariable=self.game_result_var, 
                                        font=("Arial", 14),
                                        fg=self.colors["text"],
                                        bg=self.colors["code_bg"])
        self.game_result_label.pack(pady=10)
        
        # Score display
        score_frame = tk.Frame(play_inner, bg=self.colors["code_bg"])
        score_frame.pack(fill=tk.X, pady=10)
        
        # Player score
        player_frame = tk.Frame(score_frame, bg=self.colors["accent1"], padx=10, pady=10)
        player_frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        
        player_label = tk.Label(player_frame, text="Player", 
                             font=("Arial", 14, "bold"),
                             fg=self.colors["text"],
                             bg=self.colors["accent1"])
        player_label.pack()
        
        self.player_score_var = tk.StringVar()
        self.player_score_var.set("0")
        
        player_score_label = tk.Label(player_frame, textvariable=self.player_score_var, 
                                   font=("Arial", 24, "bold"),
                                   fg=self.colors["text"],
                                   bg=self.colors["accent1"])
        player_score_label.pack()
        
        # Computer score
        computer_frame = tk.Frame(score_frame, bg=self.colors["accent4"], padx=10, pady=10)
        computer_frame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)
        
        computer_label = tk.Label(computer_frame, text="Computer", 
                               font=("Arial", 14, "bold"),
                               fg=self.colors["text"],
                               bg=self.colors["accent4"])
        computer_label.pack()
        
        self.computer_score_var = tk.StringVar()
        self.computer_score_var.set("0")
        
        computer_score_label = tk.Label(computer_frame, textvariable=self.computer_score_var, 
                                     font=("Arial", 24, "bold"),
                                     fg=self.colors["text"],
                                     bg=self.colors["accent4"])
        computer_score_label.pack()
        
        self.pages.append(page)

    def check_quiz(self):
        score = 0
        if self.q1_var.get() == "correct":
            score += 1
        if self.q2_var.get() == "correct":
            score += 1
        if self.q3_var.get() == "correct":
            score += 1
            
        self.quiz_score = score
        self.quiz_result.set(f"Your score: {score}/3 {self.get_score_emoji(score, 3)}")

    def get_score_emoji(self, score, total):
        percentage = (score / total) * 100
        if percentage >= 80:
            return "🌟"
        elif percentage >= 60:
            return "👍"
        else:
            return "🔄"

    def check_lowercase_answer(self):
        if self.input_var.get().lower() == "lower":
            self.result_var.set("✅ Correct! input().lower() converts to lowercase.")
            self.quiz_score += 1
        else:
            self.result_var.set("❌ Try again! The answer is 'lower'.")

    def check_logic_answer(self):
        if self.logic_var.get() == "correct":
            self.logic_result.set("✅ Correct! This is the right condition.")
            self.quiz_score += 1
        else:
            self.logic_result.set("❌ Try again! The correct answer is the second option.")

    def play_round(self, player_choice):
        # Generate computer choice
        computer_choice = random.choice(list(self.game_emojis.keys()))
        
        # Determine winner
        result = self.determine_winner(player_choice, computer_choice)
        
        # Update scores
        if result == "You win!":
            self.player_score += 1
        elif result == "Computer wins!":
            self.computer_score += 1
            
        # Update display
        self.player_score_var.set(str(self.player_score))
        self.computer_score_var.set(str(self.computer_score))
        
        # Show result
        self.game_result_var.set(f"You chose {self.game_emojis[player_choice]} vs Computer's {self.game_emojis[computer_choice]}\n{result}")

    def determine_winner(self, player, computer):
        # Check for a tie
        if player == computer:
            return "It's a tie!"
            
        # Check all winning conditions for player
        elif (player == 'rock' and computer == 'scissors') or \
             (player == 'paper' and computer == 'rock') or \
             (player == 'scissors' and computer == 'paper'):
            return "You win!"
            
        # Otherwise, computer wins
        else:
            return "Computer wins!"

# Main application entry point
if __name__ == "__main__":
    root = tk.Tk()
    app = GameApp(root)
    root.mainloop()