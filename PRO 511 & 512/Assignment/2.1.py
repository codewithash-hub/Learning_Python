from tkinter import ttk
import tkinter as tk
import sys

def show_info():
    name_label_string.set('Steven Marcus')
    street_label_string.set('274 Bailt Drive')
    city_label_string.set('Waynesville, NC 27999')
    

def quit_program():
    sys.exit()


# Set a master window that contains all the widgets
root = tk.Tk()
root.title('Name & Address')
root.geometry('200x150')
root.resizable()

# create an output label to displa name and address
name_label_string = tk.StringVar()
name_label = ttk.Label(root, text='Output', textvariable = name_label_string)
name_label.pack()

street_label_string = tk.StringVar()
street_label = ttk.Label(root, textvariable = street_label_string)
street_label.pack()

city_label_string = tk.StringVar()
city_label = ttk.Label(root, textvariable = city_label_string)
city_label.pack()


# Create buttons 
show_btn = ttk.Button(root, text = 'Show info', command = show_info) 
exit_btn = ttk.Button(root, text = 'Quit', command = quit_program)
show_btn.pack(side = 'left', padx = 15)
exit_btn.pack(side = 'left', padx = 10)


# run a program
root.mainloop()