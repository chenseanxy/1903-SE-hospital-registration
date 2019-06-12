from tkinter import *
from registration import RegistrationtDAO, Registration
from patient import PatientDAO
from doctor import DoctorDAO, Doctor
from department import DepartmentDAO, Department
from out import out
from datetime import datetime

class ui_newReg(object):
    def __init__(self, uid):
        self.patient = PatientDAO.get(uid)

        self.tk = Tk()
        self.tk.title("医院挂号就诊系统-新建挂号")

        self.departments = DepartmentDAO.listAll()
        self.departments.sort(key=Department.getIdAsInt)
        self.departmentList=[]
        for department in self.departments:
            self.departmentList.append(f"{department.deptID:>2}|{department.deptName}")
               
        self.rtypeList = ["普通", "专家"]

        self.departmentText = Label(self.tk, text="科室", anchor="e", width=10)
        self.departmentText.grid(row=0, column=0, padx=5)
        self.doctorText = Label(self.tk, text="医生", anchor="e", width=10)
        self.doctorText.grid(row=1, column=0, padx=5)
        self.rtypeText = Label(self.tk, text="挂号类型", anchor="e", width=10)
        self.rtypeText.grid(row=2, column=0, padx=5)

        self.department = StringVar(self.tk)
        self.department.set(self.departmentList[0])
        self.departmentOption = OptionMenu(self.tk, self.department, *self.departmentList, command=self.updateMenus)
        self.departmentOption.config(width=20)
        self.departmentOption.grid(row=0, column=1, padx=5)

        self.doctor = StringVar(self.tk)
        self.doctorOption = OptionMenu(self.tk, self.doctor, "null")
        self.updateMenus()

        self.rtype = StringVar(self.tk)
        self.rtype.set(self.rtypeList[0])
        self.rtypeOption = OptionMenu(self.tk, self.rtype, *self.rtypeList)
        self.rtypeOption.config(width=20)
        self.rtypeOption.grid(row=2, column=1, padx=5)

        self.submitButton = Button(self.tk, text="确认", command = self.submit, padx=20)
        self.submitButton.grid(row=3, columnspan=2, padx=5, pady=5)

        self.tk.mainloop()


    def getDepartment(self):
        return str(int(self.department.get().split("|")[0]))
    
    def getDoctor(self):
        return str(int(self.doctor.get().split("|")[0]))
    
    def getRType(self):
        if(self.rtype.get() == "普通"):
            return "normal"
        else:
            return "pro"

    def updateMenus(self, *args):
        self.doctors = DoctorDAO.listByDepartment(self.getDepartment())
        self.doctors.sort(key=Doctor.getPrimaryKey)
        self.doctorsList = []
        for doctor in self.doctors:
            self.doctorsList.append(f"{doctor.uid}|{doctor.name}")
            out(f"{doctor.uid}|{doctor.name}")
        
        self.doctorOption.destroy()
        if(len(self.doctorsList) == 0):
            self.doctorsList.append("None")
        self.doctor.set(self.doctorsList[0])
        self.doctorOption = OptionMenu(self.tk, self.doctor, *self.doctorsList)
        self.doctorOption.config(width=20)
        self.doctorOption.grid(row=1, column=1, padx=5)
    
    def submit(self):
        rid = RegistrationtDAO.newID()
        did = self.getDoctor()
        pid = self.patient.uid
        time = datetime.now()
        rtype = self.getRType()
        reg = Registration(rid, did, pid, rtype, time, False)
        RegistrationtDAO.add(reg)
        self.tk.destroy()

if __name__ == "__main__":
    ui_newReg("592536")