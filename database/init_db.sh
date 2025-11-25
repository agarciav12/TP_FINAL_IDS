#!/bin/bash

# Script para inicializar la base de datos
# Uso: ./init_db.sh [usuario] [contraseña]

DB_USER=${1:-root}
DB_PASS=${2}

echo "======================================"
echo "Inicializando Base de Datos"
echo "======================================"

if [ -z "$DB_PASS" ]; then
    echo "Ingrese la contraseña de MySQL para el usuario '$DB_USER':"
    mysql -u "$DB_USER" -p <<EOF
CREATE DATABASE IF NOT EXISTS base_tp;
USE base_tp;
SOURCE schema.sql;
SOURCE data.sql;
EOF
else
    mysql -u "$DB_USER" -p"$DB_PASS" <<EOF
CREATE DATABASE IF NOT EXISTS base_tp;
USE base_tp;
SOURCE schema.sql;
SOURCE data.sql;
EOF
fi

if [ $? -eq 0 ]; then
    echo "✓ Base de datos creada exitosamente"
    echo "✓ Tablas creadas"
    echo "✓ Datos de ejemplo cargados"
    echo ""
    echo "Puedes conectarte con:"
    echo "  mysql -u $DB_USER -p base_tp"
else
    echo "✗ Error al inicializar la base de datos"
    exit 1
fi
