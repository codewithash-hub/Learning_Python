import tkinter as tk
from tkinter import ttk

class MyGUI:
    def __init__(self):
        self.main_wondow = tk.Tk()

        self.label = ttk.Label(self.main_wondow, text = 'Hello World!',borderwidth=1, relief='groove')
        self.label.pack(side = 'left', padx=20, pady=20, ipadx=20, ipady=20)

        self.label = ttk.Label(self.main_wondow, text = 'This is my GUI program',borderwidth=1, relief='groove')
        self.label.pack(side = 'left', padx=20, pady=20, ipadx=20, ipady=20)

        self.main_wondow.mainloop()

if __name__ == '__main__':
    my_gui = MyGUI()