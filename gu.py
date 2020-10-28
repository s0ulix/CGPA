#importing modules
from main import *
from main import connect_db as c
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile
import pickle
c()

def calculate():
    global sub_marks
    for a,j in enumerate(cont):
        if(sub_marks[a*8].get()>30):
            messagebox.showerror(title="Limit exceed",message="Max marks for CA1 is 30")
        else:
            ca1=sub_marks[a*8].get()
        if (sub_marks[a * 8+1].get() > 30):
            messagebox.showerror(title="Limit exceed", message="Max marks for CA2 is 30")
        else:
            ca2 = sub_marks[a * 8+1].get()
        if (sub_marks[a * 8+2].get() > 30):
            messagebox.showerror(title="Limit exceed", message="Max marks for CA3 is 30")
        else:
            ca3 = sub_marks[a * 8+2].get()
        if (sub_marks[a * 8+3].get() > 40):
            messagebox.showerror(title="Limit exceed", message="Max marks for MTE is 40")
        else:
            mte = sub_marks[a * 8+3].get()
        if (sub_marks[a * 8+4].get() > 70):
            messagebox.showerror(title="Limit exceed", message="Max marks for ETE is 70")
        else:
            ete = sub_marks[a * 8+4].get()
        if (sub_marks[a * 8+5].get() > 100):
            messagebox.showerror(title="Limit exceed", message="Max Attandence is 100%")
        else:
            att = sub_marks[a * 8+5].get()
        if (sub_marks[a * 8+6].get() > 100):
            messagebox.showerror(title="Limit exceed", message="Max marks for practical is 100")
        else:
            prac = sub_marks[a * 8+6].get()
        prac=prac*(cont[j][4]/100)
        ete=ete*(cont[j][2]/70)
        mte=mte*(cont[j][1]/40)
        if(att>=90):
            att=5
        elif(att>=85):
            att=4
        elif(att>=80):
            att=3
        elif(att>=75):
            att=2
        else:
            sub_marks[(a+1)*8-1].set(0)
            continue
        att=att*(cont[j][3]/5)
        if(ca1>=ca2):
            ca=ca1
            if(ca2>=ca3):
                ca=ca+ca2
            else:
                ca=ca+ca3
        else:
            ca=ca2
            if(ca1>=ca3):
                ca=ca+ca1
            else:
                ca=ca+ca3
        ca=ca*(cont[j][0]/60)
        obt=prac+ete+mte+att+ca
        sub_marks[(a+1)*8-1].set(obt)


def fileopen():
    file=askopenfile(mode='rb')
    global cont
    cont=pickle.load(file)
    file.close()

def create():
    file_input.destroy()
    configw.destroy()
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


def head(n,c,d):
    Label(c, text="" ,bg="#454545").grid(row=(2+d), column=0)
    Label(c, text="",bg="#454545").grid(row=(3+d), column=0)
    count = 1
    for i in n:
        Label(c, text=i, padx=3, pady=4).grid(row=(3+d), column=count)
        count += 1


def add_subject(a,c,d):
    global sub_wht
    global count1
    if (count1 > 10):
        messagebox.showinfo(title="Limit exceed", message="You can add only 10 subjects")
        return

    sub_wht.append(StringVar())
    Entry(c, width="8", textvariable=sub_wht[-1]).grid(row=3 + count1+d, column=2)
    Label(c, text=" %d  " % count1).grid(row=3 + count1+d, column=1)
    count = 3
    for i in range(1, len(a)-1):
        sub_wht.append(IntVar())
        Entry(c, width="4", textvariable=sub_wht[-1]).grid(row=3 + count1+d, column=count)
        count += 1
    count1 += 1

def add_s():
    global a
    global count1
    add_subject(a,configw,0)

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
    Button(configw,text="Add", height="1", width="4", font=("Helvetica", 13), bg="#008080", fg="white", command=add_s).grid(row=1, column=1)
    Button(configw,text="Save", height="1", width="5", font=("Helvetica", 13), bg="#008080", fg="white", command=save).grid(row=1, column=7)
    Button(configw,text="Reset", height="1", width="5", font=("Helvetica", 13), bg="#008080", fg="white", command=reset).grid(row=1, column=4)
    head(a,configw,0)
    configw.mainloop()

def cn():
    config_window()

def add_sub(a,c,d,i,j):
    global sub_marks
    global count1
    Label(c, text=i).grid(row=3 + count1 + d, column=2)
    Label(c, text=" %d  " % j).grid(row=3 + count1 + d, column=1)
    count = 3
    for i in range(1, len(a)-2):
        sub_marks.append(IntVar())
        Entry(c, width="4", textvariable=sub_marks[-1]).grid(row=3 + count1 + d, column=count)
        count += 1
    sub_marks.append(StringVar())
    Entry(c, width="4", textvariable=sub_marks[-1]).grid(row=3 + count1 + d, column=count)
    count1 += 1

def add_term():
    global sub
    if(sub>10):
        messagebox.showerror(title="Sem error",message="No more than 2 semster")
    else:
        a = ["Sr No. ", "Sub code", "CA1 Marks","CA2 Marks","CA3 Marks", "MTE Marks", "ETE Marks", "Attandence", "Practical","Obtainde Marks"]
        head(a,root,sub)
        for j,i in enumerate(cont):
            add_sub(a,root,sub,i,j+1)
        sub=sub+10

def resetm():
    global sub_marks
    for i in sub_marks:
        i.set(0)

def cgpa_calc():
    global root
    root = Tk()
    logo = PhotoImage(file='logo.png')
    root.configure(bg="grey")
    root.geometry("700x450")
    root.title("CGPA Calculator")
    root.iconphoto(False, logo)
    backgound = PhotoImage(file='bg2.png')
    Label(root, image=backgound).place(x=0, y=0, relwidth=1, relheight=1)
    global sub
    sub=0
    global cont
    file=open('configw','rb')
    cont=pickle.load(file)
    file.close()
    global count1
    count1=1
    global sub_marks
    sub_marks = []

    Button(root,text="Calculate",command=calculate).grid(row=1,column=10)


    menubar = Menu(root)
    file = Menu(menubar, tearoff=0)
    menubar.add_cascade(label='File', menu=file)
    file.add_command(label='Save', command=None)
    file.add_command(label='Reset', command=resetm)
    file.add_command(label='Add year', command=add_term)
    file.add_separator()
    file.add_command(label='Exit', command=root.destroy)

    config = Menu(menubar, tearoff=0)
    menubar.add_cascade(label='Config', menu=config)
    config.add_command(label='New config', command=cn)
    config.add_separator()
    config.add_command(label='Import config', command=fileopen)

    help = Menu(menubar, tearoff=0)
    menubar.add_cascade(label='Help', menu=help)
    help.add_command(label='Contact Us', command=None)
    help.add_command(label='Faq', command=None)


    root.config(menu=menubar)
    root.mainloop()
if(check_login):
    cgpa_calc()

