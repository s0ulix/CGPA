#importing modules

from main import *
from main import connect_db as c
c()
from tkinter import messagebox

def term1():
    global term1_f
    term1_f=Frame(frame1)
    term1_f.pack(side=LEFT)


def term2():
    global term2_f
    term2_f=Frame(frame1)
    term2_f.pack(side=RIGHT)

def year_frame():
    global frame1
    frame1=Frame(root)
    frame1.pack()
    term1()
    term2()

def cgpa_calc():
    global root
    root = Tk()
    logo = PhotoImage(file='logo.png')
    root.configure(bg="grey")
    root.geometry("1280x720")
    root.title("CGPA Calculator")
    root.iconphoto(False, logo)


    menubar = Menu(root)
    file = Menu(menubar, tearoff=0)
    menubar.add_cascade(label='File', menu=file)
    file.add_command(label='Save', command=None)
    file.add_command(label='Reset', command=None)
    file.add_command(label='Add year', command=year_frame)
    file.add_separator()
    file.add_command(label='Exit', command=root.destroy)

    config = Menu(menubar, tearoff=0)
    menubar.add_cascade(label='Config', menu=config)
    config.add_command(label='New config', command=None)
    config.add_separator()
    config.add_command(label='Import config', command=None)

    help = Menu(menubar, tearoff=0)
    menubar.add_cascade(label='Help', menu=help)
    help.add_command(label='Contact Us', command=None)
    help.add_command(label='Faq', command=None)


    root.config(menu=menubar)
    root.mainloop()
if(check_login):
    cgpa_calc()

