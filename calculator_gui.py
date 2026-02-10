import tkinter as tk
import math

expression = ""

def press(value):
    global expression
    expression += str(value)
    eq.set(expression)

def clear():
    global expression
    expression = ""
    eq.set("")

def equal():
    global expression
    try:
        result = str(eval(expression))
        eq.set(result)
        expression = result
    except:
        eq.set("Error")
        expression = ""

def sci_function(func):
    global expression
    try:
        result = str(eval(f"math.{func}({expression})"))
        eq.set(result)
        expression = result
    except:
        eq.set("Error")
        expression = ""

root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("400x650")

eq = tk.StringVar()
entry = tk.Entry(root, textvariable=eq, font=("Arial", 20), bd=10, justify="right")
entry.pack(fill="both", ipadx=10, ipady=15, pady=10)

# Normal Buttons
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"]
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack()
    for btn in row:
        if btn == "=":
            tk.Button(frame, text=btn, width=6, height=2, font=("Arial", 16),
                      command=equal).pack(side="left")
        else:
            tk.Button(frame, text=btn, width=6, height=2, font=("Arial", 16),
                      command=lambda x=btn: press(x)).pack(side="left")

# Scientific Buttons
sci_btns = [
    ("sin", "sin"), ("cos", "cos"), ("tan", "tan"),
    ("log", "log10"), ("ln", "log"), ("√", "sqrt"),
    ("x²", "**2"), ("π", "pi"), ("e", "e")
]

frame = tk.Frame(root)
frame.pack(pady=10)

for label, func in sci_btns:
    if func in ["pi", "e", "**2"]:
        tk.Button(frame, text=label, width=6, height=2, font=("Arial", 14),
                  command=lambda x=func: press(f"math.{x}" if x in ["pi", "e"] else x)).pack(side="left", padx=3)
    else:
        tk.Button(frame, text=label, width=6, height=2, font=("Arial", 14),
                  command=lambda x=func: sci_function(x)).pack(side="left", padx=3)

# CLEAR button
tk.Button(root, text="CLEAR", width=25, height=2, font=("Arial", 16),
          command=clear).pack(pady=15)

root.mainloop()