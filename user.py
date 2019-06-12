import json
from hashlib import sha256
from mysql_db import DBConnect
from random import randint

def getSHA256(password):
    return sha256(password.encode("utf8")).hexdigest()

class User(object):
    def __init__(self, uid, username, hashPassword, utype):
        self.uid = uid
        self.username = username
        self.hashPassword = hashPassword
        self.utype = utype

    def toTuple(self):
        return (self.uid,
                self.username,
                self.hashPassword,
                self.utype)

    def getPrimaryKey(self):
        return self.uid

    def __str__(self):
        return f"[USER] {self.toTuple()}"
    
    def getDAO(self):
        return UserDAO

class UserDAO(object):
    tableName = "users"
    keyName = "uid"
    
    @classmethod
    def _rowToObj(cls, tup):
        try:
            return User(*tup)
        except:
            return None

    @classmethod
    def add(cls, user):
        query = f"INSERT INTO {cls.tableName} VALUES (%s, %s, %s, %s)"
        DBConnect.sets(query, user.toTuple())
    
    @classmethod
    def update(cls, user):
        query = (f"UPDATE {cls.tableName} "
                "SET username=%s, hashPassword=%s, utype=%s "
                f"WHERE {cls.keyName}=%s")
        params = ()
        DBConnect.sets(query, params)

    @classmethod
    def get(cls, uid):
        query = f"SELECT * FROM {cls.tableName} WHERE {cls.keyName}=%s"
        return cls._rowToObj(DBConnect.getone(query, (uid,)))
    
    @classmethod
    def getByUsername(cls, username):
        query = f"SELECT * FROM {cls.tableName} WHERE username=%s"
        return cls._rowToObj(DBConnect.getone(query, (username,)))
    
    @classmethod
    def listAll(cls):
        query = (f"SELECT * FROM {cls.tableName}")
        results = DBConnect.getall(query,())
        users = []
        for result in results:
            users.append(cls._rowToObj(result))
        return users

    @classmethod
    def listDoctors(cls):
        query = (f"SELECT * FROM {cls.tableName} WHERE utype=%s")
        results = DBConnect.getall(query,("doctor",))
        users = []
        for result in results:
            users.append(cls._rowToObj(result))
        return users
    
    @classmethod
    def listPatients(cls):
        query = (f"SELECT * FROM {cls.tableName} WHERE utype=%s")
        results = DBConnect.getall(query,("patient",))
        users = []
        for result in results:
            users.append(cls._rowToObj(result))
        return users
    
    @classmethod
    def newID(cls):
        newid = randint(100000, 999999)
        while cls.get(newid) != None:
            newid = randint(100000, 999999)
        return newid
