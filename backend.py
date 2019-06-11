from mysql_db import *
from entities import *

def getTable(obj):
    pass
    '''
    if(type(obj) == Flight):
        return "flights"
    if(type(obj) == Hotel):
        return "hotels"
    if(type(obj) == Bus):
        return "bus"
    '''

def getKeyName(table):
    pass
    '''
    if(table == "flights"):
        keyName = "flightNum"
    if(table == "hotels"):
        keyName = "hotelNum"
    if(table == "bus"):
        keyName = "busNum"
    if(table == "reservations"):
        keyName = "resvNum"
    if(table == "customers"):
        keyName = "custID"
    return keyName
    '''

def add(obj):
    print(f"[BACKEND] Adding {obj}") 
    pass
    '''
    if(type(obj) == Flight):
        query = "INSERT INTO flights VALUES (%s,%s,%s,%s,%s,%s,%s)"
        params = obj.toTuple()
    elif(type(obj) == Hotel):
        query = "INSERT INTO hotels VALUES (%s,%s,%s,%s,%s,%s)"
        params = obj.toTuple()
    elif(type(obj) == Bus):
        query = "INSERT INTO bus VALUES (%s,%s,%s,%s,%s,%s)"
        params = obj.toTuple()
    elif(type(obj) == Customer):
        query = "INSERT INTO customers VALUES (%s,%s)"
        params = obj.toTuple()
    elif(type(obj) == Reservation):
        query = "INSERT INTO reservations VALUES (%s,%s,%s,%s)"
        params = obj.toTuple()
    else:
        print(f"[BACKEND] {obj} is not of valid type!")

    DBConnect.cursor.execute(query, params)
    DBConnect.cnx.commit()
    '''

def remove(primaryKey, table):
    '''
    item = getValue(primaryKey, table)
    if(item == None):
        print(f"[BACKEND] Object {primaryKey} from {table} does not exist")
        return
    if(not item.isEmpty()):
        print(f"[BACKEND] {item} is booked, please sort out the reservations first")
        return
    
    query = "DELETE FROM {} WHERE {}=%s".format(table, getKeyName(table))

    DBConnect.cursor.execute(query, (primaryKey,))
    DBConnect.cnx.commit()
    '''

def update(obj):
    '''
    print(f"[BACKEND] Updating {obj}") 
    if(type(obj) == Flight):
        query = (f"UPDATE {getTable(obj)} "
                  "SET price=%s, numSeats=%s, numAvail=%s, fromCity=%s, arivCity=%s, param=%s "
                  "WHERE flightNum=%s")
        params = obj.toUpdateTuple()

    elif(type(obj) == Hotel):
        query = (f"UPDATE {getTable(obj)} "
                  "SET location=%s, price=%s, numRooms=%s, numAvail=%s, param=%s "
                  "WHERE hotelNum=%s")
        params = obj.toUpdateTuple()
        
    elif(type(obj) == Bus):
        query = (f"UPDATE {getTable(obj)} "
                  "SET location=%s, price=%s, numSeats=%s, numAvail=%s, param=%s "
                  "WHERE busNum=%s")
        params = obj.toUpdateTuple()
    
    else:
        print(f"[BACKEND] {obj} cannot be updated!")
    
    DBConnect.cursor.execute(query, params)
    DBConnect.cnx.commit()
    '''

def getValue(primaryKey, cls):
    query = f"SELECT * FROM {cls.tableName()} WHERE {cls.keyName()}=%s"
    
    DBConnect.cursor.execute(query, (primaryKey,))
    result = DBConnect.cursor.fetchone()

    return cls(result)

def createObj(queryResult, table):
    '''
    if(table == "flights"):
        return Flight(queryResult)
    if(table == "hotels"):
        return Hotel(queryResult)
    if(table == "bus"):
        return Bus(queryResult)
    if(table == "reservations"):
        return Reservation(queryResult)
    if(table == "customers"):
        return Customer(queryResult)
    return None
    '''

def queryTable(table):
    '''
    query = f"SELECT * FROM {table}"
    DBConnect.cursor.execute(query)
    results = DBConnect.cursor.fetchall()
    print(results)

    objects = []

    if(table == "users"):
        for line in results:
            objects.append(User(line))

    
    return objects
    '''

