import tkinter as tk
from tkinter import messagebox
import random

# Function to determine the winner
def determine_winner(user_choice):
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'paper' and computer_choice == 'rock') or
        (user_choice == 'scissors' and computer_choice == 'paper')
    ):
        result = "You win!"
    else:
        result = "Computer wins!"

    messagebox.showinfo("Result", f"Computer chose {computer_choice}. {result}")

# Function to handle button click
def button_click(choice):
    determine_winner(choice)

# Create the main window
window = tk.Tk()
window.title("Rock Paper Scissors")

# Create buttons for user choices
rock_button = tk.Button(window, text="Rock", command=lambda: button_click('rock'))
rock_button.pack()

paper_button = tk.Button(window, text="Paper", command=lambda: button_click('paper'))
paper_button.pack()

scissors_button = tk.Button(window, text="Scissors", command=lambda: button_click('scissors'))
scissors_button.pack()

# Start the main event loop
window.mainloop()