from tkinter import *
from tkinter import messagebox
from user import User, UserDAO, getSHA256
from out import out
from ui_patient import ui_patient
from ui_doctor import ui_doctor

class ui_login(object):
    def __init__(self):

        self.tk = Tk()
        self.tk.title("医院挂号就诊系统-登陆界面")

        self.userNameText = Label(self.tk, text="欢迎！请您登陆。")
        self.userNameText.grid(row=0, column=0, columnspan=2, padx=5)

        self.userNameText = Label(self.tk, text="用户名", anchor="e", width=10)
        self.userNameText.grid(row=1, column=0, padx=5)
        self.userName = Entry(self.tk, width=40)
        self.userName.grid(row=1, column=1, padx=5)

        self.passwordText = Label(self.tk, text="密码", anchor="e", width=10)
        self.passwordText.grid(row=2, column=0, padx=5)
        self.password = Entry(self.tk, width=40)
        self.password.grid(row=2, column=1, padx=5)

        self.loginButton = Button(self.tk, text="登录", padx=20, command=self.loginResponce)
        self.loginButton.grid(row=3, column=0, columnspan=2, padx=5, pady=2)

        self.tk.mainloop()

    def loginResponce(self):
        out(f"[LOGIN] Username: {self.userName.get()}, Password: {self.password.get()}")
        loginResult = self.userLogin(self.userName.get(), self.password.get())
        if(type(loginResult) == User):
            out(f"[LOGIN] Successful", loginResult)
            if(loginResult.utype == "doctor"):
                ui_doctor(loginResult.uid)
                return
            if(loginResult.utype == "patient"):
                ui_patient(loginResult.uid)
                return
        else:
            messagebox.showinfo("登陆失败", "请检查您的用户名和密码后，再试一次")
    
    def userLogin(self, username, password):
        user = UserDAO.getByUsername(username)
        if user == None:
            out("[userLogin] Username not found", username)
            return None

        out("[userLogin] User:", user)
        
        if getSHA256(password) == user.hashPassword:
            return user

        return None

if __name__ == "__main__":
    ui_login()