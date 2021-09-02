#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import re
import sys

import buttons


class Calculator(tk.Frame):
    def __init__(self, parent):
        super().__init__()

        self.parent = parent
        parent.title("Calculator")
        # parent.geometry("150x200")
        parent.resizable(False, False)

        self.equation = tk.StringVar()
        self.entry = ttk.Entry(self, textvariable=self.equation, state="readonly")
        self.entry.grid(row=0, column=0, columnspan=4, sticky="EW")

        buttons.create_buttons(self)

        # Bind keys to functions to allow keyboard input
        parent.bind('<Delete>', self.clear)
        parent.bind('<BackSpace>', self.backspace)
        parent.bind('<Return>', self.solve)
        parent.bind('<Key>', lambda event: self.button_press(event.char))

    def clear(self, event=None):
        self.equation.set("")

    def backspace(self, event=None):
        self.equation.set(self.equation.get()[:-1])

    def button_press(self, key_value, event=None):
        if re.match("^[0-9()+\-*/.]*$", key_value):
            self.equation.set(self.equation.get() + key_value)

    def solve(self, event=None):
        if self.equation.get() != "":
            try:
                self.equation.set(eval(self.equation.get()))
            except (SyntaxError, ZeroDivisionError) as error:
                error_message = type(error).__name__
                print(error_message)
                tk.messagebox.showerror('Calculator Error', error_message)


if __name__ == "__main__":
    root = tk.Tk()
    calculator_gui = Calculator(root)
    calculator_gui.pack()
    root.mainloop()
