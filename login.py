from tkinter import *


def register_user():
    username_info = username.get()
    password_info = password.get()

    file = open(username_info+".txt", "w")
    file.write(username_info)
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(text="registeration successful!")


def register():
    screen1 = Toplevel(screen)
    screen1.title("register")
    screen1.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(screen1, text="please enter your details below").pack()
    Label(screen1, text="Username * ").pack()
    username_entry = Entry(screen1, textvariable=username)
    username_entry.pack()
    Label(screen1, text="Password * ").pack()
    password_entry = Entry(screen1, textvariable=password)
    password_entry.pack()
    Label(screen1, text="")

    Button(screen1="Register", width=10,
           height=1, command=register_user).pack()


def login():
    print("login session started")


def main_screen():
    global screen
    screen = Tk()
    screen.geometry('300x250')
    screen.title("Notes 1.0")
    Label(text="Notes 1.0", bg="grey", height="2",
          width="300", font=("Calibri", 13)).pack()
    Label(Text="")
    # create two buttons
    Button(text="Login", height="2", width="30", command=login).pack()
    Button(Text="Register", height="2", width="30" command=register).pack()

    screen.mainloop()


main_screen()
