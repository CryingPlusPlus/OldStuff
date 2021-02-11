from tkinter import *

root = Tk()

def Click():
    myLabel = Label(root, text='hello i pressed button')
    myLabel.pack()

#hexcodes können als farben verwendet werden -> pasteeeellll
button = Button(root, text='Click Mich', pady=50, command=Click, fg='green')
button.pack()
root.mainloop()