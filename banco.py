import os
import sqlite3
from sqlite3 import Error

def create_connection():
    connection = None
    try:
        connection = sqlite3.connect("database.db")
    except Error as error:
        print(error)
    return connection

def select(query):
    with create_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()

def execute(query):
    with create_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()