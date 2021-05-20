from tkinter import *
root=Tk()
def fun():
    print("am funtion")
mymenu=Menu(root)
root.config(menu=mymenu)

submenu=Menu(mymenu)

mymenu.add_cascade(label="file",menu=submenu)
submenu.add_command(label="save")
submenu.add_separator()
submenu.add_command(label="exit",command=root.quit)

newmenu=Menu(mymenu)

mymenu.add_cascade(label="edit",menu=newmenu)
newmenu.add_command(label="undu")
newmenu.add_command(label="redo")
root.mainloop()



# from tkinter import *
# import tkinter.messagebox
# root=Tk()
# def fun():
#     print("this is afuntion")
#
# def und():
#      tkinter.messagebox.askyesno("title", "you want to save")
#
# mymenu=Menu(root)
# root.config(menu=mymenu)
#
# submenu=Menu(mymenu)
#
# mymenu.add_cascade(label="file",menu=submenu)
#
# submenu.add_command(label="save",command=fun)
#
# submenu.add_separator()
# submenu.add_command(label="exit",command=root.quit)
#
# newmenu=Menu(mymenu)
# mymenu.add_cascade(label="edit",menu=newmenu)
# newmenu.add_command(label="undo",command=und)
# newmenu.add_separator()
# newmenu.add_command(label="redo")
# root.mainloop()
