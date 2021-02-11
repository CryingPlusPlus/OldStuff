from tkinter import *

root = Tk()
root.geometry('600x600')

c = Canvas(root, height=600, width=600, bg='#515151')
c.pack()

c.create_oval(150,150, 450,450, fill='green')

root.mainloop()
