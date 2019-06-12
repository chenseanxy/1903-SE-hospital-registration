import random
from faker import Faker
from patient import Patient, PatientDAO
from doctor import Doctor, DoctorDAO
from registration import Registration, RegistrationtDAO

fake = Faker("zh_CN")
patients = PatientDAO.listAll()
doctors = DoctorDAO.listAll()
for i in range(5000):
    rtypes = ["normal", "pro"]
    done = random.choice([True]*9 +[False]*1)
    rid = RegistrationtDAO.newID()
    did = random.choice(doctors).uid
    pid = random.choice(patients).uid
    rtime = fake.date_time_this_month(before_now=True, after_now=False, tzinfo=None)
    rtype = random.choice(rtypes)
    reg = Registration(rid, did, pid, rtype, rtime, done)
    print(reg)
    RegistrationtDAO.add(reg)

for doc in doctors:
    print(f"-----------Doctor {doc.name} --------------")
    for reg in RegistrationtDAO.listByDoctor(doc.uid, True):
        print(reg)
    for reg in RegistrationtDAO.listByDoctor(doc.uid, False):
        print(reg)