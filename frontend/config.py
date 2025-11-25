"""
Configuración de la aplicación frontend
"""
import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Configuración base de la aplicación"""

    # Configuración de Flask
    DEBUG = os.getenv("FLASK_DEBUG", "True") == "True"
    HOST = os.getenv("FLASK_HOST", "127.0.0.1")
    PORT = int(os.getenv("FLASK_PORT", "5001"))

    # Configuración del Backend API
    BACKEND_URL = os.getenv("BACKEND_URL", "http://127.0.0.1:5000/api")


def get_config():
    """
    Retorna la configuración de la aplicación.
    Esta función evita usar variables globales directamente.

    Returns:
        Config: Objeto de configuración
    """
    return Config()
