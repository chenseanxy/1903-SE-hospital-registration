from mysql_db import DBConnect
from user import UserDAO

class Doctor(object):
    def __init__(self, uid, name, deptID):
        self.uid = uid
        self.name = name
        self.deptID = deptID

    def toTuple(self):
        return (self.uid,
                self.name,
                self.deptID)

    def getPrimaryKey(self):
        return self.uid

    def __str__(self):
        return f"[DOCTOR] {self.toTuple()}"
    
    def getDAO(self):
        return DoctorDAO

    def getUser(self):
        return UserDAO.get(self.uid)

class DoctorDAO(object):
    tableName = "doctors"
    keyName = "uid"

    @classmethod
    def _rowToObj(cls, tup):
        try:
            return Doctor(*tup)
        except:
            return None

    @classmethod
    def add(cls, obj):
        query = f"INSERT INTO {cls.tableName} VALUES (%s, %s, %s)"
        DBConnect.sets(query, obj.toTuple())
    
    @classmethod
    def update(cls, obj):
        query = (f"UPDATE {cls.tableName} "
                "SET name=%s, deptID=%s "
                f"WHERE {cls.keyName}=%s")
        params = (obj.name, obj.deptID, obj.uid)
        DBConnect.sets(query, params)

    @classmethod
    def get(cls, uid):
        query = f"SELECT * FROM {cls.tableName} WHERE {cls.keyName}=%s"
        row = DBConnect.getone(query, (uid,))
        return cls._rowToObj(row)
        
    @classmethod
    def listAll(cls):
        query = (f"SELECT * FROM {cls.tableName}")
        results = DBConnect.getall(query,())
        objs = []
        for result in results:
            objs.append(cls._rowToObj(result))
        return objs
    
    @classmethod
    def listByDepartment(cls, deptID):
        query = (f"SELECT * FROM {cls.tableName} WHERE deptID=%s")
        results = DBConnect.getall(query,(deptID,))
        objs = []
        for result in results:
            objs.append(cls._rowToObj(result))
        return objs