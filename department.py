from mysql_db import DBConnect

class Department(object):
    def __init__(self, tup):
        if(type(tup) == tuple):
            self.deptID = tup[0]
            self.deptName = tup[1]
            self.location = tup[2]
            self.phone = tup[3]

    def toTuple(self):
        return (self.deptID,
                self.deptName,
                self.location,
                self.phone)

    def getPrimaryKey(self):
        return self.deptID

    def __str__(self):
        return f"[Department] {self.toTuple()}"
    
    def getDAO(self):
        return DepartmentDAO
    
class DepartmentDAO(object):
    tableName = "departments"
    keyName = "deptID"
    
    @classmethod
    def add(cls, obj):
        query = f"INSERT INTO {cls.tableName} VALUES (%s, %s, %s, %s)"
        DBConnect.sets(query, obj.toTuple())
    
    @classmethod
    def update(cls, obj):
        print("ERR: [Department] is not updatable")

    @classmethod
    def get(cls, deptID):
        query = f"SELECT * FROM {cls.tableName} WHERE {cls.keyName}=%s"
        return DBConnect.getone(query, (deptID,))
    
    @classmethod
    def listAll(cls):
        query = (f"SELECT * FROM {cls.tableName}")
        results = DBConnect.getall(query,())
        objs = []
        for result in results:
            objs.append(Department(result))
        return objs