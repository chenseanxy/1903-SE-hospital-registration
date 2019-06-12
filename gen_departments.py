# -*- coding: UTF-8 -*-
import random
from faker import Faker
from department import Department, DepartmentDAO

def getLocation():
    levels = [1,2,3,4,5]
    areas = ["A", "B", "C", "D", "E"]
    return f"{random.choice(levels)}楼{random.choice(areas)}区"

fake = Faker("zh_CN")
names = ("骨科门诊", "内科门诊", "妇科门诊", "针灸推拿科", "后滘门诊部", "急诊科", "骨伤一科(关节骨科)", "骨伤二科(创伤骨科)", "骨伤三科(脊柱骨科)", "骨伤四科(老年骨科)", "运动医学-关节镜科", " 妇二科(不孕不育科)", "重症医学科", "麻醉科", "医务科", "护理部", "药剂科", "医技功能室", "检验科", "放射科", "儿科门诊", "肛肠科门诊", "皮肤科门诊", "口腔科", "内科门诊", "内科住院部", "骨科门诊", "外科门诊", "眼耳鼻咽喉科", "妇科门诊", "急诊科", "妇科住院部", "针灸推拿科", "骨外科住院部", "山村门诊部", "脑病科", "康复科", "医教科", "护理部", "卫防科", "药剂科", "医技功能室", "检验科", "放射科")
for i in range(len(names)):
    deptName = names[i]
    deptID = i+1
    location = getLocation()
    phone = fake.phone_number()
    dept = Department(deptID, deptName, location, phone)
    print(dept)

    DepartmentDAO.add(dept)

