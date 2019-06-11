from backend import *

def newReservation(reservation):
    if(reservation.resvType == 1):  #Flight
        obj = getValue(reservation.resvKey, "flights")
    elif(reservation.resvType == 2):  #Hotel
        obj = getValue(reservation.resvKey, "hotels")
    elif(reservation.resvType == 3):  #Bus
        obj = getValue(reservation.resvKey, "bus")
    else:
        print(f"[BACKEND] Reservation mode {reservation.resvType} not available")
        return
    
    if(obj == None):
        print(f"[BACKEND] {reservation.resvKey} is not available")
        return

    if(getValue(reservation.resvNum, "reservations") != None):
        print(f"[BACKEND] RESV:{reservation.resvNum} is already taken")
        print(getValue(reservation.resvNum, "reservations"))
        return
    if(getValue(reservation.custID, "customers") == None):
        print(f"[BACKEND] CustID: {reservation.custID} does not exist")
        return
    if(obj.isFull() == True):
        print(f"[BACKEND] {obj} is not available")
        return

    obj.numAvail -= 1
    update(obj)
    add(reservation)
    
def cancelReservation(resvNum):
    reservation = getValue(resvNum, "reservations")
    if(reservation == None):
        print(f"[BACKEND] Reservation {resvNum} is not available")
        return

    if(reservation.resvType == 1):  #Flight
        obj = getValue(reservation.resvKey, "flights")
    elif(reservation.resvType == 2):  #Hotel
        obj = getValue(reservation.resvKey, "hotels")
    elif(reservation.resvType == 3):  #Bus
        obj = getValue(reservation.resvKey, "bus")
    else:
        print(f"[BACKEND] Reservation mode {reservation.resvType} not available")
        return

    if(obj == None):
        print(f"[BACKEND] Reserved item {reservation.resvKey} is not available")
        print("[BACKEND] Auto-cancelling reservation")
        remove(resvNum, "reservations")
        return
    
    obj.numAvail += 1
    update(obj)
    remove(resvNum, "reservations")

def queryReservation(custID):
    query = "SELECT * FROM reservations WHERE custID=%s"
    DBConnect.cursor.execute(query, (custID,))
    results = DBConnect.cursor.fetchall()

    if(results == None):
        print("Reservations does not exist")
        return None

    objects = []
    for result in results:
        objects.append(Reservation(result))
    return objects