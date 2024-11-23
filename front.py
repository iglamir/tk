from dbm import error
from doctest import master

import password
import self

import sqlite_code
import tkinter
import messagebox
import front2
import user


class loginPage:
    def __init__(self , root):
        self.root = root
        self.root.title("صفحه ورود")
        self.root.geometry("450x300")
        self.root.config(bg='#eae202')
        self.lable_username = tkinter.Label(master=root , text ='username', font=("Arial", 13))
        self.lable_username.config(bg='#eae202')
        self.lable_username.place(x = 40, y = 100)
        self.lable_password = tkinter.Label(master=root, text='password', font=("Arial", 13))
        self.lable_password.config(bg='#eae202')
        self.lable_password.place(x=40, y=150)
        self.entry_username = tkinter.Entry(master=root, width=20 ,font=("Arial", 13))
        self.entry_username.place(x=120, y=102)
        self.entry_password = tkinter.Entry(master=root, width=20, font=("Arial", 13))
        self.entry_password.place(x=120, y=152)
        self.button = tkinter.Button(master = root , text = 'Login' , font=("Arial", 13) , width=10 , command=self.login)
        self.button.place(x=200, y=190)
        self.button = tkinter.Button(master = root , text = 'sign' , font=("Arial", 13) , width=10 , command=self.rej)
        self.button.place(x=100, y=190)
    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        user = sqlite_code.select_from_db_user(username=username)
        if user is not None:
            if user[2] == password:
                messagebox.showinfo('correct' , f'{username} Wellcome')
                self.root.destroy()
                second =tkinter.Tk()
                example = front2.Book(second)
            else:
                messagebox.showerror('error' ,'wrong password or username ')
        else:
            messagebox.showerror('wrong' , 'wrong password or wrong username')
    def rej(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        user = sqlite_code.select_from_db_user(username=username)
        if len(username.strip()) >1 and len(password.strip()) >5:
            if user is not None:
                messagebox.showerror('error' , 'username is taken')
            else:
                messagebox.showinfo('success', f'{username} Wellcome')
            result = sqlite_code.add_to_database(username=username, password=password)
            self.root.destroy()
            second = tkinter.Tk()
            example = front2.Book(second)
        else:
            messagebox.showerror('error' , 'please insert correct username and password')





if __name__ =='__main__':
    window = tkinter.Tk()
    app = loginPage(root=window)
    window.mainloop()

