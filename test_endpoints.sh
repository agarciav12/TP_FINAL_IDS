#!/bin/bash

# Script de prueba de endpoints del backend
# Asegúrate de que el backend esté corriendo antes de ejecutar este script

BACKEND_URL="http://127.0.0.1:5000/api"

echo "======================================"
echo "Prueba de Endpoints - Backend API"
echo "======================================"
echo ""

# Colores para output
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${YELLOW}1. Probando GET /api/productos${NC}"
echo "   URL: $BACKEND_URL/productos"
curl -s -w "\n   Status: %{http_code}\n" "$BACKEND_URL/productos" | head -5
echo ""

echo -e "${YELLOW}2. Probando GET /api/productos con filtro por categoría${NC}"
echo "   URL: $BACKEND_URL/productos?categoria=Electrónica"
curl -s -w "\n   Status: %{http_code}\n" "$BACKEND_URL/productos?categoria=Electrónica" | head -5
echo ""

echo -e "${YELLOW}3. Probando GET /api/productos/1${NC}"
echo "   URL: $BACKEND_URL/productos/1"
curl -s -w "\n   Status: %{http_code}\n" "$BACKEND_URL/productos/1"
echo ""

echo -e "${YELLOW}4. Probando GET /api/carrito/1${NC}"
echo "   URL: $BACKEND_URL/carrito/1"
curl -s -w "\n   Status: %{http_code}\n" "$BACKEND_URL/carrito/1"
echo ""

echo -e "${YELLOW}5. Probando POST /api/carrito${NC}"
echo "   URL: $BACKEND_URL/carrito"
echo '   Body: {"usuario_id": 1, "producto_id": 5, "cantidad": 2}'
curl -s -X POST \
  -H "Content-Type: application/json" \
  -d '{"usuario_id": 1, "producto_id": 5, "cantidad": 2}' \
  -w "\n   Status: %{http_code}\n" \
  "$BACKEND_URL/carrito"
echo ""

echo -e "${YELLOW}6. Probando validación - POST con datos inválidos${NC}"
echo "   URL: $BACKEND_URL/carrito"
echo '   Body: {"usuario_id": -1, "producto_id": 5}'
curl -s -X POST \
  -H "Content-Type: application/json" \
  -d '{"usuario_id": -1, "producto_id": 5}' \
  -w "\n   Status: %{http_code}\n" \
  "$BACKEND_URL/carrito"
echo ""

echo -e "${YELLOW}7. Probando endpoint inexistente${NC}"
echo "   URL: $BACKEND_URL/noexiste"
curl -s -w "\n   Status: %{http_code}\n" "$BACKEND_URL/noexiste"
echo ""

echo "======================================"
echo -e "${GREEN}Pruebas completadas${NC}"
echo "======================================"
echo ""
echo "Notas:"
echo "  - Status 200: Éxito"
echo "  - Status 201: Creado"
echo "  - Status 400: Error de validación (esperado)"
echo "  - Status 404: No encontrado (esperado)"
echo "  - Status 500: Error del servidor"
