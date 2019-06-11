import json
from hashlib import sha256

def getSHA256(password):
    return sha256(password).hexdigest()


class User(object):
    def __init__(self, tup):
        if(type(tup) == tuple):
            self.uid = tup[0]
            self.username = tup[1]
            self.hashPassword = tup[2]
            self.utype = tup[3]

        if(type(tup) == str):
            d = json.loads(tup)
            self.uid = d["uid"]
            self.username = d["username"]
            self.hashPassword = d["hashPassword"]
            self.utype = d["utype"]

    def toTuple(self):
        return (self.uid,
                self.username,
                self.hashPassword,
                self.utype)

    def getPrimaryKey(self):
        return self.uid

    def __str__(self):
        return f"[USER] {self.toTuple()}"
    
    @staticmethod
    def tableName():
        return "users"
    
    @staticmethod
    def keyName():
        return "uid"
    

