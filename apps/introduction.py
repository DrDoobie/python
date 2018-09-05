from tkinter import *
# Notes from first time working with tkinter

# Instantiates window
root = Tk()
# Label = text(window, string)
label = Label(root, text = "I am a string.")
# Quickly place widget using pack
label.pack()
# Keeps the window going/open. When this loop is broken the window is closed.
root.mainloop()