#!/usr/bin/env python3
import tkinter as tk
from tkinter import messagebox
import re
import json
import configparser
import os

import buttons


# Class containing all the code for calculator functionality
class Calculator(tk.Frame):
	""" Custom tkinter Frame that contains a fully functional calculator with GUI. """
	# Initialisation of calculator GUI and configuration
    def __init__(self, parent):
        self.__version__ = "1.3.0"
		
		# Parse cofig file and load the users preferences/theme
        config = configparser.ConfigParser()
        config.read("config.conf")
        self.decimal_precision = int(config.get("CONFIG", "precision"))
        self.theme = config.get("CONFIG", "theme")
        self.theme_data = json.load(open(f"theme/{self.theme}.json", "r"))
        super().__init__(bg=self.theme_data["interface"])
		
		# Setup Window geometry
        self.parent = parent
        parent.title("Calculator")
        parent.resizable(False, False)
		
		# Set inital conditions of entry field and display
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
		""" Clears everything from the equation input. """
        self.equation.set("")

    def backspace(self, event=None):
		""" Removes the last entered character from the equation. """
        self.equation.set(self.equation.get()[:-1])

    def button_press(self, key_value, event=None):
		"""
		Appends the value of the pressed button/key to the equation.
		
		:param str key_value: takes char [0-9], decimal or mathematical operator
		
		Sanitisation is performed to ensure that only valid characters are input in equation strings.
		"""
        if re.match("^[0-9()+\\-*/.]*$", key_value):
            self.equation.set(self.equation.get() + key_value)

    def solve(self, event=None):
		"""
		Returns the answer to the supplied mathematical equation string.
		
		Sanitisation is performed to strip leading zeros, prevent invalid input and zero division errors.
		Answer is rounded to number of decimal places (decimal_precision) specified by the user in config file.
		"""
        if self.equation.get() != "":
            try:
				# Sanitise equation to remove leading zeros and invalid characters
                sanitised_equation = []
                split_equation = re.split("([+\\-*/])", self.equation.get())
                for expression in split_equation:
                    sanitised_equation.append(expression.lstrip('0'))
                sanitised_equation = ''.join(sanitised_equation)
				
				# Solve sanitised_equation and round answer to specified number of decimal places
                self.equation.set(round(eval(sanitised_equation), self.decimal_precision))
			# Present any errors to the user in a system dialouge box
            except (SyntaxError, ZeroDivisionError, TypeError) as error:
                error_message = type(error).__name__
                print(error_message)
                tk.messagebox.showerror('Calculator Error', error_message)


# Create an instance of calculator class and render inside of parented tkinter window
if __name__ == "__main__":
    root = tk.Tk()
    root.attributes('-toolwindow', True) if os.name == "nt" else None  # Comment out this line restore normal window behaviour
    calculator_gui = Calculator(root)
    calculator_gui.pack()
    root.mainloop()
