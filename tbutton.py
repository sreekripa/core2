# from tkinter import *
# root=Tk()
# Button(root,text="login",bg="cyan").pack()
# Button(root,text="cancel",bg="red").pack()
# root.mainloop()

from tkinter import *
root=Tk()
f=Frame(root)
f.pack()
def fun():
    print("hai avodha")
def clear():
    print("cancelled")
Button(f,text="login",bg="cyan",command=fun).pack()
Button(f,text="cancel",bg="red",command=clear).pack()
root.mainloop()



