from tkinter import*

def hd():
    bottomframe1.pack_forget()
root = Tk()
frame = Frame(root)
frame.pack()

bottomframe=Frame(root,width=200,bg="blue")
bottomframe.pack(side=BOTTOM)

bottomframe1 = Frame(root,width=200,bg="blue",bd=2,relief="solid",height=50,highlightcolor="red")
bottomframe1.pack()

greenbutton = Button(frame,text="Brown",fg="brown")
greenbutton.pack(side=LEFT)

bluebutton = Button(frame,text="Blue",fg="blue")
bluebutton.pack(side=LEFT)

blackbutton = Button(bottomframe,text="Hide",fg="black",command=hd)
blackbutton.pack(side=BOTTOM)

root.mainloop()
