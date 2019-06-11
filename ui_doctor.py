from tkinter import *
from tkinter import messagebox
from user import User
from doctor import Doctor, DoctorDAO
from out import out

class ui_login(object):
    def __init__(self, uid):

        doc = DoctorDAO.get(uid)
        doc = Doctor()

        self.tk = Tk()
        self.tk.title("Doctor Page")

        self.userNameText = Label(self.tk, text=f"Welcome! Doctor {doc.name}")
        self.userNameText.grid(row=0, column=0, columnspan=2, padx=5)

        self.userNameText = Label(self.tk, text="User Name", anchor="e", width=10)
        self.userNameText.grid(row=1, column=0, padx=5)
        self.userName = Entry(self.tk, width=40)
        self.userName.grid(row=1, column=1, padx=5)

        self.passwordText = Label(self.tk, text="Password", anchor="e", width=10)
        self.passwordText.grid(row=2, column=0, padx=5)
        self.password = Entry(self.tk, width=40)
        self.password.grid(row=2, column=1, padx=5)

        self.loginButton = Button(self.tk, text="Login", padx=20, command=self.loginResponce)
        self.loginButton.grid(row=3, column=0, columnspan=2, padx=5, pady=2)

        self.tk.mainloop()

    def loginResponce(self):
        pass

if __name__ == "__main__":
    ui_login("430470")