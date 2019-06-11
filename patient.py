from mysql_db import DBConnect
from user import UserDAO

class Patient(object):
    def __init__(self, uid, name, balance, email, phone):
        self.uid = uid
        self.name = name
        self.balance = balance
        self.email = email
        self.phone = phone

    def toTuple(self):
        return (self.uid,
                self.name,
                self.balance,
                self.email,
                self.phone)

    def getPrimaryKey(self):
        return self.uid

    def __str__(self):
        return f"[Patient] {self.toTuple()}"
    
    def getDAO(self):
        return PatientDAO
    
    def getUser(self):
        return UserDAO.get(self.uid)

class PatientDAO(object):
    tableName = "patients"
    keyName = "uid"
    
    @classmethod
    def _rowToObj(cls, tup):
        try:
            return Patient(*tup)
        except:
            return None
    
    @classmethod
    def add(cls, obj):
        query = f"INSERT INTO {cls.tableName} VALUES (%s, %s, %s, %s, %s)"
        DBConnect.sets(query, obj.toTuple())
    
    @classmethod
    def update(cls, obj):
        query = (f"UPDATE {cls.tableName} "
                "SET name=%s, balance=%s, email=%s, phone=%s "
                f"WHERE {cls.keyName}=%s")
        params = (obj.name, obj.balance, obj.email, obj.phone, obj.uid)
        DBConnect.sets(query, params)

    @classmethod
    def get(cls, uid):
        query = f"SELECT * FROM {cls.tableName} WHERE {cls.keyName}=%s"
        return cls._rowToObj(DBConnect.getone(query, (uid,)))
    
    @classmethod
    def listAll(cls):
        query = (f"SELECT * FROM {cls.tableName}")
        results = DBConnect.getall(query,())
        objs = []
        for result in results:
            objs.append(cls._rowToObj(result))
        return objs