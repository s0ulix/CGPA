#importing modules

from main import *
from main import connect_db as c
c()
from tkinter import messagebox

def term1():
    global term1_f
    term1_f=Frame(frame1,bg="white",bd=5)
    term1_f.pack(side=LEFT,padx=10,pady=10)
    Label(term1_f, text="Sr No.", padx=3, pady=4).grid(row=0, column=0)
    Label(term1_f, text="Sub code", padx=3, pady=4).grid(row=0, column=1)
    Label(term1_f, text="CA1 Marks", padx=3, pady=4).grid(row=0, column=2)
    Label(term1_f, text="CA2 Marks", padx=3, pady=4).grid(row=0, column=3)
    Label(term1_f, text="CA3 Marks", padx=3, pady=4).grid(row=0, column=4)
    Label(term1_f, text="MTE Marks", padx=3, pady=4).grid(row=0, column=5)
    Label(term1_f, text="ETE Marks", padx=3, pady=4).grid(row=0, column=6)
    Label(term1_f, text="Attandence", padx=3, pady=4).grid(row=0, column=7)
    Label(term1_f, text="Practical", padx=3, pady=4).grid(row=0, column=8)
    Label(term1_f, text="Obtained Marks", padx=3, pady=4).grid(row=0, column=9)


def term2():
    global term2_f
    term2_f=Frame(frame1,bg="white",bd=5)
    term2_f.pack(side=RIGHT,padx=10,pady=10)
    Label(term2_f, text="Sr No.", padx=3, pady=4).grid(row=0, column=1)
    Label(term2_f, text="Sub code", padx=3, pady=4).grid(row=0, column=2)
    Label(term2_f, text="CA1 Marks", padx=3, pady=4).grid(row=0, column=3)
    Label(term2_f, text="CA2 Marks", padx=3, pady=4).grid(row=0, column=4)
    Label(term2_f, text="CA3 Marks", padx=3, pady=4).grid(row=0, column=5)
    Label(term2_f, text="MTE Marks", padx=3, pady=4).grid(row=0, column=6)
    Label(term2_f, text="ETE Marks", padx=3, pady=4).grid(row=0, column=7)
    Label(term2_f, text="Attandence", padx=3, pady=4).grid(row=0, column=8)
    Label(term2_f, text="Practical", padx=3, pady=4).grid(row=0, column=9)
    Label(term2_f, text="Obtained Marks", padx=3, pady=4).grid(row=0, column=10)


def year_frame():
    global frame1
    frame1=Frame(root,width=720,bg="blue")
    frame1.pack(padx=4,pady=4)
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

