from fastapi import Depends
import mysql.connector


def get_db_connection():
    connection = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        user="root",
        password="123456",
        database="alcohol",
        autocommit=True
    )
    return connection

# def get_db():
#     connection = get_db_connection()
#     db = connection.cursor()

#     try:
#         yield db
#     finally:
#         db.close()
#         connection.close()

def get_db():
    connection = get_db_connection()

    try:
        yield connection
    finally:
        connection.close()