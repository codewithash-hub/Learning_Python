import tkinter as tk

class MyGUI:
    def __init__(self):
        self.root = tk.Tk()

        # create two frames
        self.top_frame = tk.Frame(self.root)
        self.bottom_frame = tk.Frame(self.root)

        
        self.top_frame.pack()
        self.bottom_frame.pack()


        # 3 widgets for top frame
        self.label1 = tk.Label(self.top_frame, text = 'Winken')
        self.label2 = tk.Label(self.top_frame, text = 'Blinken')
        self.label3 = tk.Label(self.top_frame, text = 'Nod')

        # Pack labels in the top frame
        self.label1.pack(side='top')
        self.label2.pack(side='top')
        self.label3.pack(side='top')

        # create 3 wdgets for bottom frame
        self.label4 = tk.Label(self.bottom_frame, text = 'Winken')
        self.label5 = tk.Label(self.bottom_frame, text = 'Blinken')
        self.label6 = tk.Label(self.bottom_frame, text = 'Nod')

        # Pack labels in the top frame
        self.label4.pack(side='left')
        self.label5.pack(side='left')
        self.label6.pack(side='left')

        self.root.mainloop()

if __name__ == '__main__':
    my_gui = MyGUI()
