#!/bin/bash

# Script interactivo para configurar la base de datos

echo "======================================"
echo "Configuración de Base de Datos"
echo "======================================"
echo ""

# Solicitar credenciales
read -p "Usuario de MySQL (por defecto: root): " DB_USER
DB_USER=${DB_USER:-root}

read -sp "Contraseña de MySQL: " DB_PASS
echo ""

# Verificar conexión
echo ""
echo "Verificando conexión a MySQL..."
mysql -u "$DB_USER" -p"$DB_PASS" -e "SELECT 1;" > /dev/null 2>&1

if [ $? -ne 0 ]; then
    echo "❌ Error: No se pudo conectar a MySQL con esas credenciales"
    echo ""
    echo "Posibles soluciones:"
    echo "  1. Verifica que MySQL esté corriendo"
    echo "  2. Verifica tu usuario y contraseña"
    echo "  3. Si es la primera vez, puede que necesites configurar MySQL"
    exit 1
fi

echo "✅ Conexión exitosa"
echo ""

# Crear base de datos
echo "Creando base de datos 'base_tp'..."
mysql -u "$DB_USER" -p"$DB_PASS" <<EOF
CREATE DATABASE IF NOT EXISTS base_tp;
USE base_tp;
SOURCE database/schema.sql;
SOURCE database/data.sql;
EOF

if [ $? -eq 0 ]; then
    echo "✅ Base de datos creada exitosamente"

    # Verificar datos
    PRODUCTOS_COUNT=$(mysql -u "$DB_USER" -p"$DB_PASS" -D base_tp -se "SELECT COUNT(*) FROM productos;")
    echo "✅ $PRODUCTOS_COUNT productos cargados"

    # Actualizar .env
    echo ""
    echo "Actualizando archivo backend/.env..."
    cat > backend/.env <<ENVEOF
# Configuración de Base de Datos
DB_HOST=localhost
DB_USER=$DB_USER
DB_PASSWORD=$DB_PASS
DB_NAME=base_tp
DB_PORT=3306

# Configuración de Flask
FLASK_DEBUG=True
FLASK_HOST=127.0.0.1
FLASK_PORT=5000

# Configuración de CORS
CORS_ORIGINS=*
ENVEOF

    echo "✅ Archivo .env actualizado"
    echo ""
    echo "======================================"
    echo "✅ Configuración completada"
    echo "======================================"
    echo ""
    echo "Ahora puedes ejecutar:"
    echo "  1. cd backend && python3 app.py"
    echo "  2. cd frontend && python3 app.py (en otra terminal)"
else
    echo "❌ Error al crear la base de datos"
    exit 1
fi
