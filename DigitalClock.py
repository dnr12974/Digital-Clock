from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Clock")

def time():
    string = strftime('%H:%M:%S %p')
    label_time.config(text=string)
    
    # Get the current date and day
    date_string = strftime('%A, %B %d, %Y')
    label_date.config(text=date_string)
    
    label_time.after(1000, time)

# Time label
label_time = Label(root, font=("ds-digital", 132), background="black", foreground="yellow")
label_time.pack(anchor='center')

# Date label
label_date = Label(root, font=("ds-digital", 45), background="black", foreground="yellow")
label_date.pack(anchor='center')

time()
mainloop()
