from tkinter import*
from tkinter import ttk

def left_click(event):
    print("This is click")

def double_click(event):
    print("This is Double click")

def motion(event):
    print("This is Motion")
    x,y=event.x,event.y
    print('()','()'.format(x,y))

root=Tk()
button=Button(root,width=200,height=200,background="gray")
button.place(x=50,y=60)
button.bind("<Button-1>",left_click)
button.bind("<Double-1>",double_click)
button.bind("<Motion>",motion)

root.mainloop()
