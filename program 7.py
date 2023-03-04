from tkinter import*
from tkinter import messagebox

root = Tk()
root.geometry("300x200")
w=Label(root,text='Demo of MassageBox',font='80')
w.pack()

messagebox.showinfo("showinfo","Information")
messagebox.showwarning("showwarning","Warning")
messagebox.showerror("showerror","Error")
messagebox.askquestion("askquestion","Are You Sure?")
messagebox.askokcancel("askokcancel","Want to Continue?")
messagebox.askyesno("askyesno","Find the Value?")
messagebox.askretrycancel("askretrycancel","Try Again")

root.mainloop()
