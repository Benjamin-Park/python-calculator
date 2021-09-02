import tkinter as tk
from tkinter import ttk

def create_buttons(self):
    parent = self

    # Define buttons
    self.button_clear = tk.Button(parent, text="CE", command=self.clear, width=2)
    self.button_backspace = tk.Button(parent, text="B", command=self.backspace, width=2)

    self.button_0 = tk.Button(parent, text="0", command=lambda: self.button_press("0"), width=2)
    self.button_1 = tk.Button(parent, text="1", command=lambda: self.button_press("1"), width=2)
    self.button_2 = tk.Button(parent, text="2", command=lambda: self.button_press("2"), width=2)
    self.button_3 = tk.Button(parent, text="3", command=lambda: self.button_press("3"), width=2)
    self.button_4 = tk.Button(parent, text="4", command=lambda: self.button_press("4"), width=2)
    self.button_5 = tk.Button(parent, text="5", command=lambda: self.button_press("5"), width=2)
    self.button_6 = tk.Button(parent, text="6", command=lambda: self.button_press("6"), width=2)
    self.button_7 = tk.Button(parent, text="7", command=lambda: self.button_press("7"), width=2)
    self.button_8 = tk.Button(parent, text="8", command=lambda: self.button_press("8"), width=2)
    self.button_9 = tk.Button(parent, text="9", command=lambda: self.button_press("9"), width=2)

    self.button_decimal = tk.Button(parent, text=".", command=lambda: self.button_press("."), width=2)

    self.button_plus = tk.Button(parent, text="+", command=lambda: self.button_press("+"), width=2, bg="lightgrey")
    self.button_minus = tk.Button(parent, text="-", command=lambda: self.button_press("-"), width=2, bg="lightgrey")
    self.button_multiply = tk.Button(parent, text="*", command=lambda: self.button_press("*"), width=2, bg="lightgrey")
    self.button_divide = tk.Button(parent, text="/", command=lambda: self.button_press("/"), width=2, bg="lightgrey")
    self.button_solve = tk.Button(parent, text="=", command=self.solve, width=2, bg="orange")

    # Draw buttons on screen
    self.button_clear.grid(row=1, column=0, columnspan=2, sticky="NSEW")
    self.button_backspace.grid(row=1, column=2, sticky="NSEW")

    self.button_0.grid(row=5, column=0, sticky="NSEW")
    self.button_1.grid(row=4, column=0, sticky="NSEW")
    self.button_2.grid(row=4, column=1, sticky="NSEW")
    self.button_3.grid(row=4, column=2, sticky="NSEW")
    self.button_4.grid(row=3, column=0, sticky="NSEW")
    self.button_5.grid(row=3, column=1, sticky="NSEW")
    self.button_6.grid(row=3, column=2, sticky="NSEW")
    self.button_7.grid(row=2, column=0, sticky="NSEW")
    self.button_8.grid(row=2, column=1, sticky="NSEW")
    self.button_9.grid(row=2, column=2, sticky="NSEW")

    self.button_decimal.grid(row=5, column=1, sticky="NSEW")

    self.button_plus.grid(row=3, column=3, sticky="NSEW")
    self.button_minus.grid(row=4, column=3, sticky="NSEW")
    self.button_multiply.grid(row=2, column=3, sticky="NSEW")
    self.button_divide.grid(row=1, column=3, sticky="NSEW")
    self.button_solve.grid(row=5, column=3, sticky="NSEW")