import tkinter as tk
import ttkbootstrap  as ttk

class MyGUI:
    def __init__(self):
        self.main_wondow = tk.Tk()

        self.label = ttk.Label(self.main_wondow, text = 'Hello World!')
        self.label.pack()

        self.main_wondow.mainloop()

if __name__ == '__main__':
    my_gui = MyGUI()