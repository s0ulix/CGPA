#importing module
from tkinter import *
from tkinter import messagebox
import mysql.connector as m
from hashlib import md5


#connecting to database
def connect_db():
    try:                                           #error handling for databse connection
        global mydb
        mydb = m.connect( host="127.0.0.1", user="root",password="Jaatram@1729")
    except:
        warning="Check if database is started or not \n If started enter your creds in command line"
        messagebox.showwarning(title="Db error",message=warning)
        h=input("enter host: ")
        u=input("enter username: ")
        p=input("enter password: ")
        mydb = m.connect(host=h, user=u, password=p)
    global mc
    mc = mydb.cursor()

    #creating database
    def create_db():
        try:                                          #error handling if databse is there
            mc.execute("create database GUI")
        except:
            print("database already created")
    create_db()

    #using database
    mc.execute("use GUI")

    #creating table
    def create_table():
        try:                                         #error handling if table is there
            mc.execute("create table creds(username int,password varchar(255))")
        except:
            print("table already created")
    create_table()

#register screen
def register():

    #gui window configs
    global register_screen
    register_screen = Toplevel(root)
    register_screen.title("Register")
    register_screen.geometry("300x250")
    register_screen.iconphoto(False,logo)

    #declaring variables
    global username
    global password
    global username_entry
    global password_entry
    username = IntVar()
    password = StringVar()

    #Lables and entryboxes
    Label(register_screen, text="Enter details below", bg="black",width="300", height="2", font=("Helvetica", 11),fg="white").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Registration ID ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    username_entry.delete(0, END)
    password_lable = Label(register_screen, text="Password ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=12, height=1, bg="red", command=register_user).pack()

def login():

    # gui config for login screen
    global login_screen
    login_screen = Toplevel(root)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    login_screen.iconphoto(False,logo)

    #Declaring variables
    global username_verify
    global password_verify
    username_verify = IntVar()
    password_verify = StringVar()
    global username_login_entry
    global password_login_entry

    #labels and entryboxes
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Registration ID ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    username_login_entry.delete(0, END)
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command=login_verify).pack()

def register_user():
    try:
        username_info = username.get()
        unhashed_passwd = password.get()                                 # getting password
        if len(unhashed_passwd)<8:
            messagebox.showerror(title="Password eroor",message="Password must contain min 8 letters")
        else:
            password_info = (md5(unhashed_passwd.encode())).hexdigest()  # creating hash of password
            mc.execute("select username from creds")
            a = mc.fetchall()
            if (username_info,) in a:  # checking is user exist or not
                user_exist()
            else:
                mc.execute("insert into creds values(%s,%s)", (username_info, password_info))
                mydb.commit()
                register_sucess()
    except:
        messagebox.showerror(title="Error", message="ID should be numeric")
        register_screen.destroy()
        register()


def login_verify():
    username1 = username_verify.get()                            #getting id
    unhashed_passwd = password_verify.get()                      #getting password
    password1 = (md5(unhashed_passwd.encode())).hexdigest()      #creating hash of password
    mc.execute("select username from creds")
    a=mc.fetchall()
    if (username1,) in a:                                        # Checking username
        mc.execute("select password FROM creds WHERE username=%d"%username1)
        b=mc.fetchall()
        if (password1,) in b:                                    #checking password
            login_sucess()
        else:
            password_not_recognised()
    else:
        user_not_found()

#Messageboxes
def register_sucess():
    register_screen.destroy()
    messagebox.showinfo(title="Success", message="ID Registered Successfully")

def user_exist():
    user_exist_message = messagebox.showwarning(title="Warning", message="Registration ID Already exist")

def login_sucess():
    login_screen.destroy()
    #root.destroy()
    login_success_message= messagebox.showinfo(title="Success",message="Login Success")

def password_not_recognised():
    password_not_recognised_message = messagebox.showerror(title="Error", message="Invalid Password")

def user_not_found():
    user_not_found_message = messagebox.showerror(title="Error", message="ID not found")

def main():

    #Main gui config
    global logo
    global root
    root = Tk()
    logo = PhotoImage(file='logo.png')
    root.geometry("500x375")
    root.title("Account Login")
    root.iconphoto(False,logo)

    connect_db()                             #starting db connection

    #lablels and buttons
    Label(text="CGPA Calculator", bg="Black", width="500", height="2", font=("Helvetica", 13), fg="white").pack()
    Label(text="").pack()
    Button(text="Login", height="3", width="40",font=("Helvetica", 13), command=login).pack()
    Label(text="").pack()
    Button(text="Register", height="3", width="40",font=("Helvetica", 13), command=register).pack()
    Label(text="").pack()
    Label(text="").pack()
    Label(text="* New user must register", bg="Red", width="20", height="2", font=("Helvetica", 13), fg="black").pack()
    root.mainloop()

main()