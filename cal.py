import tkinter as tk

def button_click(value):
    current = display_var.get()
    display_var.set(current + value)

def clear():
    display_var.set("")

def equal():
    try:
        result = str(eval(display_var.get()))
        display_var.set(result)
    except:
        display_var.set("Error")

# Main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x350")
root.resizable(False, False)

display_var = tk.StringVar()

# Display box
display = tk.Entry(root, font=("Arial", 20), textvariable=display_var, justify="right")
display.pack(fill="both", padx=10, pady=10)

# Buttons frame
btn_frame = tk.Frame(root)
btn_frame.pack()

# Buttons layout
buttons = [
    ("7", 0, 0), ("8", 0, 1), ("9", 0, 2), ("/", 0, 3),
    ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), ("*", 1, 3),
    ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("-", 2, 3),
    ("0", 3, 0), (".", 3, 1), ("=", 3, 2), ("+", 3, 3),
]

for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(btn_frame, text=text, width=5, height=2,
                        command=equal, font=("Arial", 14))
    else:
        btn = tk.Button(btn_frame, text=text, width=5, height=2,
                        command=lambda t=text: button_click(t), font=("Arial", 14))
    btn.grid(row=row, column=col, padx=5, pady=5)

# Clear Button
clear_btn = tk.Button(root, text="Clear", width=20, height=2, command=clear, font=("Arial", 14))
clear_btn.pack(pady=10)

root.mainloop()
