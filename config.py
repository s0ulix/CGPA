from tkinter import *
from tkinter import messagebox
import pickle

def head(n):
    Label(config,text=" ",bg="#454545").grid(row=1,column=0)
    Label(config, text=" ", bg="#454545").grid(row=2, column=0)
    count=1
    for i in n:
        Label(config,text=i,padx=3, pady=4).grid(row=2,column=count)
        count+=1

def add_subject():
    global count1
    if(count1>20):
        messagebox.showinfo(title="Limit exceed",message="You can add only 20 subjects")
        return
    global a
    Label(config, text=" %d  " %count1).grid(row=2+count1,column=1)
    count = 2
    for i in range(len(a)-1):2
        Entry(config,width="4").grid(row=2+count1,column=count)
        count+=1
    count1 +=1

def config_window():
    global config
    config=Tk()
    logo = PhotoImage(file='logo.png')
    config.configure(bg="#454545")
    config.geometry("590x510")
    config.title("Config")
    config.iconphoto(False, logo)

    global count1
    global a
    count1=1
    a=["Sr No. ","Sub code","CA1 Marks","CA2 Marks","CA3 Marks","MTE Marks","ETE Marks","Attandence","Practical"]
    Button(text="Add", height="1", width="4", font=("Helvetica", 13),bg="#008080",fg="white", command=add_subject).grid(row=0,column=1)
    head(a)
    config.mainloop()
config_window()