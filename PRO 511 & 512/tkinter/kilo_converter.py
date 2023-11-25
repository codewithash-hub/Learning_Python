import tkinter as tk
import tkinter.messagebox as msg_box

class KiloConverterGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Kimometer Conveter")

        # create two frames
        self.top_frame = tk.Frame(self.root)
        self.mid_frame = tk.Frame(self.root)
        self.bottom_frame = tk.Frame(self.root)

        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        # Create the widgets for the top frame.
        self.prompt_label = tk.Label(self.top_frame, text = 'Enter a distance in kilometers:')
        self.kilo_entry = tk.Entry(self.top_frame, width = 10)

        self.prompt_label.pack(side = 'left')
        self.kilo_entry.pack(side = 'left')
        
        # Create widgets for mid frame
        self.descr_label = tk.Label(self.mid_frame, text = 'Converted to miles')
        self.descr_label.pack()

        self.value = tk.StringVar()
        self.miles = tk.Label(self.mid_frame, textvariable = self.value)
        self.miles.pack()

        # Create the button widgets for the bottom frame.
        self.calc_btn = tk.Button(self.bottom_frame, text = 'Convert', command = self.convert)
        self.quit_btn = tk.Button(self.bottom_frame, text = 'Quit', command = self.root.destroy)

        self.calc_btn.pack(side = 'left')
        self.quit_btn.pack(side = 'left')

        self.root.mainloop()

    # The convert method is a callback function for the calculation button'
    def convert(self):
        kilo = float(self.kilo_entry.get())

        miles = kilo * 0.6214


        self.value.set(miles)
        msg_box.showinfo('Results', f'{str(kilo)} kilometers is equal to {miles:.2f} miles')



if __name__ == '__main__':
    my_gui = KiloConverterGUI()
