import mysql.connector
from mysql.connector import errorcode
import json


with open("resources//mysql_config.json", "r") as f:
    mysql_config = json.load(f)


class DBConnect(object):
    cnx = mysql.connector.connect(**mysql_config)
    cursor = cnx.cursor()

    @classmethod
    def sets(cls, query, params):
        cls.cursor.execute(query, params)
        cls.cnx.commit()
    
    @classmethod
    def getone(cls, query, params):
        cls.cursor.execute(query, params)
        return cls.cursor.fetchone()
    
    @classmethod
    def getall(cls, query, params):
        cls.cursor.execute(query, params)
        return cls.cursor.fetchall()
