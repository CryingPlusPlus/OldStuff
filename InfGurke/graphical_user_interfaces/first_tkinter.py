from tkinter import *

root = Tk()

# Creating a label widget
pyckingLabel = Label(root, text='Hello WOrlds!')
myLabel1 = Label(root, text='Hello World')
myLabel2 = Label(root, text='Hello World')
myLabel3 = Label(root, text='Hello World')
# shoving it in the screen
pyckingLabel.pack()
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=1)
myLabel3.grid(row=2, column=2)

# a gui is looping all the time to notice every change

root.mainloop()

