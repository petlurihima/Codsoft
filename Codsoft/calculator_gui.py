import tkinter as tk
from tkinter import messagebox

def perform_operation():
    try:
        a = int(entry_a.get())
        b = int(entry_b.get())
        op = operation.get()
        
        if op == '+':
            result = a + b
        elif op == '-':
            result = a - b
        elif op == '*':
            result = a * b
        elif op == '/':
            result = a / b
        elif op == '%':
            result = a % b
        else:
            result = "Invalid operation"
        
        result_label.config(text="Result: " + str(result))
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid integers for the numbers.")
    except ZeroDivisionError:
        messagebox.showerror("Math Error", "Division by zero is not allowed.")

# Creating the main window
root = tk.Tk()
root.title("Simple Calculator")

# Creating and placing the widgets
tk.Label(root, text="Enter first number:").grid(row=0, column=0)
entry_a = tk.Entry(root)
entry_a.grid(row=0, column=1)

tk.Label(root, text="Enter second number:").grid(row=1, column=0)
entry_b = tk.Entry(root)
entry_b.grid(row=1, column=1)

tk.Label(root, text="Enter your operation (+, -, *, /, %):").grid(row=2, column=0)
operation = tk.Entry(root)
operation.grid(row=2, column=1)

calculate_button = tk.Button(root, text="Calculate", command=perform_operation)
calculate_button.grid(row=3, columnspan=2)

result_label = tk.Label(root, text="Result: ")
result_label.grid(row=4, columnspan=2)

# Starting the main event loop
root.mainloop()