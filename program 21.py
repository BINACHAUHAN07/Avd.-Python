from tkinter import*
def chk1():
    print(var3.get())
root=Tk()
root.geometry("300x200")
w=Label(root,text="GeeksForGeeks",font="50")
w.pack()
menubutton=Menubutton(root,text="Menu")
menubutton.menu=Menu(menubutton,tearoff=0)
menubutton["menu"]=menubutton.menu
var1=IntVar()
var2=IntVar()
var3=StringVar()
menubutton.menu.add_checkbutton(label="Courses",variable=var1)
menubutton.menu.add_checkbutton(label="Students",variable=var2)
menubutton.menu.add_checkbutton(label="Careers",variable=var3,command=chk1)
menubutton.menu.add_radiobutton(label='Radio1',value=0)
menubutton.menu.add_command(label='my_fun')
menubutton.pack()
root.mainloop()

