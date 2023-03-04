from tkinter import*
from tkinter import messagebox

root = Tk()
root.geometry("300x200")
w=Label(root,text='Demo of MassageBox',font='80')
w.pack()

x=messagebox.showinfo("showinfo","Information")
print(x)
x=messagebox.showwarning("showwarning","Warning")
print(x)
x=messagebox.showerror("showerror","Error")
print(x)
x=messagebox.askquestion("askquestion","Are You Sure?")
print(x)
x=messagebox.askokcancel("askokcancel","Want to Continue?")
print(x)
x=messagebox.askyesno("askyesno","Find the Value?")
print(x)
x=messagebox.askretrycancel("askretrycancel","Try Again")
print(x)

root.mainloop()
