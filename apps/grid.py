from tkinter import *

root = Tk()

label1 = Label(root, text = "Username: ")
label2 = Label(root, text = "Password: ")

# Entry is a form of taking user input
entry1 = Entry(root)
entry2 = Entry(root)

# Sticky is used for alignment. It used NESW (North, East, South, West) for direction.
label1.grid(row = 0, sticky = W)
label2.grid(row = 1, sticky = W)
entry1.grid(row = 0, column = 1)
entry2.grid(row = 1, column = 1)

# Simple check box
cBox = Checkbutton(root, text = "Remember password")
# Make checkbox take up two cells of space
cBox.grid(columnspan = 2, sticky = W)

button1 = Button(root, text = "Login")
button1.grid(row = 2, column = 1, sticky = E)

root.mainloop()