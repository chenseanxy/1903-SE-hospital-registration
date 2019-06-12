from mysql_db import DBConnect

class Department(object):
    def __init__(self, deptID, deptName, location, phone):
        self.deptID = deptID
        self.deptName = deptName
        self.location = location
        self.phone = phone

    def toTuple(self):
        return (self.deptID,
                self.deptName,
                self.location,
                self.phone)

    def getPrimaryKey(self):
        return self.deptID
    
    def getIdAsInt(self):
        return int(self.deptID)

    def __str__(self):
        return f"[Department] {self.toTuple()}"
    
    def getDAO(self):
        return DepartmentDAO
    
class DepartmentDAO(object):
    tableName = "departments"
    keyName = "deptID"
    
    @classmethod
    def _rowToObj(cls, tup):
        try:
            return Department(*tup)
        except:
            return None

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
        return cls._rowToObj(DBConnect.getone(query, (deptID,)))
    
    @classmethod
    def listAll(cls):
        query = (f"SELECT * FROM {cls.tableName}")
        results = DBConnect.getall(query,())
        objs = []
        for result in results:
            objs.append(cls._rowToObj((result)))
        return objs