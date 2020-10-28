from tkinter import *
from tkinter import messagebox
import pickle

def create():
    file_input.destroy()
    config.destroy()
    file = open(name.get(), "ab")
    pickle.dump(conf, file)
    file.close()


def makefile():
    global file_input
    file_input=Toplevel(config)
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


def head(n):
    Label(config, text="" ,bg="#454545").grid(row=2, column=0)
    Label(config, text="",bg="#454545").grid(row=3, column=0)
    count = 1
    for i in n:
        Label(config, text=i, padx=3, pady=4).grid(row=3, column=count)
        count += 1


def add_subject():
    global count1
    global sub_wht
    if (count1 > 10):
        messagebox.showinfo(title="Limit exceed", message="You can add only 10 subjects")
        return

    sub_wht.append(StringVar())
    Entry(config, width="8", textvariable=sub_wht[-1]).grid(row=3 + count1, column=2)
    Label(config, text=" %d  " % count1).grid(row=3 + count1, column=1)
    count = 3
    ent = []
    for i in range(1, 6):
        sub_wht.append(IntVar())
        Entry(config, width="4", textvariable=sub_wht[-1]).grid(row=3 + count1, column=count)
        count += 1
    count1 += 1


def config_window():
    global config
    config = Tk()
    logo = PhotoImage(file='logo.png')
    config.configure(bg="#454545")
    config.geometry("440x320")
    config.title("Config")
    config.iconphoto(False, logo)
    backgound=PhotoImage(file='bg1.png')
    Label(config,image=backgound).place(x=0,y=0,relwidth=1,relheight=1)

    global count1
    global a
    global sub_wht
    sub_wht = []
    count1 = 1
    a = ["Sr No. ", "Sub code", "CA Marks", "MTE Marks", "ETE Marks", "Attandence","Practical"]
    Label(bg="#454545").grid(row=0,column=0)
    Button(text="Add", height="1", width="4", font=("Helvetica", 13), bg="#008080", fg="white", command=add_subject).grid(row=1, column=1)
    Button(text="Save", height="1", width="5", font=("Helvetica", 13), bg="#008080", fg="white", command=save).grid(row=1, column=7)
    Button(text="Reset", height="1", width="5", font=("Helvetica", 13), bg="#008080", fg="white", command=reset).grid(row=1, column=4)
    head(a)
    config.mainloop()


config_window()
