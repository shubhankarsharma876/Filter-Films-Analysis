import sqlite3
from sqlite3 import Error

def create_connection(path):
    connection= None
    try:
        connection = sqlite3.connect(path,timeout=20)
        print("Connection Establish")
    except Error as e:
        print(f"Connection Failed '{e}'")
    return connection