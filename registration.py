from mysql_db import DBConnect
from doctor import Doctor, DoctorDAO
from patient import Patient, PatientDAO
from random import randint
from datetime import datetime

class Registration(object):
    def __init__(self, rid, did, pid, rtype, rtime, done):
        self.rid = rid
        self.did = did
        self.pid = pid
        self.rtype = rtype
        self.rtime = rtime
        self.done = done

    def toTuple(self):
        return (self.rid,
                self.did,
                self.pid,
                self.rtype,
                self.rtime.strftime("%m/%d/%Y %H:%M:%S"),
                self.done)

    def getPrimaryKey(self):
        return self.rid

    def getRTime(self):
        return self.rtime

    def __str__(self):
        return f"[Registration] {self.toTuple()}"
    
    def getDAO(self):
        return RegistrationtDAO
    
    def getPatient(self):
        return PatientDAO.get(self.pid)
    
    def getDoctor(self):
        return DoctorDAO.get(self.did)

class RegistrationtDAO(object):
    tableName = "registrations"
    keyName = "rid"
    
    @classmethod
    def _rowToObj(cls, tup):
        try:
            return Registration(
                tup[0],
                tup[1],
                tup[2],
                tup[3],
                datetime.strptime(tup[4], "%m/%d/%Y %H:%M:%S"),
                tup[5]
            )
        except:
            return None
        
    @classmethod
    def add(cls, obj):
        query = f"INSERT INTO {cls.tableName} VALUES (%s, %s, %s, %s, %s, %s)"
        DBConnect.sets(query, obj.toTuple())
    
    @classmethod
    def update(cls, obj):
        query = (f"UPDATE {cls.tableName} "
                "SET did=%s, pid=%s, rtype=%s, rtime=%s, done=%s "
                f"WHERE {cls.keyName}=%s")
        params = (obj.did, obj.pid, obj.rtype, obj.rtime.strftime("%m/%d/%Y %H:%M:%S"), obj.done, obj.rid)
        DBConnect.sets(query, params)

    @classmethod
    def get(cls, rid):
        query = f"SELECT * FROM {cls.tableName} WHERE {cls.keyName}=%s"
        return cls._rowToObj(DBConnect.getone(query, (rid,)))
    
    @classmethod
    def listAll(cls, done):
        query = (f"SELECT * FROM {cls.tableName} WHERE done=%s")
        results = DBConnect.getall(query,(done,))
        objs = []
        for result in results:
            objs.append(cls._rowToObj(result))
        return objs
    
    @classmethod
    def listByPatient(cls, pid, done):
        query = (f"SELECT * FROM {cls.tableName} WHERE pid=%s AND done=%s")
        results = DBConnect.getall(query,(pid, done))
        objs = []
        for result in results:
            objs.append(cls._rowToObj(result))
        return objs
    
    @classmethod
    def listByDoctor(cls, did, done):
        query = (f"SELECT * FROM {cls.tableName} WHERE did=%s AND done=%s")
        results = DBConnect.getall(query,(did, done))
        objs = []
        for result in results:
            objs.append(cls._rowToObj(result))
        return objs
    
    @classmethod
    def newID(cls):
        newid = randint(10000000, 99999999)
        while cls.get(newid) != None:
            newid = randint(10000000, 99999999)
        return newid
