import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", ""),
<<<<<<< HEAD
        database=os.getenv("DB_NAME", "tp"),
=======
        database=os.getenv("DB_NAME", "base_tp"),
>>>>>>> ff66d95 (Actualizar proyecto final: Terminado carrito y correcciones de archivos .html)
        port=int(os.getenv("DB_PORT", "3306"))
    )