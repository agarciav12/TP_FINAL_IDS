"""
Backend API - E-commerce
Aplicación Flask que proporciona endpoints RESTful para el frontend
"""
<<<<<<< HEAD
from flask import Flask, jsonify, request
from flask_cors import CORS
from config import get_config
from utils import with_database_connection, validate_required_fields, validate_positive_integer


def create_app():
    """
    Factory pattern para crear la aplicación Flask.
    Evita el uso de variables globales.
    """
=======
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
from config import get_config
from utils import with_database_connection, validate_required_fields, validate_positive_integer
from flask_mail import Mail, Message


def create_app():
>>>>>>> ff66d95 (Actualizar proyecto final: Terminado carrito y correcciones de archivos .html)
    app = Flask(__name__)
    config = get_config()

    # Configurar CORS
    CORS(app, origins=config.CORS_ORIGINS)

<<<<<<< HEAD
=======
    # Configurar Mail
    app.config['MAIL_SERVER'] = config.MAIL_SERVER
    app.config['MAIL_PORT'] = config.MAIL_PORT
    app.config['MAIL_USE_TLS'] = config.MAIL_USE_TLS
    app.config['MAIL_USERNAME'] = config.MAIL_USERNAME
    app.config['MAIL_PASSWORD'] = config.MAIL_PASSWORD
    app.config['MAIL_DEFAULT_SENDER'] = config.MAIL_DEFAULT_SENDER

    mail = Mail(app)

    from flask import send_from_directory

    @app.route("/api/images/<path:nombre>")
    def imagenes(nombre):
        return send_from_directory("static/productos", nombre)

>>>>>>> ff66d95 (Actualizar proyecto final: Terminado carrito y correcciones de archivos .html)
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
<<<<<<< HEAD
=======

        backend_url = "http://127.0.0.1:5000" 

        for prod in data:
            if prod.get("imagen"):
                prod["imagen_url"] = f"{backend_url}/api/images/{prod['imagen']}"
            else:
                prod["imagen_url"] = None

>>>>>>> ff66d95 (Actualizar proyecto final: Terminado carrito y correcciones de archivos .html)
        return jsonify(data), 200

    # ----------------------------
    # GET /api/productos/<id>
    # ----------------------------
<<<<<<< HEAD
    @app.get("/api/productos/<int:id>")
    @with_database_connection(dictionary=True)
    def get_producto(cur, conn, id):
=======
    @app.get("/api/productos/<int:pid>")
    @with_database_connection(dictionary=True)
    def get_producto(cur, conn, pid):
>>>>>>> ff66d95 (Actualizar proyecto final: Terminado carrito y correcciones de archivos .html)
        """
        Obtiene un producto específico por ID.

        Args:
            pid (int): ID del producto

        Returns:
            JSON: Datos del producto o error 404
        """
        # Validar que el ID sea positivo
<<<<<<< HEAD
        is_valid, error_msg = validate_positive_integer(id, "ID del producto")
        if not is_valid:
            return jsonify({"error": error_msg}), 400

        cur.execute("SELECT * FROM productos WHERE id=%s", (id,))
=======
        is_valid, error_msg = validate_positive_integer(pid, "ID del producto")
        if not is_valid:
            return jsonify({"error": error_msg}), 400

        cur.execute("SELECT * FROM productos WHERE id=%s", (pid,))
>>>>>>> ff66d95 (Actualizar proyecto final: Terminado carrito y correcciones de archivos .html)
        data = cur.fetchone()

        if not data:
            return jsonify({"error": "Producto no encontrado"}), 404
<<<<<<< HEAD
=======
        
        backend_url = "http://127.0.0.1:5000"
        
        if data.get("imagen"):
            data["imagen_url"] = f"{backend_url}/api/images/{data['imagen']}"
        else:
            data["imagen_url"] = None
>>>>>>> ff66d95 (Actualizar proyecto final: Terminado carrito y correcciones de archivos .html)

        return jsonify(data), 200

    # ----------------------------
    # POST /api/carrito → agregar
    # ----------------------------
    @app.post("/api/carrito")
    @with_database_connection(dictionary=False)
    def post_carrito(cur, conn):
<<<<<<< HEAD
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
=======
        data = request.get_json()

       
>>>>>>> ff66d95 (Actualizar proyecto final: Terminado carrito y correcciones de archivos .html)
        required_fields = ["usuario_id", "producto_id", "cantidad"]
        is_valid, error_msg = validate_required_fields(data, required_fields)
        if not is_valid:
            return jsonify({"error": error_msg}), 400

<<<<<<< HEAD
        # Validar que sean números positivos
=======
       
>>>>>>> ff66d95 (Actualizar proyecto final: Terminado carrito y correcciones de archivos .html)
        for field in required_fields:
            is_valid, error_msg = validate_positive_integer(data[field], field)
            if not is_valid:
                return jsonify({"error": error_msg}), 400

<<<<<<< HEAD
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
=======
        usuario_id = int(data["usuario_id"])
        producto_id = int(data["producto_id"])
        cantidad_a_agregar = int(data["cantidad"])

        cur.execute("SELECT stock FROM productos WHERE id = %s", (producto_id,))
        row = cur.fetchone()
        if not row:
            return jsonify({"error": "El producto no existe"}), 404

        stock_disponible = int(row[0])

        cur.execute("""
            SELECT cantidad
            FROM carrito
            WHERE usuario_id = %s AND producto_id = %s
        """, (usuario_id, producto_id))
        row = cur.fetchone()
        cantidad_actual = int(row[0]) if row else 0

        nueva_cantidad = cantidad_actual + cantidad_a_agregar

        if nueva_cantidad > stock_disponible:
            return jsonify({
                "error": f"Stock insuficiente. Máximo disponible: {stock_disponible}"
            }), 400

        query = """
            INSERT INTO carrito (usuario_id, producto_id, cantidad)
            VALUES (%s, %s, %s)
            ON DUPLICATE KEY UPDATE cantidad = %s
        """
        cur.execute(query, (usuario_id, producto_id, nueva_cantidad, nueva_cantidad))
        conn.commit()

        return jsonify({"status": "ok", "message": "Producto agregado al carrito"}), 201
    
    # ----------------------------
    # DELETE /api/carrito/<usuario_id>
    # ----------------------------
    @app.delete("/api/carrito/<int:uid>")
    @with_database_connection(dictionary=False)
    def delete_carrito(cur, conn, uid):
        """
        Vacía completamente el carrito del usuario.
        """
        # Validar ID positivo
        is_valid, error_msg = validate_positive_integer(uid, "ID del usuario")
        if not is_valid:
            return jsonify({"error": error_msg}), 400

        cur.execute("DELETE FROM carrito WHERE usuario_id = %s", (uid,))
        conn.commit()

        return jsonify({"status": "ok", "message": "Carrito vacío"}), 200
>>>>>>> ff66d95 (Actualizar proyecto final: Terminado carrito y correcciones de archivos .html)

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
<<<<<<< HEAD
        """
        Finaliza la compra del carrito de un usuario.

        Body JSON:
            - usuario_id (int): ID del usuario

        Returns:
            JSON: Información de la compra creada
        """
        data = request.get_json()

        # Validar campos requeridos
=======
        data = request.get_json()

>>>>>>> ff66d95 (Actualizar proyecto final: Terminado carrito y correcciones de archivos .html)
        required_fields = ["usuario_id"]
        is_valid, error_msg = validate_required_fields(data, required_fields)
        if not is_valid:
            return jsonify({"error": error_msg}), 400

        usuario_id = data["usuario_id"]

<<<<<<< HEAD
        # Validar que sea un número positivo
=======
>>>>>>> ff66d95 (Actualizar proyecto final: Terminado carrito y correcciones de archivos .html)
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
<<<<<<< HEAD
            cur.execute("SELECT precio FROM productos WHERE id=%s", (producto_id,))
            result = cur.fetchone()

            if not result:
                # Rollback si un producto no existe
=======
            cur.execute("SELECT precio, nombre FROM productos WHERE id=%s", (producto_id,))
            result = cur.fetchone()

            if not result:
>>>>>>> ff66d95 (Actualizar proyecto final: Terminado carrito y correcciones de archivos .html)
                conn.rollback()
                return jsonify({"error": f"Producto con ID {producto_id} no encontrado"}), 404

            precio = result[0]
<<<<<<< HEAD
=======
            nombre = result[1]
>>>>>>> ff66d95 (Actualizar proyecto final: Terminado carrito y correcciones de archivos .html)
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

<<<<<<< HEAD
=======
        # -----------------------------------------------------
        # Enviar email de confirmación al usuario
        # -----------------------------------------------------
        
        # Obtener email del usuario
        cur.execute("SELECT email, nombre FROM usuarios WHERE id=%s", (usuario_id,))
        user_data = cur.fetchone()

        if user_data:
            email_usuario, nombre_usuario = user_data

            # Obtener los items comprados (para mostrar en el email)
            cur.execute("""
                SELECT p.nombre, i.cantidad, i.precio_unitario, i.subtotal
                FROM items_compra i
                JOIN productos p ON p.id = i.producto_id
                WHERE i.compra_id = %s
            """, (compra_id,))
            items = cur.fetchall()

            # Crear contenido del email
            lineas_items = "\n".join([
                f"- {nombre} x{cantidad}: ${subtotal}"
                for (nombre, cantidad, precio, subtotal) in items
            ])

            cuerpo = f"""
            Hola {nombre_usuario},

            ¡Gracias por tu compra!

            Número de compra: {compra_id}
            Total pagado: ${total:.2f}

            Detalle:
            {lineas_items}

            ¡Gracias por confiar en nosotros!
            """

            msg = Message(
                subject="Confirmación de compra",
                recipients=[email_usuario],
                body=cuerpo
            )

            # Enviar email
            try:
                mail.send(msg)
            except Exception as e:
                print("Error enviando email:", e)

>>>>>>> ff66d95 (Actualizar proyecto final: Terminado carrito y correcciones de archivos .html)
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
