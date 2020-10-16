from tkinter import *
import mysql.connector as m
mydb = m.connect( host="127.0.0.1", user="root",password="Jaatram@1729")
mc = mydb.cursor()
def create_db():
    try:
        mc.execute("create database GUI")
    except:
        print("database already created")
create_db()
mc.execute("use GUI")
def create_table():
    try:
        mc.execute("create table cred(username varchar(255),password varchar(255))")
    except:
        print("table already created")
create_table()

def register():
    global register_screen
    register_screen = Toplevel(root)
    register_screen.title("Register")
    register_screen.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(register_screen, text="Enter details below", bg="black",width="300", height="2", font=("Helvetica", 11),fg="white").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=12, height=1, bg="red", command=register_user).pack()

def login():
    global login_screen
    login_screen = Toplevel(root)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()
    global username_verify
    global password_verify
    username_verify = StringVar()
    password_verify = StringVar()
    global username_login_entry
    global password_login_entry
    Label(login_screen, text="Username ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command=login_verify).pack()

def register_user():
    username_info = username.get()
    password_info = password.get()
    mc.execute("insert into cred values(%s,%s)", (username_info, password_info))
    mydb.commit()
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    register_sucess()
#    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
    mc.execute("select username from cred")
    a=mc.fetchall()
    if (username1,) in a:
        print("select password FROM cred WHERE username='%s'"%username1)
        mc.execute("select password FROM cred WHERE username='%s'"%username1)
        b=mc.fetchall()
        if (password1,) in b:
            login_sucess()
        else:
            password_not_recognised()
    else:
        user_not_found()

def register_sucess():
    global register_success_screen
    register_screen.destroy()
    register_success_screen = Toplevel(root)
    register_success_screen.title("Success")
    register_success_screen.geometry("150x100")
    Label(register_success_screen, text="Register Success").pack()
    Button(register_success_screen, text="OK", command=delete_register_success).pack()

def login_sucess():
    global login_success_screen
    login_screen.destroy()
    login_success_screen = Toplevel(root)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()

def delete_login_success():
    login_success_screen.destroy()

def delete_register_success():
    register_success_screen.destroy()

def delete_password_not_recognised():
    password_not_recog_screen.destroy()

def delete_user_not_found_screen():
    user_not_found_screen.destroy()

def main():
    global root
    root = Tk()
    root.geometry("500x375")
    root.title("Account Login")
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