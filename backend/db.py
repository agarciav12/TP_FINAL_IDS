import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="agus",
        password="Agus_DB_1206",
        database="base_tp"
        port=3306
    )