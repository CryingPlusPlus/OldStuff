from tkinter import *

root = Tk()
root.title('Images')
root.iconbitmap(r'D:/python-icon-png-5.png') # it is to big but would work

quitButton = Button(root, text='Exit', command=root.quit)
quitButton.pack()

root.mainloop()