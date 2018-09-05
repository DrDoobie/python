from tkinter import *

root = Tk()
root.geometry("250x300")

one = Button(root, text = "1")
two = Button(root, text = "2")
three = Button(root, text = "3")

four = Button(root, text = "4")
five = Button(root, text = "5")
six = Button(root, text = "6")

seven = Button(root, text = "7")
eight = Button(root, text = "8")
nine = Button(root, text = "9")

one.grid(row = 0), four.grid(row = 0, column = 1), seven.grid(row = 0, column = 2)
two.grid(row = 1), five.grid(row = 1, column = 1), eight.grid(row = 1, column = 2)
three.grid(row = 2), six.grid(row = 2, column = 1), nine.grid(row = 2, column = 2)

root.mainloop()