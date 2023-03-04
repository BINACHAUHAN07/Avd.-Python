from tkinter import*
def colorRed():
    r.config(fg="red")

def colorGreen():
    r.config(fg="green")

def colorBlue():
    r.config(fg="blue")

def size10():
    r.config(font="Forte 10")

def size18():
    r.config(font="Forte 18")

def size20():
    r.config(font="Forte 20")

def size24():
    r.config(font="Forte 24")

root = Tk()
root.geometry("400x600")
r=Label(root,text = 'ANKITA JIVANI',font='Forte 20')
r.place(x=70,y=0)

Button(root,text='RED',bg='BLACK',fg='RED',font='Forte 15',command=colorRed).place(x=50,y=70)
Button(root,text='GREEN',bg='BLACK',fg='RED',font='Forte 15',command=colorGreen).place(x=130,y=70)
Button(root,text='BLUE',bg='BLACK',fg='RED',font='Forte 15',command=colorBlue).place(x=240,y=70)

Button(root,text='12',bg='BLACK',fg='RED',font='Forte 15',command=size10).place(x=50,y=120)
Button(root,text='18',bg='BLACK',fg='RED',font='Forte 15',command=size18).place(x=120,y=120)
Button(root,text='20',bg='BLACK',fg='RED',font='Forte 15',command=size20).place(x=180,y=120)
Button(root,text='24',bg='BLACK',fg='RED',font='Forte 15',command=size24).place(x=250,y=120)

root.mainloop()

