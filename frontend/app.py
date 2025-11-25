"""
Frontend - E-commerce
Aplicación Flask que renderiza la interfaz web y consume el backend API
"""
from flask import Flask, render_template, request, redirect
from config import get_config
from utils import safe_api_request, render_error_page


def create_app():
    """
    Factory pattern para crear la aplicación Flask.
    Evita el uso de variables globales.
    """
    app = Flask(__name__)
    config = get_config()

    @app.route("/")
    def home():
        """Página principal"""
        return redirect("/productos")

    @app.route("/productos")
    def productos():
        """
        Lista de productos.
        Puede filtrar por categoría mediante query param.
        """
        categoria = request.args.get("categoria")
        backend_url = config.BACKEND_URL

        # Construir URL con o sin filtro de categoría
        if categoria:
            url = f"{backend_url}/productos?categoria={categoria}"
        else:
            url = f"{backend_url}/productos"

        # Realizar petición al backend
        data, error = safe_api_request(url, method='GET')

        if error:
            return render_error_page(
                f"Error al obtener productos: {error}",
                status_code=500
            )

        return render_template("productos.html", productos=data)

    @app.route("/producto/<int:id>")
    def producto(id):
        """
        Detalle de un producto específico.

        Args:
            pid (int): ID del producto
        """
        backend_url = config.BACKEND_URL
        url = f"{backend_url}/productos/{id}"

        # Realizar petición al backend
        data, error = safe_api_request(url, method='GET')

        if error:
            return render_error_page(
                f"Error al obtener el producto: {error}",
                status_code=404 if "no encontrado" in error.lower() else 500
            )

        return render_template("producto.html", producto=data)

    @app.route("/about")
    def sobre_nosotros():
        """Página sobre nosotros"""
        return render_template("about.html")

    @app.route("/contacto")
    def contacto():
        """Página de contacto"""
        return render_template("contact.html")

    # ----------------------------
    # Manejo de errores 404
    # ----------------------------
    @app.errorhandler(404)
    def not_found(error):
        """Maneja páginas no encontradas"""
        return render_error_page("Página no encontrada", status_code=404)

    # ----------------------------
    # Manejo de errores 500
    # ----------------------------
    @app.errorhandler(500)
    def internal_error(error):
        """Maneja errores internos del servidor"""
        return render_error_page("Error interno del servidor", status_code=500)

    return app


if __name__ == "__main__":
    application = create_app()
    config = get_config()
    application.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)
