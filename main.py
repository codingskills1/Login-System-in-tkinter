from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox 
import tkinter as tk
import sys 

window = Tk()
window.title("Login")
window.geometry("600x300")

def show():
    password_entry.configure(show="")

def hide():
    password_entry.configure(show="*")

def labels():
    global username
    global password
    username = tk.Label(window, text="Username", fg="blue", font=("Arial Bold", 20))
    username.place(x=100, y=70)
    password = tk.Label(window, text="Password", fg="blue", font=("Arial Bold", 20))
    password.place(x=100, y=140)

def entries():
    global username_entry
    global password_entry
    username_entry = Entry(window, width=20)
    username_entry.focus()
    username_entry.place(x=250, y=78)
    password_entry = Entry(window, width=20)
    password_entry.place(x=250, y=150)

def buttons():
    global register_btn 
    global show_btn
    register_btn = tk.Button(window, text="Register", fg="black", bg="blue", font=("Arial Bold", 15), command=clicked)
    register_btn.place(x=250, y=200)
    show_btn = tk.Button(window, text="Show", fg="black", bg="blue", font=("Arial Bold", 10), command=show)
    show_btn.place(x=450 ,y=145)
    hide_btn = tk.Button(window, text="Hide", fg="black", bg="blue", font=("Arial Bold", 10), command=hide)
    hide_btn.place(x=520, y=145)

def clicked():
    if username_entry.get() == "":
        messagebox.showwarning("WARN", "Enter Your Username")

    elif password_entry.get() == "":
        messagebox.showwarning("WARN", "Enter Your Password")

    elif len(username_entry.get()) <= 2:
        messagebox.showwarning("WARN", "Enter Valid Username(more than 2 characters)")

    elif len(password_entry.get()) <=7:
        messagebox.showwarning("WARN", "Your Password must have more than 7 characters")

    elif "@" not in password_entry.get():
        messagebox.showwarning("WARN", "Use '@' in your password for more security")

    else:
        with open("DataBase.txt") as f:
            if username_entry.get() in f.read():
                messagebox.showwarning("WARN", "This username is taken")
            else:
                li = ["-------------------------------"]
                myfile = open("DataBase.txt", "a")
                for i in li:
                    myfile.write("{}\n".format(i))
                myfile.write("Username : {}\nPassword : {}\n".format(username_entry.get(), password_entry.get()))
                myfile.close()
                messagebox.showinfo("SUCCESSFUL", "You Registered Successfully")
                #sys.exit()


labels()
entries()
buttons()
show()
hide()

window.mainloop()