from tkinter import *
from tkinter import messagebox
from user import User
from doctor import Doctor, DoctorDAO
from registration import Registration, RegistrationtDAO
from patient import PatientDAO
from out import out
from ui_patient import rtypePrint


def doctorResultToString(result):
    patient = PatientDAO.get(result.pid)
    if result.rtype == "pro":
        printType = "专家"
    else:
        printType = "普通"
    time = result.rtime.strftime("%Y/%m/%d %H:%M:%S")
    return f"{result.rid:8} | {time:19} | {printType:2} | {patient.name:<10}"

class ui_doctor(object):
    def __init__(self, uid):

        self.doc = DoctorDAO.get(uid)

        self.tk = Tk()
        self.tk.title("医院挂号就诊系统-医生界面")

        self.userNameText = Label(self.tk, text=f"欢迎你， {self.doc.name}")
        self.userNameText.grid(row=0, column=0, columnspan=2, padx=5)

        self.actionsFrame = LabelFrame(self.tk, text="操作")

        self.refresButton = Button(self.actionsFrame, text="  刷新  ", padx=20, command=self.refresHandler)
        self.refresButton.grid(row=0, column=0, padx=5)
        self.historyButton = Button(self.actionsFrame, text="查看历史", padx=20, command=self.historyHandler)
        self.historyButton.grid(row=0, column=1, padx=5)

        self.actionsFrame.grid(row=1, column=0)
    
        self.createPendingFrame()
        self.createDetailedFrame()

        self.tk.mainloop()

    def refresHandler(self):
        self.doc = DoctorDAO.get(self.doc.uid)
        self.updatePendingFrame()
        self.updateDetailedFrame()

    def historyHandler(self):
        ui_doctorHistory(self.doc.uid)

    def createPendingFrame(self):
        self.pendingFrame = LabelFrame(self.tk, text="当前待就诊")

        results = RegistrationtDAO.listByDoctor(self.doc.uid, False)
        results.sort(key=Registration.getRTime)

        rows = []
        rows.append("编号         | 时间                        | 类型 | 患者姓名")
        for result in results:
            if result == None:
                continue
            rows.append(doctorResultToString(result))
        
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
        results = RegistrationtDAO.listByDoctor(self.doc.uid, False)
        results.sort(key=Registration.getRTime)
        self.detailedList = []
        for result in results:
            self.detailedList.append(doctorResultToString(result))
            out(doctorResultToString(result))
        self.detailedSelect.set(self.detailedList[0])
        self.detailedOption = OptionMenu(self.detailedFrame, self.detailedSelect, *self.detailedList, command=self.updateInfoFrame)
        self.detailedOption.config(width=43)
        self.detailedOption.grid(row=0, column=1, padx=5)

        self.createInfoFrame()

        self.doneButton = Button(self.detailedFrame, text="开始诊断", padx=10, command=self.doneHandler)
        self.doneButton.grid(row=2, column=0, columnspan=2)
        self.detailedFrame.grid(row=3, column=0)
                
    def doneHandler(self):
        reg = RegistrationtDAO.get(self.selectedRID())
        reg.done = True
        RegistrationtDAO.update(reg)
        self.refresHandler()

    def updateDetailedFrame(self):
        self.detailedFrame.destroy()
        self.createDetailedFrame()

    def selectedRID(self):
        return str(int(self.detailedSelect.get().split("|")[0]))

    def createInfoFrame(self):
        self.infoFrame = Frame(self.detailedFrame)
        reg = RegistrationtDAO.get(self.selectedRID())
        patient = PatientDAO.get(reg.pid)

        Label(self.infoFrame, text="挂号编号", width=13, anchor="e").grid(row=0, column=0)
        Label(self.infoFrame, text=reg.rid, width=30, anchor="w").grid(row=0, column=1)

        Label(self.infoFrame, text="挂号时间", width=13, anchor="e").grid(row=1, column=0)
        Label(self.infoFrame, text=reg.rtime.strftime("%Y/%m/%d %H:%M:%S"), width=30, anchor="w").grid(row=1, column=1)

        Label(self.infoFrame, text="挂号类型", width=13, anchor="e").grid(row=2, column=0)
        Label(self.infoFrame, text=rtypePrint(reg.rtype), width=30, anchor="w").grid(row=2, column=1)

        Label(self.infoFrame, text="患者名称", width=13, anchor="e").grid(row=3, column=0)
        Label(self.infoFrame, text=patient.name, width=30, anchor="w").grid(row=3, column=1)

        Label(self.infoFrame, text="患者电话", width=13, anchor="e").grid(row=4, column=0)
        Label(self.infoFrame, text=patient.phone, width=30, anchor="w").grid(row=4, column=1)

        self.infoFrame.grid(row=1, columnspan=2)

    def updateInfoFrame(self, *args):
        self.infoFrame.destroy()
        self.createInfoFrame()

class ui_doctorHistory(object):
    def __init__(self, uid):
        self.doc = DoctorDAO.get(uid)
        self.tk = Tk()
        self.tk.title("医院挂号就诊系统-历史查询")

        self.createPendingFrame()
        
        self.tk.mainloop()

    def createPendingFrame(self):
        self.pendingFrame = LabelFrame(self.tk, text="历史查询")

        results = RegistrationtDAO.listByDoctor(self.doc.uid, True)
        results.sort(key=Registration.getRTime)

        rows = []
        rows.append("编号         | 时间                        | 类型 | 患者姓名")
        for result in results:
            if result == None:
                continue
            rows.append(doctorResultToString(result))
        
        self.pendingFrameLabels = []
        for i in range(len(rows)):
            label = Label(self.pendingFrame, text=rows[i], anchor="w", width=50)
            label.grid()
        
        self.pendingFrame.grid(row=0, column=0)


if __name__ == "__main__":
    ui_doctor("590090")