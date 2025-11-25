# 🧪 Guía de Pruebas - TP Final IDS

Esta guía te ayudará a probar el proyecto paso a paso desde cero.

---

## 📋 Requisitos Previos

Antes de comenzar, asegúrate de tener instalado:

- ✅ **Python 3.8+** - Verificar: `python3 --version`
- ✅ **MySQL 5.7+** - Verificar: `mysql --version`
- ✅ **pip** - Verificar: `pip3 --version`

---

## 🚀 Guía de Prueba Rápida (5 minutos)

### Paso 1: Instalar Dependencias (1 min)

```bash
cd /Users/juantapia/Downloads/TP_FINAL_IDS/backend
pip3 install -r requirments.txt
```

**Salida esperada:**
```
Successfully installed Flask-3.1.2 flask-cors-6.0.1 mysql-connector-python-9.5.0 python-dotenv-1.0.0 ...
```

---

### Paso 2: Configurar Base de Datos (2 min)

Ejecuta el script de configuración automático:

```bash
cd /Users/juantapia/Downloads/TP_FINAL_IDS
./setup_database.sh
```

El script te pedirá:

```
Usuario de MySQL (por defecto: root): [presiona Enter o escribe tu usuario]
Contraseña de MySQL: [escribe tu contraseña]
```

**Salida esperada:**
```
✅ Conexión exitosa
✅ Base de datos creada exitosamente
✅ 30 productos cargados
✅ Archivo .env actualizado
✅ Configuración completada
```

---

### Paso 3: Iniciar el Backend (30 seg)

**En la Terminal 1:**

```bash
cd /Users/juantapia/Downloads/TP_FINAL_IDS/backend
python3 app.py
```

**Salida esperada:**
```
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

🎯 **¡Deja esta terminal abierta y corriendo!**

---

### Paso 4: Iniciar el Frontend (30 seg)

**En una NUEVA Terminal 2:**

```bash
cd /Users/juantapia/Downloads/TP_FINAL_IDS/frontend
python3 app.py
```

**Salida esperada:**
```
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5001
Press CTRL+C to quit
```

🎯 **¡Deja también esta terminal abierta!**

---

### Paso 5: Probar en el Navegador (1 min)

Abre tu navegador y visita:

#### 🌐 Página Principal
```
http://localhost:5001
```

#### 🛍️ Páginas para probar:

1. **Lista de productos:**
   ```
   http://localhost:5001/productos
   ```

2. **Filtrado por categoría:**
   ```
   http://localhost:5001/productos?categoria=Electrónica
   http://localhost:5001/productos?categoria=Ropa
   http://localhost:5001/productos?categoria=Deportes
   ```

3. **Detalle de un producto:**
   ```
   http://localhost:5001/producto/1
   http://localhost:5001/producto/5
   ```

4. **Sobre Nosotros:**
   ```
   http://localhost:5001/about
   ```

5. **Contacto:**
   ```
   http://localhost:5001/contacto
   ```

---

### Paso 6: Probar los Endpoints de la API (Opcional)

**En una NUEVA Terminal 3:**

```bash
cd /Users/juantapia/Downloads/TP_FINAL_IDS
./test_endpoints.sh
```

**Salida esperada:**
```
======================================
Prueba de Endpoints - Backend API
======================================

1. Probando GET /api/productos
   URL: http://127.0.0.1:5000/api/productos
   [{"id": 1, "nombre": "Laptop Dell XPS 13", ...}]
   Status: 200

2. Probando GET /api/productos con filtro por categoría
   Status: 200

...

✅ Pruebas completadas
```

---

## 🔧 Solución de Problemas Comunes

### Problema 1: "Access denied for user"

**Error:**
```
ERROR 1045 (28000): Access denied for user 'agus'@'localhost'
```

**Solución:**

1. Verifica que MySQL esté corriendo:
   ```bash
   # macOS con Homebrew
   brew services list | grep mysql
   brew services start mysql

   # Linux
   sudo systemctl status mysql
   sudo systemctl start mysql
   ```

2. Si no conoces las credenciales, conéctate como root:
   ```bash
   mysql -u root -p
   # Si no tiene contraseña, solo: mysql -u root
   ```

3. Dentro de MySQL, crea el usuario:
   ```sql
   CREATE USER 'agus'@'localhost' IDENTIFIED BY 'Agus_DB_1206';
   GRANT ALL PRIVILEGES ON *.* TO 'agus'@'localhost';
   FLUSH PRIVILEGES;
   EXIT;
   ```

4. Vuelve a ejecutar `./setup_database.sh`

---

### Problema 2: "Port 5000 already in use"

**Error:**
```
OSError: [Errno 48] Address already in use
```

**Solución:**

**Opción A:** Matar el proceso que está usando el puerto:
```bash
# Encontrar el proceso
lsof -ti:5000

# Matar el proceso
kill -9 $(lsof -ti:5000)
```

**Opción B:** Cambiar el puerto en `backend/.env`:
```bash
# Editar backend/.env
FLASK_PORT=5002  # Cambiar de 5000 a 5002
```

Luego actualizar `frontend/.env`:
```bash
BACKEND_URL=http://127.0.0.1:5002/api  # Cambiar el puerto
```

---

### Problema 3: "Module not found"

**Error:**
```
ModuleNotFoundError: No module named 'flask'
```

**Solución:**

Asegúrate de estar usando `python3` y no `python`:
```bash
python3 -m pip install -r backend/requirments.txt
python3 app.py  # No usar solo 'python'
```

---

### Problema 4: "Database does not exist"

**Error:**
```
mysql.connector.errors.ProgrammingError: 1049 (42000): Unknown database 'base_tp'
```

**Solución:**

Ejecuta el script de configuración:
```bash
./setup_database.sh
```

O manualmente:
```bash
mysql -u root -p <<EOF
CREATE DATABASE base_tp;
USE base_tp;
SOURCE database/schema.sql;
SOURCE database/data.sql;
EOF
```

---

### Problema 5: "Cannot connect to backend"

**Error en el navegador:**
```
Error al obtener productos: No se pudo conectar con el servidor
```

**Solución:**

1. Verifica que el backend esté corriendo:
   ```bash
   # Debería mostrar algo en el puerto 5000
   lsof -ti:5000
   ```

2. Si no está corriendo:
   ```bash
   cd backend
   python3 app.py
   ```

3. Verifica la URL en `frontend/.env`:
   ```bash
   cat frontend/.env
   # Debe tener: BACKEND_URL=http://127.0.0.1:5000/api
   ```

---

## 🧪 Pruebas Manuales de los Endpoints

### 1. Listar todos los productos

```bash
curl http://localhost:5000/api/productos
```

**Respuesta esperada:**
```json
[
  {
    "id": 1,
    "nombre": "Laptop Dell XPS 13",
    "categoria": "Electrónica",
    "precio": 1299.99,
    "stock": 15
  },
  ...
]
```

---

### 2. Filtrar por categoría

```bash
curl "http://localhost:5000/api/productos?categoria=Electrónica"
```

---

### 3. Obtener un producto específico

```bash
curl http://localhost:5000/api/productos/1
```

---

### 4. Ver carrito de un usuario

```bash
curl http://localhost:5000/api/carrito/1
```

---

### 5. Agregar producto al carrito

```bash
curl -X POST http://localhost:5000/api/carrito \
  -H "Content-Type: application/json" \
  -d '{
    "usuario_id": 1,
    "producto_id": 5,
    "cantidad": 2
  }'
```

**Respuesta esperada:**
```json
{
  "status": "ok",
  "message": "Producto agregado al carrito"
}
```

---

### 6. Finalizar compra

```bash
curl -X POST http://localhost:5000/api/compras \
  -H "Content-Type: application/json" \
  -d '{
    "usuario_id": 1
  }'
```

**Respuesta esperada:**
```json
{
  "status": "ok",
  "compra_id": 1,
  "total": 499.98,
  "message": "Compra realizada exitosamente"
}
```

---

## 🧪 Pruebas de Validaciones

### Probar validación de campos requeridos

```bash
curl -X POST http://localhost:5000/api/carrito \
  -H "Content-Type: application/json" \
  -d '{
    "usuario_id": 1
  }'
```

**Respuesta esperada (Error 400):**
```json
{
  "error": "Faltan campos requeridos: producto_id, cantidad"
}
```

---

### Probar validación de números positivos

```bash
curl -X POST http://localhost:5000/api/carrito \
  -H "Content-Type: application/json" \
  -d '{
    "usuario_id": -1,
    "producto_id": 5,
    "cantidad": 2
  }'
```

**Respuesta esperada (Error 400):**
```json
{
  "error": "usuario_id debe ser un número positivo"
}
```

---

### Probar producto inexistente

```bash
curl http://localhost:5000/api/productos/999
```

**Respuesta esperada (Error 404):**
```json
{
  "error": "Producto no encontrado"
}
```

---

## 📊 Verificar Base de Datos

### Conectarse a MySQL

```bash
mysql -u agus -pAgus_DB_1206 base_tp
```

### Consultas útiles

```sql
-- Ver todos los productos
SELECT * FROM productos;

-- Ver productos por categoría
SELECT * FROM productos WHERE categoria = 'Electrónica';

-- Ver usuarios
SELECT id, nombre, email FROM usuarios;

-- Ver carritos activos
SELECT u.nombre, p.nombre AS producto, c.cantidad
FROM carrito c
JOIN usuarios u ON u.id = c.usuario_id
JOIN productos p ON p.id = c.producto_id;

-- Ver compras realizadas
SELECT c.id, u.nombre, c.fecha, c.total
FROM compras c
JOIN usuarios u ON u.id = c.usuario_id;

-- Ver items de una compra
SELECT p.nombre, i.cantidad, i.precio_unitario, i.subtotal
FROM items_compra i
JOIN productos p ON p.id = i.producto_id
WHERE i.compra_id = 1;
```

---

## 📸 Screenshots de lo que deberías ver

### 1. Backend corriendo:
```
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
```

### 2. Frontend corriendo:
```
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5001
```

### 3. Navegador mostrando la página principal

### 4. Lista de productos con precios y categorías

---

## ✅ Checklist de Pruebas Completas

Marca cada elemento cuando lo pruebes:

### Backend
- [ ] Backend inicia sin errores
- [ ] GET /api/productos devuelve lista de productos
- [ ] GET /api/productos?categoria=X filtra correctamente
- [ ] GET /api/productos/1 devuelve un producto específico
- [ ] GET /api/productos/999 devuelve error 404
- [ ] POST /api/carrito agrega productos
- [ ] POST /api/carrito valida campos requeridos
- [ ] POST /api/carrito valida números positivos
- [ ] GET /api/carrito/1 muestra el carrito
- [ ] POST /api/compras finaliza la compra

### Frontend
- [ ] Frontend inicia sin errores
- [ ] Página principal (/) carga correctamente
- [ ] /productos muestra lista de productos
- [ ] /productos?categoria=X filtra por categoría
- [ ] /producto/1 muestra detalle del producto
- [ ] /about carga la página "Sobre Nosotros"
- [ ] /contacto carga el formulario de contacto
- [ ] Errores muestran página personalizada

### Base de Datos
- [ ] Conexión a MySQL exitosa
- [ ] Base de datos base_tp creada
- [ ] 5 tablas creadas (productos, usuarios, carrito, compras, items_compra)
- [ ] 30+ productos cargados
- [ ] 3 usuarios cargados
- [ ] Datos de ejemplo en carrito

---

## 🎯 Prueba Completa en 3 Comandos

Si ya tienes MySQL configurado:

```bash
# 1. Instalar dependencias
pip3 install -r backend/requirments.txt

# 2. Configurar base de datos
./setup_database.sh

# 3. Iniciar aplicación (en terminales separadas)
cd backend && python3 app.py  # Terminal 1
cd frontend && python3 app.py  # Terminal 2
```

Luego abre: http://localhost:5001

---

## 📞 Soporte

Si encuentras algún problema:

1. Revisa la sección "Solución de Problemas Comunes"
2. Verifica los logs en las terminales del backend y frontend
3. Consulta los archivos de documentación:
   - `README.md` - Documentación general
   - `BUENAS_PRACTICAS.md` - Verificación de requisitos
   - `CORRECCIONES.md` - Historial de cambios

---

## 🎓 Demostración para Evaluación

### Orden recomendado para demostrar el proyecto:

1. **Mostrar la estructura del código** (2 min)
   - Explicar modularización (app.py, config.py, utils.py, db.py)
   - Mostrar Factory Pattern en app.py
   - Mostrar decorador @with_database_connection

2. **Mostrar la base de datos** (2 min)
   ```bash
   mysql -u agus -pAgus_DB_1206 base_tp -e "SHOW TABLES;"
   mysql -u agus -pAgus_DB_1206 base_tp -e "SELECT COUNT(*) FROM productos;"
   ```

3. **Iniciar backend** (1 min)
   ```bash
   cd backend && python3 app.py
   ```
   Mostrar que inicia sin errores

4. **Probar endpoints con curl** (3 min)
   ```bash
   # En otra terminal
   ./test_endpoints.sh
   ```
   Mostrar respuestas JSON y validaciones

5. **Iniciar frontend** (1 min)
   ```bash
   cd frontend && python3 app.py
   ```

6. **Demostración en navegador** (5 min)
   - Página principal
   - Lista de productos
   - Filtrado por categoría
   - Detalle de producto
   - Mostrar página de error (producto inexistente)

7. **Mostrar buenas prácticas** (2 min)
   - Abrir `BUENAS_PRACTICAS.md`
   - Mostrar checklist completo
   - Mencionar: sin variables globales, manejo de errores, validaciones

**Tiempo total: 15-20 minutos**

---

*Última actualización: Noviembre 2024*
*Proyecto: TP Final - Introducción al Desarrollo de Software*
