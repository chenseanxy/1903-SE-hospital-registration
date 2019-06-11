from tkinter import *
from tkinter import messagebox
from user import User, UserDAO, getSHA256
from out import out

class ui_login(object):
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

        self.loginButton = Button(self.tk, text="Login", padx=20, command=self.loginResponce)
        self.loginButton.grid(row=3, column=0, columnspan=2, padx=5, pady=2)

        self.tk.mainloop()

    def loginResponce(self):
        out(f"[LOGIN] Username: {self.userName.get()}, Password: {self.password.get()}")
        loginResult = self.userLogin(self.userName.get(), self.password.get())
        if(type(loginResult) == User):
            out(f"[LOGIN] Successful", loginResult)
            if(loginResult.utype == "doctor"):
                
                return
            if(loginResult.utype == "patient"):

                return
        else:
            messagebox.showinfo("Login Error", "Username and/or password is incorrect, please try again")
    
    def userLogin(self, username, password):
        result = UserDAO.getByUsername(username)
        if result == None:
            out("[userLogin] Username not found", username)
            return None

        user = User(result)
        out("[userLogin] User:", user)
        
        if getSHA256(password) == user.hashPassword:
            return user

        return None

if __name__ == "__main__":
    ui_login()