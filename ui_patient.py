from tkinter import *
from tkinter import messagebox
from user import User
from patient import PatientDAO
from registration import RegistrationtDAO, Registration
from doctor import DoctorDAO
from department import DepartmentDAO
from out import out
from ui_newReg import ui_newReg

def rtypePrint(rtype):
    if rtype == "pro":
        printType = "专家"
    else:
        printType = "普通"
    return printType

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
        self.createDetailedFrame()

        self.tk.mainloop()

    
    def createPendingFrame(self):
        self.pendingFrame = LabelFrame(self.tk, text="当前待就诊")

        results = RegistrationtDAO.listByPatient(self.patient.uid, False)
        results.sort(key=Registration.getRTime)

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
    
    def createDetailedFrame(self):
        self.detailedFrame = LabelFrame(self.tk, text="挂号详情")
        self.detailedSelect = StringVar(self.detailedFrame)
        results = RegistrationtDAO.listByPatient(self.patient.uid, False)
        results.sort(key=Registration.getRTime)
        self.detailedList = []
        for result in results:
            self.detailedList.append(resultToString(result))
            out(resultToString(result))
        self.detailedSelect.set(self.detailedList[0])
        self.detailedOption = OptionMenu(self.detailedFrame, self.detailedSelect, *self.detailedList, command=self.updateInfoFrame)
        self.detailedOption.config(width=43)
        self.detailedOption.grid(row=0, column=1, padx=5)

        self.createInfoFrame()

        self.detailedFrame.grid(row=3, column=0)
                

    def updateDetailedFrame(self):
        self.detailedFrame.destroy()
        self.createDetailedFrame()

    def selectedRID(self):
        return str(int(self.detailedSelect.get().split("|")[0]))

    def createInfoFrame(self):
        self.infoFrame = Frame(self.detailedFrame)
        reg = RegistrationtDAO.get(self.selectedRID())
        doc = DoctorDAO.get(reg.did)
        dept = DepartmentDAO.get(doc.deptID)

        Label(self.infoFrame, text="挂号编号", width=13, anchor="e").grid(row=0, column=0)
        Label(self.infoFrame, text=reg.rid, width=30, anchor="w").grid(row=0, column=1)

        Label(self.infoFrame, text="挂号时间", width=13, anchor="e").grid(row=1, column=0)
        Label(self.infoFrame, text=reg.rtime.strftime("%Y/%m/%d %H:%M:%S"), width=30, anchor="w").grid(row=1, column=1)

        Label(self.infoFrame, text="挂号类型", width=13, anchor="e").grid(row=2, column=0)
        Label(self.infoFrame, text=rtypePrint(reg.rtype), width=30, anchor="w").grid(row=2, column=1)

        Label(self.infoFrame, text="科室名称", width=13, anchor="e").grid(row=3, column=0)
        Label(self.infoFrame, text=dept.deptName, width=30, anchor="w").grid(row=3, column=1)

        Label(self.infoFrame, text="科室地点", width=13, anchor="e").grid(row=4, column=0)
        Label(self.infoFrame, text=dept.location, width=30, anchor="w").grid(row=4, column=1)

        Label(self.infoFrame, text="科室电话", width=13, anchor="e").grid(row=5, column=0)
        Label(self.infoFrame, text=dept.phone, width=30, anchor="w").grid(row=5, column=1)

        Label(self.infoFrame, text="医生名称", width=13, anchor="e").grid(row=6, column=0)
        Label(self.infoFrame, text=doc.name, width=30, anchor="w").grid(row=6, column=1)

        self.infoFrame.grid(row=1, columnspan=2)

    def updateInfoFrame(self, *args):
        self.infoFrame.destroy()
        self.createInfoFrame()

    def newRegHandler(self):
        ui_newReg(self.patient.uid)
    
    def refresHandler(self):
        self.patient = PatientDAO.get(self.patient.uid)
        self.updatePendingFrame()
        self.updateDetailedFrame()

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
        results.sort(key=Registration.getRTime)

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
    ui_patient("592536")