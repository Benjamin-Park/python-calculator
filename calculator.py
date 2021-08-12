import tkinter as tk

class Calculator(tk.Frame):
    def __init__(self, parent):
        self.parent = parent
        parent.title("Calculator")
        parent.geometry("150x200")
        parent.resizable(False, False)


root = tk.Tk()
my_gui = Calculator(root)
root.mainloop()
