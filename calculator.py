import tkinter as tk
import re


class Calculator(tk.Frame):
    def __init__(self, parent):
        self.parent = parent
        parent.title("Calculator")
        parent.geometry("150x200")
        parent.resizable(False, False)

        self.equation = tk.StringVar()
        self.entry = tk.Entry(self.parent, textvariable=self.equation)
        # FIXME: Replace with grid
        self.entry.pack()

        self.button_clear = tk.Button(parent, text="CE", command=self.clear)
        self.button_clear.pack()
        self.button_0 = tk.Button(parent, text="0", command=lambda: self.button_press("0"))
        self.button_0.pack()
        self.button_1 = tk.Button(parent, text="1", command=lambda: self.button_press("1"))
        self.button_1.pack()
        self.button_plus = tk.Button(parent, text="+", command=lambda: self.button_press("+"))
        self.button_plus.pack()
        self.button_solve = tk.Button(parent, text="=", command=self.solve)
        self.button_solve.pack()

        # Bind keys to functions to allow keyboard input
        parent.bind('<Delete>', self.clear)
        parent.bind('<Return>', self.solve)

    def clear(self, event=None):
        self.equation.set("")

    def button_press(self, key_value, event=None):
        if re.match("^[0-9()+\-*/.]*$", key_value):
            self.equation.set(self.equation.get() + key_value)

    def solve(self, event=None):
        if self.equation.get() != "":
            try:
                self.equation.set(eval(self.equation.get()))
            except SyntaxError:
                print("Syntax Error")


root = tk.Tk()
my_gui = Calculator(root)
root.mainloop()
