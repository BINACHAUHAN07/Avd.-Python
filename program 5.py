from tkinter import*

def hello():
    print("Single click,Button-1")
def quit(event):
    print("Double click,so let's stop")
    import sys;sys.exit()
widget=Button(None,text = "Mouse Clicks",font="Arial 20",command=hello)
widget.pack()
widget.bind('<Button-1>',hello())
widget.bind('<Double-1>',quit)
widget.mainloop()
