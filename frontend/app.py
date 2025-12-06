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
<<<<<<< HEAD
        """
        Lista de productos.
        Puede filtrar por categoría mediante query param.
        """
        categoria = request.args.get("categoria")
        backend_url = config.BACKEND_URL

        # Construir URL con o sin filtro de categoría
=======
        categoria = request.args.get("categoria")
        backend_url = config.BACKEND_URL

>>>>>>> ff66d95 (Actualizar proyecto final: Terminado carrito y correcciones de archivos .html)
        if categoria:
            url = f"{backend_url}/productos?categoria={categoria}"
        else:
            url = f"{backend_url}/productos"

<<<<<<< HEAD
        # Realizar petición al backend
        data, error = safe_api_request(url, method='GET')

        if error:
=======
        data, error = safe_api_request(url, method='GET')

        if error or data is None:
>>>>>>> ff66d95 (Actualizar proyecto final: Terminado carrito y correcciones de archivos .html)
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
<<<<<<< HEAD

=======
    
    @app.get("/carrito")
    def ver_carrito():
        backend_url = config.BACKEND_URL
        usuario_id = 1

        url = f"{backend_url}/carrito/{usuario_id}"
        data, error = safe_api_request(url, method="GET")

        if error or data is None:
            return render_error_page(
                f"Error al obtener el carrito: {error}",
                status_code=500
            )

        items = data
        total = sum(float(item["precio"]) * int(item["cantidad"]) for item in items)

        return render_template("carrito.html", items=items, total=total)
    
    @app.post("/carrito")
    def carrito():
        backend_url = config.BACKEND_URL
        
        producto_id = request.form.get("producto_id")

        cantidad = request.form.get("cantidad", 1) 
        

        submit_type = request.form.get("submit_type") 

        usuario_id = 1
        
        payload = {
            "usuario_id": int(usuario_id),
            "producto_id": int(producto_id),
            "cantidad": int(cantidad)
        }

        url = f"{backend_url}/carrito"    
        data, error = safe_api_request(url, method="POST", json_data=payload)
        
        if error or data is None:
            return render_error_page(
                f"Error al obtener el carrito: {error}",
                status_code=500
            )

        if submit_type == "checkout":
            return redirect(f"/finalizar_compra?producto_id={producto_id}&cantidad={cantidad}")
        else: 
            return redirect(f"/producto/{producto_id}")
    
    @app.post("/carrito/vaciar")
    def vaciar_carrito():
        backend_url = config.BACKEND_URL
        usuario_id = 1

        url = f"{backend_url}/carrito/{usuario_id}"
        data, error = safe_api_request(url, method="DELETE")

        if error or data is None:
            return render_error_page(
                f"Error al vaciar el carrito: {error}",
                status_code=500
            )

        return redirect("/carrito")
    
    @app.route("/finalizar_compra", methods=["GET", "POST"])
    def finalizar_compra():
        backend_url = config.BACKEND_URL
        usuario_id = 1

        if request.method == "GET":
            return render_template("pago.html")

        payload = {"usuario_id": int(usuario_id)}
        url = f"{backend_url}/compras"

        data, error = safe_api_request(url, method="POST", json_data=payload)

        if error or data is None:
            return render_error_page(
                f"Error al finalizar la compra: {error}",
                status_code=400
            )
        
        return render_template("checkout.html", compra=data)
    
>>>>>>> ff66d95 (Actualizar proyecto final: Terminado carrito y correcciones de archivos .html)
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
