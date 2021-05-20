from tkinter import  *

root=Tk()
root.title("BMS CALCULATOR")

def cal():
    h = h_entry.get()
    h=float(h)
    h=h*h
    w = w_entry.get()
    w=float(w)

    try:
        a=w/h
        bmi=eval('a')
        result.delete(0, END)
        result.insert(0,bmi)
    except:
        result.delete(0,END)
        result.insert(0,"error")

h_entry=Entry()
h_entry.grid(row=2,columnspan=6)

w_entry=Entry()
w_entry.grid(row=4,columnspan=6)

labelh=Label(root,text="entire the height ,in meter")
labelh.grid(row=1,column=0)

labelw=Label(root,text="entire the weight ,in kg")
labelw.grid(row=3,column=0)

Button(root,text="calculate", command=lambda :cal()).grid(row=6,columnspan=6)
result=Entry(root)
result.grid(row=7,columnspan=6)

label1=Label(root,text="bmi  lessthan 18.5'under weight' ")
label1.grid(row=8,columnspan=6)

label2=Label(root,text="18.5 to 24.5  'normal'")
label2.grid(row=9,columnspan=6)

label3=Label(root,text="overweight bmi above 25")
label3.grid(row=10,columnspan=6)



root.mainloop()