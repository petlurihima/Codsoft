import tkinter as tk
from tkinter import messagebox
import random

def generate_password():
    try:
        num = int(entry_num.get())
        sym = int(entry_sym.get())
        letters = int(entry_letters.get())
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for all fields.")
        return
    
    if num < 0 or sym < 0 or letters < 0:
        messagebox.showerror("Input Error", "Please enter positive numbers for all fields.")
        return
    
    char = [
        'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
        'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
    ]
    symbols = ['[',']','(',')','{','}','+','?','-','*','/','@','&']
    numbers = ['1','2','3','4','5','6','7','8','9','0']
    
    password_list = []
    for _ in range(letters):
        password_list.append(random.choice(char))
    for _ in range(sym):
        password_list.append(random.choice(symbols))
    for _ in range(num):
        password_list.append(random.choice(numbers))
    
    random.shuffle(password_list)
    password = ''.join(password_list)
    
    result_label.config(text="Password is: " + password)

# Creating the main window
root = tk.Tk()
root.title("Password Generator")

# Creating and placing the widgets
tk.Label(root, text="Enter number of numbers you need in password:").grid(row=0, column=0)
entry_num = tk.Entry(root)
entry_num.grid(row=0, column=1)

tk.Label(root, text="Enter number of symbols you need in password:").grid(row=1, column=0)
entry_sym = tk.Entry(root)
entry_sym.grid(row=1, column=1)

tk.Label(root, text="Enter number of characters you need in password:").grid(row=2, column=0)
entry_letters = tk.Entry(root)
entry_letters.grid(row=2, column=1)

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=3, columnspan=2)

result_label = tk.Label(root, text="")
result_label.grid(row=4, columnspan=2)

# Starting the main event loop
root.mainloop()
