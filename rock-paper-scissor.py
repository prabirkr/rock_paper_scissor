import tkinter as tk
from tkinter import messagebox, font
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
window.geometry("400x300")  # Set window size

# Create a custom font
custom_font = font.Font(size=20)

# Create buttons for user choices
rock_button = tk.Button(window, text="Rock", command=lambda: button_click('rock'), font=custom_font)
rock_button.grid(row=0, column=0, padx=10, pady=10)

paper_button = tk.Button(window, text="Paper", command=lambda: button_click('paper'), font=custom_font)
paper_button.grid(row=0, column=1, padx=10, pady=10)

scissors_button = tk.Button(window, text="Scissors", command=lambda: button_click('scissors'), font=custom_font)
scissors_button.grid(row=0, column=2, padx=10, pady=10)

# Start the main event loop
window.mainloop()
