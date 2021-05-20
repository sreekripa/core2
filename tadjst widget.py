# from tkinter import *
# root=Tk()
# Label(root,text="X direction",bg="red").pack(fill=X)
# Label(root,text="Y direction",bg="cyan").pack(side=LEFT,fill=Y)
# root.mainloop()


# TKINTER CLASS

from tkinter import *
root=Tk()
class demo:
    def __init__(self,rootone):
        frame=Frame(rootone)
        frame.pack()
        Button(frame,text="avodha",bg="red",command=self.name).pack()
        Button(frame,text="exit",bg="cyan",command=frame.quit).pack()
    def name(self):
        print("i am avodha")
obj=demo(root)
root.mainloop()
