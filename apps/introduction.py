from tkinter import *
# Notes from first time working with tkinter
# Pack is used to quickly place something in the window

# Instantiates window - REQUIRED
root = Tk()

# "Container" in window root
topFrame = Frame(root)
topFrame.pack()

botFrame = Frame(root)
# Parameter inside of pack allows you to define where you want the widget
botFrame.pack(side = BOTTOM)

# Simple button (location, display, colour(optional))
sampleButton = Button(topFrame, text = "Click Me!", fg = "red", bg = "black")
sampleButton.pack()

# Simple text box
sampleText = Label(root, text = "Did you do it?")
sampleText.pack()

# Keeps the window going/open. When this loop is broken the window is closed. - REQUIRED
root.mainloop()