from tkinter import *
from tkinter import messagebox
from math import sqrt

def calculate_sqrt():
    try:
        num = int(entry.get())
        if num < 0:
            raise ValueError("Negative number")
        result = sqrt(num)
        output.delete(0, END)
        output.insert(0, round(result, 4))
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a non-negative integer.")

root = Tk()
root.title("Square Root Calculator")
root.geometry("350x200")


Label(root, text="Enter an integer:", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10)
entry = Entry(root)
entry.grid(row=0, column=1)

Label(root, text="Square root:", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=10)
output = Entry(root)
output.grid(row=1, column=1)
output.insert(0, "0")

Button(root, text="Compute", command=calculate_sqrt).grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
