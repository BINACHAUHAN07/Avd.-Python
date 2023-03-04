from tkinter import*
root=Tk()
root.geometry("300x200")

def chk1():
    print(Checkbutton1.get())
w=Label(root,text="GeeksForGeeks",font="50")
w.pack()
Checkbutton1=IntVar()
Checkbutton2=IntVar()
Checkbutton3=IntVar()

Button1=Checkbutton(root,text="Tutorial",variable=Checkbutton1,onvalue=1,offvalue=0,height=2,command=chk1,width=10)
Button1.pack()

Button2=Checkbutton(root,text="Courses",variable=Checkbutton2,onvalue=1,offvalue=0,height=2,command=chk1,width=10)
Button2.pack()

Button3=Checkbutton(root,text="Students",variable=Checkbutton3,onvalue=1,offvalue=0,height=2,command=chk1,width=10)
Button3.pack()

root.mainloop()
