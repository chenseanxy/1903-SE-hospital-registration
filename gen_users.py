import random
from faker import Faker
from user import User, UserDAO, getSHA256

fake = Faker("zh_CN")

for i in range(500):
    uid = UserDAO.newID()
    username = fake.user_name()
    utype = random.choice(["patient"]*9 + ["doctor"])
    if(utype == "doctor"):
        password = "doctor"
    else:
        password = fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)
    hashPassword = getSHA256(password)

    user = User(uid, username, hashPassword, utype)
    print(user)
    UserDAO.add(user)

uid = str(random.randint(100000, 999999))
username = "doctor"
password = "doctor"
hashPassword = getSHA256(password)
utype = "doctor"
user = User(uid, username, hashPassword, utype)
UserDAO.add(user)

uid = str(random.randint(100000, 999999))
username = "patient"
password = "patient"
hashPassword = getSHA256(password)
utype = "patient"
user = User(uid, username, hashPassword, utype)
UserDAO.add(user)

print("--------")

for user in UserDAO.listAll():
    print(user)