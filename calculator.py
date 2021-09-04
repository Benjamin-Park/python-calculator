#!/usr/bin/env python3
import tkinter as tk
from tkinter import messagebox
import re
import json
import configparser

import buttons


class Calculator(tk.Frame):
    def __init__(self, parent):
        self.__version__ = "1.1.0"

        config = configparser.ConfigParser()
        config.read("config.conf")
        self.theme = config.get("CONFIG", "theme")
        self.theme_data = json.load(open(f"theme/{self.theme}.json", "r"))
        super().__init__(bg=self.theme_data["interface"])

        self.parent = parent
        parent.title("Calculator")
        parent.resizable(False, False)

        self.equation = tk.StringVar()
        self.entry = tk.Entry(self, textvariable=self.equation, state="readonly", fg=self.theme_data["display"]["fg"], readonlybackground=self.theme_data["display"]["bg"])
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
        if re.match("^[0-9()+\\-*/.]*$", key_value):
            self.equation.set(self.equation.get() + key_value)

    def solve(self, event=None):
        if self.equation.get() != "":
            try:
                sanitised_equation = []
                split_equation = re.split("([+\\-*/])", self.equation.get())
                for expression in split_equation:
                    sanitised_equation.append(expression.lstrip('0'))
                sanitised_equation = ''.join(sanitised_equation)

                self.equation.set(eval(sanitised_equation))
            except (SyntaxError, ZeroDivisionError) as error:
                error_message = type(error).__name__
                print(error_message)
                tk.messagebox.showerror('Calculator Error', error_message)


if __name__ == "__main__":
    root = tk.Tk()
    calculator_gui = Calculator(root)
    calculator_gui.pack()
    root.mainloop()
