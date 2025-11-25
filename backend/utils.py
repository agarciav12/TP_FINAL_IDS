"""
Utilidades para el backend
Contiene decoradores y funciones auxiliares
"""
from functools import wraps
from flask import jsonify
from db import get_connection
import mysql.connector


def with_database_connection(dictionary=True):
    """
    Decorador para manejar automáticamente las conexiones a la base de datos.
    Elimina código repetido y asegura que las conexiones se cierren siempre.

    Args:
        dictionary (bool): Si el cursor debe retornar diccionarios (default: True)
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            conn = None
            cur = None
            try:
                conn = get_connection()
                cur = conn.cursor(dictionary=dictionary)
                result = func(cur, conn, *args, **kwargs)
                return result
            except mysql.connector.Error as db_err:
                if conn:
                    conn.rollback()
                return jsonify({"error": f"Error de base de datos: {str(db_err)}"}), 500
            except Exception as e:
                if conn:
                    conn.rollback()
                return jsonify({"error": f"Error interno del servidor: {str(e)}"}), 500
            finally:
                if cur:
                    cur.close()
                if conn:
                    conn.close()
        return wrapper
    return decorator


def validate_required_fields(data, required_fields):
    """
    Valida que todos los campos requeridos estén presentes en los datos.

    Args:
        data (dict): Datos a validar
        required_fields (list): Lista de campos requeridos

    Returns:
        tuple: (es_válido, mensaje_error)
    """
    if not data:
        return False, "No se recibieron datos"

    missing_fields = [field for field in required_fields if field not in data]

    if missing_fields:
        return False, f"Faltan campos requeridos: {', '.join(missing_fields)}"

    return True, None


def validate_positive_integer(value, field_name):
    """
    Valida que un valor sea un entero positivo.

    Args:
        value: Valor a validar
        field_name (str): Nombre del campo para el mensaje de error

    Returns:
        tuple: (es_válido, mensaje_error)
    """
    try:
        int_value = int(value)
        if int_value <= 0:
            return False, f"{field_name} debe ser un número positivo"
        return True, None
    except (ValueError, TypeError):
        return False, f"{field_name} debe ser un número entero válido"
