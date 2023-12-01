import tkinter as tk
from tkinter import ttk
import sys

def calc_avg():
    test1 = test1_int.get()
    test2 = test2_int.get()
    test3 = test3_int.get()
    
    average = (test1 + test2 + test3) / 3
    
    display_string.set(f'{average: .2f}')


def quit_program():
    sys.exit()


root = tk.Tk()
root.title('Calculate Average Score')
root.geometry('300x220')

# Labels and entries
test1_label = ttk.Label(root, text = 'Enter the score for test 1:')
test1_int = tk.IntVar()
test1_entry = ttk.Entry(root, textvariable = test1_int)
test1_label.grid(row=0, column=0, padx = 10, pady = 10)
test1_entry.grid(row=0, column=1, padx = 10, pady = 10)

test2_label = ttk.Label(root, text = 'Enter the score for test 2:')
test2_int = tk.IntVar()
test2_entry = ttk.Entry(root, textvariable = test2_int)
test2_label.grid(row=1, column=0, padx = 10, pady = 10)
test2_entry.grid(row=1, column=1, padx = 10, pady = 10)

test3_label = ttk.Label(root, text = 'Enter the score for test 3:')
test3_int = tk.IntVar()
test3_entry = ttk.Entry(root, textvariable = test3_int)
test3_label.grid(row=2, column=0, padx = 10, pady = 10)
test3_entry.grid(row=2, column=1, padx = 10, pady = 10)

# Display label
display_label = ttk.Label(root, text = 'Average')
display_string = tk.StringVar()
display = ttk.Label(root, text='', textvariable = display_string)
display_label.grid(row=3, column=0)
display.grid(row=3, column=1)

# calculate button
average_btn = ttk.Button(root, text = "Averege", command = calc_avg)
quit_btn = ttk.Button(root, text = "Quit", command = quit_program)
average_btn.grid(row=4, column=0, padx = 10, pady = 10)
quit_btn.grid(row=4, column=1, padx = 10, pady = 10)

root.mainloop()
