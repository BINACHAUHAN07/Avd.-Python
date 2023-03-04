from tkinter import*

def shw():
    top = Toplevel()
    top.geometry("180x100")
    top.title("toplevel")
    l2 = Label(top,text="This is toplevel window")
    l2.pack()
    btn1 = Button(top,text="exit",command=top.destroy)
    btn1.pack()

root=Tk()
root.geometry("200x300")
root .title("main")
l=Label(root,text="This is root window")
btn=Button(root,text="click",command=shw)
l.pack()
btn.pack()
root.mainloop()
