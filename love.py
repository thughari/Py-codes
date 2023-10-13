import tkinter as tk
from tkinter import messagebox
def propose():
    message = "Will you marry me?"
    answer = tk.messagebox.askquestion("Proposal", message)
    if answer == 'yes':
        tk.messagebox.showinfo("Congratulations!\U0001F60D", "We are getting married!!\U0001F618\U0001F496\U0001F496\U0001F496!")
    else:
        tk.messagebox.showinfo("Rejected", "I'm sorry, she said no.\U0001F494")

root = tk.Tk()

label = tk.Label(root, text="Click the button to propose!")
label.pack()

button = tk.Button(root, text="Propose", command=propose)
button.pack()

root.mainloop()
