import tkinter as tk
root = tk.Tk()
root.geometry("300x200")
def func(event):
    print("You hit return.")
def onclick(event):
    print("You clicked the button")
root.bind('<Return>', onclick)
button = tk.Button(root, text="click me")
button.bind('<Button-1>', onclick)
button.pack()
root.mainloop()