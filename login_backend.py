from entities import User, getSHA256
from mysql_db import *
from backend import *


def userLogin(username, password):
    query = f"SELECT * FROM users WHERE username=%s"
    
    DBConnect.cursor.execute(query, (username,))
    result = DBConnect.cursor.fetchone()

    print(result)

    if result == None:
        print("[userLogin] Username not found", username)
        return None

    user = User(result)

    print("[userLogin] User:", user)
    
    if getSHA256(password) == user.hashPassword:
        return user

    return None