"""
Utilidades para el frontend
Contiene funciones auxiliares para comunicación con el backend
"""
import requests
from flask import render_template


def safe_api_request(url, method='GET', json_data=None, timeout=5):
    """
    Realiza una petición al backend API con manejo de errores.

    Args:
        url (str): URL del endpoint
        method (str): Método HTTP (GET, POST, etc.)
        json_data (dict): Datos JSON para enviar (opcional)
        timeout (int): Timeout en segundos

    Returns:
        tuple: (data, error_message)
            - data: Datos de la respuesta si fue exitosa, None si falló
            - error_message: Mensaje de error si falló, None si fue exitosa
    """
    try:
        if method.upper() == 'GET':
            response = requests.get(url, timeout=timeout)
        elif method.upper() == 'POST':
            response = requests.post(url, json=json_data, timeout=timeout)
        elif method.upper() == 'PUT':
            response = requests.put(url, json=json_data, timeout=timeout)
        elif method.upper() == 'DELETE':
            response = requests.delete(url, timeout=timeout)
        else:
            return None, f"Método HTTP no soportado: {method}"

        # Verificar el código de estado
        if response.status_code >= 200 and response.status_code < 300:
            try:
                return response.json(), None
            except ValueError:
                return None, "La respuesta del servidor no es un JSON válido"
        else:
            # Intenta extraer el mensaje de error del backend
            try:
                error_data = response.json()
                error_msg = error_data.get('error', f'Error {response.status_code}')
            except ValueError:
                error_msg = f'Error {response.status_code}: {response.text}'

            return None, error_msg

    except requests.exceptions.Timeout:
        return None, "El servidor no respondió a tiempo. Intenta nuevamente."

    except requests.exceptions.ConnectionError:
        return None, "No se pudo conectar con el servidor. Verifica que el backend esté ejecutándose."

    except requests.exceptions.RequestException as e:
        return None, f"Error al comunicarse con el servidor: {str(e)}"

    except Exception as e:
        return None, f"Error inesperado: {str(e)}"


def render_error_page(error_message, status_code=500):
    """
    Renderiza una página de error genérica.

    Args:
        error_message (str): Mensaje de error a mostrar
        status_code (int): Código de estado HTTP

    Returns:
        tuple: (rendered_template, status_code)
    """
    return render_template(
        'error.html',
        error_message=error_message,
        status_code=status_code
    ), status_code
