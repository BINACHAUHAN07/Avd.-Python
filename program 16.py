from tkinter import*

def a():
    #E1.delete(2,4)
    #print(E1.get())
    E1.icursor(3)
    E1.insert(5,"hii")
    print(E1.get())
    E1.select_clear()
    print(E1.select_present())
    E1.select_range(1,5)

top=Tk()
l1=Label(top,text="Username")
l1.pack(side=LEFT)
abc=StringVar()
E1=Entry(top,textvariable=abc,bd=5,selectborderwidth=3,highlightcolor="RED",justify="center",selectbackground="RED")
E1.pack()
btn=Button(text="click",command=a)
btn.pack()
print(abc.get())
top.mainloop()
