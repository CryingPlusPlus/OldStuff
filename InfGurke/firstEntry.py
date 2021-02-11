from tkinter import *

root = Tk()

entry = Entry(root)
entry.pack()


def Click():
    label = Label(root, text=entry.get()).pack()


button = Button(root, text='ClickMe', command=Click).pack()
root.mainloop()
