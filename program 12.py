
from tkinter import*

def sel():
    selection="You selected the options" +str(var.get())
    label.config(text=selection)
root=Tk()
var=IntVar()
R1 = Radiobutton(root,text="option1",variable=var,value=1,command=sel)
R1.place(x=10,y=50)

R2 = Radiobutton(root,text="option2",variable=var,value=2,command=sel)
R2.place(x=10,y=100)

R3 = Radiobutton(root,text="option3",variable=var,value=3,command=sel)
R3.place(x=10,y=150)

label=Label(root)
label.place(x=10,y=200)
root.mainloop()
