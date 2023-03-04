import tkinter as tk
from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
root = Tk()
root.title("Insert Data")
connection = mysql.connector.connect(host='localhost',user='root',password="",port='3306',database='demo1')

c = connection.cursor()
bkg = "#636e72"
frame = tk.Frame(root, bg=bkg)
label_firstname = tk.Label(frame, text="First Name: ", font=('verdana',12), bg=bkg)
entry_firstname = tk.Entry(frame, font=('verdana',12))
label_lastname = tk.Label(frame, text="Last Name: ", font=('verdana',12), bg=bkg)
entry_lastname = tk.Entry(frame, font=('verdana',12))
label_email = tk.Label(frame, text="Email: ", font=('verdana',12), bg=bkg)
entry_email = tk.Entry(frame, font=('verdana',12))
label_age = tk.Label(frame, text="Age: ", font=('verdana',12), bg=bkg)
entry_age = tk.Entry(frame, font=('verdana',12))


def insertData():
    firstname = entry_firstname.get()
    lastname = entry_lastname.get()
    email = entry_email.get()
    age = entry_age.get()
    insert_query = "INSERT INTO users(`firstname`, `lastname`, `email`, `age`)  VALUES (%s,%s,%s,%s)"
    vals = (firstname,lastname,email,age)
    c.execute(insert_query,vals)
    connection.commit()
    messagebox.showinfo("Info","Record Inserted...")
def updateData():
    firstname = entry_firstname.get()
    lastname = entry_lastname.get()
    email = entry_email.get()
    age = entry_age.get()
    update_qry="Update users set firstname='%s',lastname='%s', email='%s', age='%s'where firstname='%s'"%(firstname,lastname,email,age,firstname)
    c.execute(update_qry)
    connection.commit()
    messagebox.showinfo("Info","Record Updated")

def deleteData():
    firstname = entry_firstname.get()
    delete_qry="delete from users where firstname='%s'" %(firstname)
    c.execute(delete_qry)
    connection.commit()
    messagebox.showinfo("Info","Record Deleted")

def display_record():
    top = Toplevel()
    top.geometry("300x300")
    top.title("toplevel")
    c.execute("SELECT * FROM users")
    i=0
    for users in c: 
        for j in range(len(users)):
            #e = Entry(top, width=10, fg='blue')
            e = Label(top, width=10, fg='blue',
                      text=users[j])
            e.grid(row=i, column=j) 
            #e.insert(END, users[j])
        i=i+1


def search_record():
    top = Toplevel()
    top.geometry("300x300")
    top.title("toplevel")
    c.execute("SELECT * FROM users where firstname='%s'" % entry_firstname.get())
    i=0
    for users in c: 
        for j in range(len(users)):
            e = Entry(top, width=10, fg='blue') 
            e.grid(row=i, column=j) 
            e.insert(END, users[j])
        i=i+1


button_insert = tk.Button(frame, text="Insert", font=('verdana',14), bg='orange',
                          command = insertData)
button_update = tk.Button(frame, text="Update", font=('verdana',14), bg='orange',
                          command = updateData)
button_delete = tk.Button(frame, text="Delete", font=('verdana',14), bg='orange',
                          command = deleteData)
button_show = tk.Button(frame, text="Display Record", font=('verdana',14), bg='orange',
                          command = display_record)
button_search = tk.Button(frame, text="Search", font=('verdana',14), bg='orange',
                          command = search_record)

label_firstname.grid(row=0, column=0)
entry_firstname.grid(row=0, column=1, pady=10, padx=10)
label_lastname.grid(row=1, column=0)
entry_lastname.grid(row=1, column=1, pady=10, padx=10)
label_email.grid(row=2, column=0, sticky='e')
entry_email.grid(row=2, column=1, pady=10, padx=10)
label_age.grid(row=3, column=0, sticky='e')
entry_age.grid(row=3, column=1, pady=10, padx=10)
button_insert.grid(row=4,column=0, columnspan=2, pady=10, padx=10, sticky='nsew')
button_update.grid(row=5,column=0, columnspan=2, pady=10, padx=10, sticky='nsew')
button_delete.grid(row=6,column=0, columnspan=2, pady=10, padx=10, sticky='nsew')
button_show.grid(row=7,column=0, columnspan=2, pady=10, padx=10, sticky='nsew')
button_search.grid(row=8,column=0, columnspan=2, pady=10, padx=10, sticky='nsew')

frame.grid(row=0, column=0)
root.mainloop()
