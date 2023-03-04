from tkinter import *
top = Tk()
def hello():
    print("Hello!")
    
menubar =Menu(top)
menubar.add_command(label="File",command=hello)
menubar.add_command(label="Edit",command=hello)
menubar.add_command(label="Format",command=hello)
top.config(menu=menubar)
top.mainloop()

    
