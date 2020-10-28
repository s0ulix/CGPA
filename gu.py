#importing modules
from main import *
from main import connect_db as c
from tkinter import *
from tkinter import messagebox
import pickle
c()


def create():
    file_input.destroy()
    config.destroy()
    file = open(name.get(), "ab")
    pickle.dump(conf, file)
    file.close()


def makefile():
    global file_input
    file_input=Toplevel(configw)
    global name
    name=StringVar()
    Label(file_input,text="Enter name of file").grid()
    Entry(file_input,textvariable=name).grid()
    Button(file_input,text="Done",command=create).grid()
    file_input.mainloop()


def reset():
    global sub_wht
    for i in sub_wht:
        i.set(0)

def save():
    global sub_wht
    global conf
    conf = {}
    st = sub_wht[0].get()
    ls = []
    for i in sub_wht[1::]:
        if (isinstance(i.get(), str)):
            if (sum(ls) == 100):
                conf[st] = ls
                st = i.get()
                ls = []
            else:
                messagebox.showerror(title="Weightage incorrect", message="Sum of wightage in %s is not 100" % st)
                return
        else:
            ls.append(i.get())
    if (sum(ls) == 100):
        conf[st] = ls
        ls = []
    else:
        messagebox.showerror(title="Weightage incorrect", message="Sum of wightage in %s is not 100" % st)
        return
    makefile()


def head():
    global a
    Label(configw, text="" ,bg="#454545").grid(row=2, column=0)
    Label(configw, text="",bg="#454545").grid(row=3, column=0)
    count = 1
    for i in a:
        Label(configw, text=i, padx=3, pady=4).grid(row=3, column=count)
        count += 1


def add_subject():
    global count1
    global sub_wht
    if (count1 > 10):
        messagebox.showinfo(title="Limit exceed", message="You can add only 10 subjects")
        return

    sub_wht.append(StringVar())
    Entry(configw, width="8", textvariable=sub_wht[-1]).grid(row=3 + count1, column=2)
    Label(configw, text=" %d  " % count1).grid(row=3 + count1, column=1)
    count = 3
    ent = []
    for i in range(1, 6):
        sub_wht.append(IntVar())
        Entry(configw, width="4", textvariable=sub_wht[-1]).grid(row=3 + count1, column=count)
        count += 1
    count1 += 1


def config_window():
    global configw
    configw = Toplevel(root)
    logo = PhotoImage(file='logo.png')
    configw.configure(bg="#454545")
    configw.geometry("440x320")
    configw.title("Config")
    configw.iconphoto(False, logo)
    backgound=PhotoImage(file='bg1.png')
    Label(configw,image=backgound).place(x=0,y=0,relwidth=1,relheight=1)

    global count1
    global a
    global sub_wht
    sub_wht = []
    count1 = 1
    a = ["Sr No. ", "Sub code", "CA Marks", "MTE Marks", "ETE Marks", "Attandence","Practical"]
    Label(configw,bg="#454545").grid(row=0,column=0)
    Button(configw,text="Add", height="1", width="4", font=("Helvetica", 13), bg="#008080", fg="white", command=add_subject).grid(row=1, column=1)
    Button(configw,text="Save", height="1", width="5", font=("Helvetica", 13), bg="#008080", fg="white", command=save).grid(row=1, column=7)
    Button(configw,text="Reset", height="1", width="5", font=("Helvetica", 13), bg="#008080", fg="white", command=reset).grid(row=1, column=4)
    head()
    configw.mainloop()

def cn():
    config_window()

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
    config.add_command(label='New config', command=cn)
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

