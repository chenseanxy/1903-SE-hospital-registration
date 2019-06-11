from tkinter import *
from tkinter import messagebox
from user import User
from patient import PatientDAO
from registration import RegistrationtDAO
from doctor import DoctorDAO
from department import DepartmentDAO
from out import out

def resultToString(result):
    doctor = DoctorDAO.get(result.did)
    dept = DepartmentDAO.get(doctor.deptID)
    if result.rtype == "pro":
        printType = "专家"
    else:
        printType = "普通"
    time = result.rtime.strftime("%Y/%m/%d %H:%M:%S")
    return f"{result.rid:8} | {time:19} | {printType:2} | {dept.deptName:<10}"

class ui_patient(object):
    def __init__(self, uid):

        self.patient = PatientDAO.get(uid)

        self.tk = Tk()
        self.tk.title("医院挂号就诊系统-病患界面")

        self.userNameText = Label(self.tk, text=f"欢迎你， {self.patient.name}")
        self.userNameText.grid(row=0, column=0, padx=5, pady=10)

        self.actionsFrame = LabelFrame(self.tk, text="操作")

        self.newRegButton = Button(self.actionsFrame, text="新建挂号", padx=20, command=self.newRegHandler)
        self.newRegButton.grid(row=0, column=0, padx=5)
        self.refresButton = Button(self.actionsFrame, text="  刷新  ", padx=20, command=self.refresHandler)
        self.refresButton.grid(row=0, column=1, padx=5)
        self.historyButton = Button(self.actionsFrame, text="查看历史", padx=20, command=self.historyHandler)
        self.historyButton.grid(row=0, column=2, padx=5)

        self.actionsFrame.grid(row=1, column=0)
    
        self.createPendingFrame()

        self.tk.mainloop()

    
    def createPendingFrame(self):
        self.pendingFrame = LabelFrame(self.tk, text="当前待就诊")

        results = RegistrationtDAO.listByPatient(self.patient.uid, False)

        rows = []
        rows.append("编号         | 时间                        | 类型 | 科室")
        for result in results:
            if result == None:
                continue
            rows.append(resultToString(result))
        
        self.pendingFrameLabels = []
        for i in range(len(rows)):
            label = Label(self.pendingFrame, text=rows[i], anchor="w", width=50)
            label.grid()
        
        self.pendingFrame.grid(row=2, column=0)


    def updatePendingFrame(self):
        self.pendingFrame.destroy()
        self.createPendingFrame()
    
    def newRegHandler(self):
        pass
    
    def refresHandler(self):
        self.patient = PatientDAO.get(self.patient.uid)
        self.updatePendingFrame()

    def historyHandler(self):
        ui_patientHistory(self.patient.uid)



class ui_patientHistory(object):
    def __init__(self, uid):
        self.patient = PatientDAO.get(uid)
        self.tk = Tk()
        self.tk.title("医院挂号就诊系统-历史挂号")

        self.createPendingFrame()
        
        self.tk.mainloop()

    def createPendingFrame(self):
        self.pendingFrame = LabelFrame(self.tk, text="历史挂号")

        results = RegistrationtDAO.listByPatient(self.patient.uid, True)

        rows = []
        rows.append("编号         | 时间                        | 类型 | 科室")
        for result in results:
            if result == None:
                continue
            rows.append(resultToString(result))
        
        self.pendingFrameLabels = []
        for i in range(len(rows)):
            label = Label(self.pendingFrame, text=rows[i], anchor="w", width=50)
            label.grid()
        
        self.pendingFrame.grid(row=0, column=0)


if __name__ == "__main__":
    ui_patient("560904")