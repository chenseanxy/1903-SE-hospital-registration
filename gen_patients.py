import random
from faker import Faker
from user import User, UserDAO
from patient import Patient, PatientDAO

fake = Faker("zh_CN")

users = UserDAO.listPatients()
for user in users:
    uid = user.uid
    name = fake.name()
    balance = random.randint(0, 1000000)/100
    email = fake.email()
    phone = fake.phone_number()
    pat = Patient(uid, name, balance, email, phone)
    PatientDAO.add(pat)

for patient in PatientDAO.listAll():
    print(patient)