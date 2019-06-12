import random
from faker import Faker
from doctor import Doctor, DoctorDAO
from user import User, UserDAO
from department import Department, DepartmentDAO

fake = Faker("zh_CN")
departments = DepartmentDAO.listAll()
dusers = UserDAO.listDoctors()
for user in dusers:
    print(user)
    uid = user.uid
    name = fake.name()
    deptID = random.choice(departments).deptID
    doc = Doctor(uid, name, deptID)
    print(doc)
    DoctorDAO.add(doc)

print("------")

docs = DoctorDAO.listAll()
for doc in docs:
    print(doc)