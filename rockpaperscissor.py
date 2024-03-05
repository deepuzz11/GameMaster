import tkinter as tk
from tkinter import messagebox
import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!", 0
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!", 1
    else:
        return "Computer wins!", -1

def play_game(user_choice):
    global user_score, computer_score
    computer_choice = get_computer_choice()
    result, score = determine_winner(user_choice, computer_choice)
    result_label.config(text=result)
    user_score += score
    computer_score -= score
    user_score_label.config(text=f"Your Score: {user_score}")
    computer_score_label.config(text=f"Computer's Score: {computer_score}")

def rock_clicked():
    play_game('rock')

def paper_clicked():
    play_game('paper')

def scissors_clicked():
    play_game('scissors')

def back_to_home():
    home_frame.tkraise()

def play_again():
    play_frame.tkraise()

def start_game():
    global player_name, game_level
    player_name = name_entry.get()
    game_level = level_var.get()
    name_entry.delete(0, tk.END)
    name_frame.tkraise()

def play():
    name_frame.lower()
    play_frame.tkraise()

def show_name():
    player_name_label.config(text=f"Player Name: {player_name}")
    game_level_label.config(text=f"Game Level: {game_level.capitalize()}")
    play_frame.tkraise()

user_score = 0
computer_score = 0
player_name = ""
game_level = ""

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x300")

# Colors
bg_color = "#F3CFC6"  # Light Peach
button_bg = "#e75480"  # Pink
button_fg = "black"
font = ("Helvetica", 14)

# Create frames
home_frame = tk.Frame(root, bg=bg_color)
name_frame = tk.Frame(root, bg=bg_color)
play_frame = tk.Frame(root, bg=bg_color)
score_frame = tk.Frame(root, bg=bg_color)

# Define widgets for the home frame
tk.Label(home_frame, text="Welcome to Rock Paper Scissors", font=("Helvetica", 18), bg=bg_color).pack(pady=10)
tk.Button(home_frame, text="Start Game", command=start_game, bg=button_bg, fg=button_fg, font=font).pack(pady=5)

# Define widgets for the name frame
name_label = tk.Label(name_frame, text="Enter Your Name:", font=("Helvetica", 14), bg=bg_color)
name_label.pack(pady=10)
name_entry = tk.Entry(name_frame, font=("Helvetica", 12))
name_entry.pack(pady=5)
level_label = tk.Label(name_frame, text="Select Game Level:", font=("Helvetica", 14), bg=bg_color)
level_label.pack(pady=10)
level_var = tk.StringVar()
level_var.set("easy")
level_menu = tk.OptionMenu(name_frame, level_var, "easy", "medium", "hard")
level_menu.pack(pady=5)
start_button = tk.Button(name_frame, text="Start", command=play, bg=button_bg, fg=button_fg, font=font)
start_button.pack(pady=5)

# Define widgets for the play frame
tk.Label(play_frame, text="Choose Your Move", font=("Helvetica", 18), bg=bg_color).pack(pady=10)
tk.Button(play_frame, text="Rock", command=rock_clicked, font=font, bg=button_bg, fg=button_fg).pack(pady=5)
tk.Button(play_frame, text="Paper", command=paper_clicked, font=font, bg=button_bg, fg=button_fg).pack(pady=5)
tk.Button(play_frame, text="Scissors", command=scissors_clicked, font=font, bg=button_bg, fg=button_fg).pack(pady=5)
result_label = tk.Label(play_frame, text="", font=("Helvetica", 18), bg=bg_color)
result_label.pack(pady=10)
user_score_label = tk.Label(play_frame, text="Your Score: 0", font=font, bg=bg_color)
user_score_label.pack()
computer_score_label = tk.Label(play_frame, text="Computer's Score: 0", font=font, bg=bg_color)
computer_score_label.pack()
back_button = tk.Button(play_frame, text="Back", command=back_to_home, font=font, bg=button_bg, fg=button_fg, width=10, height=2)
back_button.pack(pady=10)

# Define widgets for the score frame
total_score_label = tk.Label(score_frame, text="", font=("Helvetica", 18), bg=bg_color)
total_score_label.pack(pady=10)
back_to_play_button = tk.Button(score_frame, text="Back to Play", command=play_again, font=font, bg=button_bg, fg=button_fg)
back_to_play_button.pack(pady=10)

# Define widgets for the name frame
player_name_label = tk.Label(name_frame, text="", font=("Helvetica", 14), bg=bg_color)
player_name_label.pack(pady=10)
game_level_label = tk.Label(name_frame, text="", font=("Helvetica", 14), bg=bg_color)
game_level_label.pack(pady=10)

# Place frames in the root window
home_frame.pack(fill="both", expand=True)
name_frame.pack(fill="both", expand=True)
play_frame.pack(fill="both", expand=True)
score_frame.pack(fill="both", expand=True)

# Hide name, play, and score frames initially
name_frame.place(x=0, y=0, width=400, height=300)
name_frame.lower()

play_frame.place(x=0, y=0, width=400, height=300)
play_frame.lower()

score_frame.place(x=0, y=0, width=400, height=300)
score_frame.lower()

root.mainloop()
