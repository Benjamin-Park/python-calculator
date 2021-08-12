import tkinter as tk


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
        
        parent.bind('<Delete>', self.clear)

    def clear(self):
        self.equation.set("")

    # TODO: Implement eval sanitization
    def solve(self):
        self.equation.set(eval(self.equation))


root = tk.Tk()
my_gui = Calculator(root)
root.mainloop()
