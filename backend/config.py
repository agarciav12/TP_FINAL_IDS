"""
Configuración de la aplicación backend
"""
import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Configuración base de la aplicación"""

    # Configuración de Flask
    DEBUG = os.getenv("FLASK_DEBUG", "True") == "True"
    HOST = os.getenv("FLASK_HOST", "127.0.0.1")
    PORT = int(os.getenv("FLASK_PORT", "5000"))

    # Configuración de CORS
    CORS_ORIGINS = os.getenv("CORS_ORIGINS", "*")
<<<<<<< HEAD
=======
    MAIL_SERVER = "smtp.gmail.com"
    
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = "TU_EMAIL@gmail.com"
    MAIL_PASSWORD = "CONTRASEÑA_DE_APP"
    MAIL_DEFAULT_SENDER = "TU_EMAIL@gmail.com"
>>>>>>> ff66d95 (Actualizar proyecto final: Terminado carrito y correcciones de archivos .html)


def get_config():
    """
    Retorna la configuración de la aplicación.
    Esta función evita usar variables globales directamente.

    Returns:
        Config: Objeto de configuración
    """
    return Config()
