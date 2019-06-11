import json
from hashlib import sha256
from mysql_db import DBConnect

def getSHA256(password):
    return sha256(password.encode("utf8")).hexdigest()

class User(object):
    def __init__(self, tup):
        if(type(tup) == tuple):
            self.uid = tup[0]
            self.username = tup[1]
            self.hashPassword = tup[2]
            self.utype = tup[3]

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
        return DBConnect.getone(query, (uid,))
    
    @classmethod
    def getByUsername(cls, username):
        query = f"SELECT * FROM {cls.tableName} WHERE username=%s"
        return DBConnect.getone(query, (username,))
    
    @classmethod
    def list(cls):
        query = (f"SELECT * FROM {cls.tableName}")
        results = DBConnect.getall(query,())
        users = []
        for result in results:
            users.append(User(result))
        return users