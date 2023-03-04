from tkinter import*
from tkinter import ttk

def left_click(event):
    x,y=event.x,event.y
    c.create_line(event.x,event.y,50,80,width=5)
    c.create_oval(10,10,80,80,outline="#fill",fill="#1f1",width=2)

    #event.widget.configure(bg="green")
    #c.create_oval(x,x,y,y)
    #c.create_oval(x,x,y,y,fill="red")
    #filename = PhotoImage(file = "a3.jpg")
    #image = canvas.create.image(50,50,anchor=NE,image=filename)

def right_click(event):
    event.widget.configure(bg="red")
    #c.create_line(event.x,event.y,50,80,width=5)
    #c.create_rectangle(50,150,250,50,fill="blue")
    #c.create_oval(10,10,80,80,outline="#fll",fill="#1f1",width=2)
    #c.creare_oval(110,10,120,80,outline="#fll",fill="#1f1",width=2)
    #c.create_rectangle(230,10,290,60,outline="#fll",fill="#1f1",width=2)
    #c.create_arc(30,200,90,100,start=0,extent=210,outline="#fll",fill="#1f1",width=2)
    #points = [150,100,200,120,240,180,210,200,150,150,100,200]
    #c.create_polygon(points,outline="#f11",fill="#1f1",width=2)

def left_double_click(event):
    print("double click")

def motion(event):
    x,y = event.x,event.y
    c.create_oval(x,x,y,y,fill="pink")

root=Tk()
c=Canvas(root,width=1100,height=800,bg="white")
c.pack()
c.bind("<Button-1>",left_click)
c.bind("<Motion>",motion)
root.mainloop()
    
