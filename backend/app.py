"""
Backend API - E-commerce
Aplicación Flask que proporciona endpoints RESTful para el frontend
"""
from flask import Flask, jsonify, request
from flask_cors import CORS
from config import get_config
from utils import with_database_connection, validate_required_fields, validate_positive_integer


def create_app():
    """
    Factory pattern para crear la aplicación Flask.
    Evita el uso de variables globales.
    """
    app = Flask(__name__)
    config = get_config()

    # Configurar CORS
    CORS(app, origins=config.CORS_ORIGINS)

    # ----------------------------
    # GET /api/productos
    # ----------------------------
    @app.get("/api/productos")
    @with_database_connection(dictionary=True)
    def get_productos(cur, conn):
        """
        Obtiene todos los productos o filtra por categoría.

        Query params:
            - categoria (str, opcional): Categoría para filtrar

        Returns:
            JSON: Lista de productos
        """
        categoria = request.args.get("categoria")

        if categoria:
            cur.execute("SELECT * FROM productos WHERE categoria = %s", (categoria,))
        else:
            cur.execute("SELECT * FROM productos")

        data = cur.fetchall()
        return jsonify(data), 200

    # ----------------------------
    # GET /api/productos/<id>
    # ----------------------------
    @app.get("/api/productos/<int:id>")
    @with_database_connection(dictionary=True)
    def get_producto(cur, conn, id):
        """
        Obtiene un producto específico por ID.

        Args:
            pid (int): ID del producto

        Returns:
            JSON: Datos del producto o error 404
        """
        # Validar que el ID sea positivo
        is_valid, error_msg = validate_positive_integer(id, "ID del producto")
        if not is_valid:
            return jsonify({"error": error_msg}), 400

        cur.execute("SELECT * FROM productos WHERE id=%s", (id,))
        data = cur.fetchone()

        if not data:
            return jsonify({"error": "Producto no encontrado"}), 404

        return jsonify(data), 200

    # ----------------------------
    # POST /api/carrito → agregar
    # ----------------------------
    @app.post("/api/carrito")
    @with_database_connection(dictionary=False)
    def post_carrito(cur, conn):
        """
        Agrega un producto al carrito del usuario.

        Body JSON:
            - usuario_id (int): ID del usuario
            - producto_id (int): ID del producto
            - cantidad (int): Cantidad a agregar

        Returns:
            JSON: Estado de la operación
        """
        data = request.get_json()

        # Validar campos requeridos
        required_fields = ["usuario_id", "producto_id", "cantidad"]
        is_valid, error_msg = validate_required_fields(data, required_fields)
        if not is_valid:
            return jsonify({"error": error_msg}), 400

        # Validar que sean números positivos
        for field in required_fields:
            is_valid, error_msg = validate_positive_integer(data[field], field)
            if not is_valid:
                return jsonify({"error": error_msg}), 400

        # Verificar que el producto exista
        cur.execute("SELECT id FROM productos WHERE id = %s", (data["producto_id"],))
        if not cur.fetchone():
            return jsonify({"error": "El producto no existe"}), 404

        # Insertar o actualizar en el carrito
        query = """
            INSERT INTO carrito (usuario_id, producto_id, cantidad)
            VALUES (%s, %s, %s)
            ON DUPLICATE KEY UPDATE cantidad = cantidad + VALUES(cantidad)
        """
        cur.execute(query, (data["usuario_id"], data["producto_id"], data["cantidad"]))
        conn.commit()

        return jsonify({"status": "ok", "message": "Producto agregado al carrito"}), 201

    # ----------------------------
    # GET /api/carrito/<usuario_id>
    # ----------------------------
    @app.get("/api/carrito/<int:uid>")
    @with_database_connection(dictionary=True)
    def get_carrito(cur, conn, uid):
        """
        Obtiene el carrito de un usuario específico.

        Args:
            uid (int): ID del usuario

        Returns:
            JSON: Lista de productos en el carrito
        """
        # Validar que el ID sea positivo
        is_valid, error_msg = validate_positive_integer(uid, "ID del usuario")
        if not is_valid:
            return jsonify({"error": error_msg}), 400

        query = """
            SELECT c.producto_id, c.cantidad, p.nombre, p.precio
            FROM carrito c
            JOIN productos p ON p.id = c.producto_id
            WHERE c.usuario_id = %s
        """
        cur.execute(query, (uid,))
        data = cur.fetchall()

        return jsonify(data), 200

    # ----------------------------
    # POST /api/compras → finalizar compra
    # ----------------------------
    @app.post("/api/compras")
    @with_database_connection(dictionary=False)
    def post_compra(cur, conn):
        """
        Finaliza la compra del carrito de un usuario.

        Body JSON:
            - usuario_id (int): ID del usuario

        Returns:
            JSON: Información de la compra creada
        """
        data = request.get_json()

        # Validar campos requeridos
        required_fields = ["usuario_id"]
        is_valid, error_msg = validate_required_fields(data, required_fields)
        if not is_valid:
            return jsonify({"error": error_msg}), 400

        usuario_id = data["usuario_id"]

        # Validar que sea un número positivo
        is_valid, error_msg = validate_positive_integer(usuario_id, "ID del usuario")
        if not is_valid:
            return jsonify({"error": error_msg}), 400

        # Obtener el carrito
        cur.execute("""
            SELECT producto_id, cantidad
            FROM carrito
            WHERE usuario_id = %s
        """, (usuario_id,))
        carrito = cur.fetchall()

        if not carrito:
            return jsonify({"error": "Carrito vacío"}), 400

        # Crear la compra
        cur.execute("INSERT INTO compras (usuario_id, total) VALUES (%s, 0)", (usuario_id,))
        compra_id = cur.lastrowid

        total = 0

        # Agregar los items
        for (producto_id, cantidad) in carrito:
            cur.execute("SELECT precio FROM productos WHERE id=%s", (producto_id,))
            result = cur.fetchone()

            if not result:
                # Rollback si un producto no existe
                conn.rollback()
                return jsonify({"error": f"Producto con ID {producto_id} no encontrado"}), 404

            precio = result[0]
            subtotal = precio * cantidad
            total += subtotal

            cur.execute("""
                INSERT INTO items_compra (compra_id, producto_id, precio_unitario, cantidad, subtotal)
                VALUES (%s, %s, %s, %s, %s)
            """, (compra_id, producto_id, precio, cantidad, subtotal))

        # Actualizar el total
        cur.execute("UPDATE compras SET total=%s WHERE id=%s", (total, compra_id))

        # Vaciar el carrito
        cur.execute("DELETE FROM carrito WHERE usuario_id=%s", (usuario_id,))

        conn.commit()

        return jsonify({
            "status": "ok",
            "compra_id": compra_id,
            "total": float(total),
            "message": "Compra realizada exitosamente"
        }), 201

    # ----------------------------
    # Manejo de errores 404
    # ----------------------------
    @app.errorhandler(404)
    def not_found(error):
        """Maneja rutas no encontradas"""
        return jsonify({"error": "Endpoint no encontrado"}), 404

    # ----------------------------
    # Manejo de errores 500
    # ----------------------------
    @app.errorhandler(500)
    def internal_error(error):
        """Maneja errores internos del servidor"""
        return jsonify({"error": "Error interno del servidor"}), 500

    return app


if __name__ == "__main__":
    application = create_app()
    config = get_config()
    application.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)
