from tkinter import *
from functions import *

root = Tk()
root.title('CIE Statistics Calculator by Ungku')

n1 = Entry(root)
n1.pack()
n1.get()

def myClick():
    myLabel = Label(root, text=n1.get())
    myLabel.pack()

mainLabel = Label(root, text='CIE Statistics Calculator')
mainLabel.pack()

myButton = Button(root, text='Chi Contigency Test', command = myClick,  padx = 30, pady = 30)
myButton.pack()


root.mainloop()
