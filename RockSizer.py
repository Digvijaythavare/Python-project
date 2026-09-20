import tkinter as tk
import random

# Main Window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x500")
root.resizable(False, False)

# Variables
user_score = 0
computer_score = 0

# Game Function
def play(user_choice):
    global user_score, computer_score

    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)

    user_label.config(text=f"You: {user_choice}")
    computer_label.config(text=f"Computer: {computer_choice}")

    if user_choice == computer_choice:
        result_label.config(text="It's a Draw!", fg="orange")

    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result_label.config(text="You Win! 🎉", fg="green")
        user_score += 1

    else:
        result_label.config(text="Computer Wins!", fg="red")
        computer_score += 1

    score_label.config(
        text=f"Score: You {user_score} - {computer_score} Computer"
    )

# Reset Function
def reset_game():
    global user_score, computer_score

    user_score = 0
    computer_score = 0

    user_label.config(text="You: ")
    computer_label.config(text="Computer: ")
    result_label.config(text="Choose your move!", fg="black")
    score_label.config(text="Score: You 0 - 0 Computer")


# Heading
title = tk.Label(
    root,
    text="ROCK PAPER SCISSORS",
    font=("Arial", 18, "bold")
)
title.pack(pady=20)

# Choice Buttons
rock_btn = tk.Button(
    root, text="🪨 Rock", width=15,
    font=("Arial", 12),
    command=lambda: play("Rock")
)
rock_btn.pack(pady=8)

paper_btn = tk.Button(
    root, text="📄 Paper", width=15,
    font=("Arial", 12),
    command=lambda: play("Paper")
)
paper_btn.pack(pady=8)

scissors_btn = tk.Button(
    root, text="✂️ Scissors", width=15,
    font=("Arial", 12),
    command=lambda: play("Scissors")
)
scissors_btn.pack(pady=8)

# Result Labels
user_label = tk.Label(root, text="You: ", font=("Arial", 12))
user_label.pack(pady=5)

computer_label = tk.Label(
    root, text="Computer: ", font=("Arial", 12)
)
computer_label.pack(pady=5)

result_label = tk.Label(
    root, text="Choose your move!",
    font=("Arial", 16, "bold")
)
result_label.pack(pady=15)

# Score
score_label = tk.Label(
    root, text="Score: You 0 - 0 Computer",
    font=("Arial", 12, "bold")
)
score_label.pack(pady=10)

# Reset Button
reset_btn = tk.Button(
    root, text="Reset Game",
    font=("Arial", 12),
    command=reset_game
)
reset_btn.pack(pady=10)

# Run Application
root.mainloop()