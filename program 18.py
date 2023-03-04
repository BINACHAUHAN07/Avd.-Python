import tkinter as tk

from tkinter import*

my_w=tk.Tk()

my_w.geometry("300x150")

my_w.title("Welcome")

my_list=['One','Two','Three','Four','Five']

sb2=Spinbox(my_w,values=my_list,width=10)

sb2.grid(row=1,column=2,padx=20,pady=20)

my_w.mainloop()
