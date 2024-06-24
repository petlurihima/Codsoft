import tkinter as tk
import random
from tkinter import messagebox

def play_game():
    user_choice = user_input.get()
    if user_choice not in ['r', 'p', 's']:
        messagebox.showerror("Input Error", "Please select 'r' for rock, 'p' for paper, or 's' for scissors.")
        return

    computer_choice = random.choice(['r', 'p', 's'])
    if user_choice == computer_choice:
        result = "Both are tied"
    elif (user_choice == 'r' and computer_choice == 's') or \
         (user_choice == 'p' and computer_choice == 'r') or \
         (user_choice == 's' and computer_choice == 'p'):
        result = "Congrats, you won"
    else:
        result = "Sorry, you lost"

    result_label.config(text=f"Your choice: {user_choice}, Computer's choice: {computer_choice}\nResult: {result}")

def reset_game():
    user_input.set("")
    result_label.config(text="")

# Creating the main window
root = tk.Tk()
root.title("Rock Paper Scissors Game")

# Creating and placing the widgets
tk.Label(root, text="Select 'r' for rock, 'p' for paper, 's' for scissors:").grid(row=0, column=0, columnspan=2)

user_input = tk.StringVar()
entry_user = tk.Entry(root, textvariable=user_input)
entry_user.grid(row=1, column=0, columnspan=2)

play_button = tk.Button(root, text="Play", command=play_game)
play_button.grid(row=2, column=0)

reset_button = tk.Button(root, text="Reset", command=reset_game)
reset_button.grid(row=2, column=1)

result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2)

# Starting the main event loop
root.mainloop()