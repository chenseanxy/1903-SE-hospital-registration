from tkinter import *
from tkinter import messagebox
from login_backend import userLogin
from entities import User

class login(object):
    def __init__(self):

        self.tk = Tk()
        self.tk.title("Login Page")

        self.userNameText = Label(self.tk, text="Welcome! Please login.")
        self.userNameText.grid(row=0, column=0, columnspan=2, padx=5)

        self.userNameText = Label(self.tk, text="User Name", anchor="e", width=10)
        self.userNameText.grid(row=1, column=0, padx=5)
        self.userName = Entry(self.tk, width=40)
        self.userName.grid(row=1, column=1, padx=5)

        self.passwordText = Label(self.tk, text="Password", anchor="e", width=10)
        self.passwordText.grid(row=2, column=0, padx=5)
        self.password = Entry(self.tk, width=40)
        self.password.grid(row=2, column=1, padx=5)

        self.loginButton = Button(self.tk, text="Login", padx=20, command=self.loginCheck)
        self.loginButton.grid(row=3, column=0, columnspan=2, padx=5, pady=2)

        self.tk.mainloop()

    def loginCheck(self):
        print(f"[LOGIN] Username: {self.userName.get()}, Password: {self.password.get()}")
        loginResult = userLogin(self.userName.get(), self.password.get())
        if(type(loginResult) == User):
            print(f"[LOGIN] Successful", loginResult)
            if(loginResult.utype == "doctor"):
                
                return
            if(loginResult.utype == "patient"):

                return
        else:
            messagebox.showinfo("Login Error", "Username and/or password is incorrect, please try again")
            


if __name__ == "__main__":
    login()