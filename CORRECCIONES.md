# Resumen de Correcciones Realizadas

## 1. Schema de Base de Datos (`database/schema.sql`)

### Problemas encontrados:
- Columna `categoria` duplicada (definida en CREATE TABLE y luego con ALTER TABLE)
- Faltaban restricciones NOT NULL en campos importantes
- Sin valores DEFAULT recomendados
- Faltaban ON DELETE CASCADE para integridad referencial

### Soluciones aplicadas:
- Eliminado el ALTER TABLE duplicado
- Agregadas restricciones NOT NULL donde corresponde
- Agregados valores DEFAULT (stock = 0, cantidad = 1)
- Agregadas cláusulas ON DELETE CASCADE en foreign keys
- Mejorado el formato y consistencia del código SQL

## 2. Script de Carga (`database/data.sql`)

### Problemas encontrados:
- Archivo completamente vacío
- Sin datos de ejemplo para probar la aplicación

### Soluciones aplicadas:
- Creados **30 productos** de ejemplo en 5 categorías:
  - Electrónica (8 productos)
  - Ropa (6 productos)
  - Hogar (6 productos)
  - Deportes (5 productos)
  - Libros (5 productos)
- Creados **3 usuarios** de ejemplo
- Agregados **5 items** en carritos de ejemplo
- Creada **1 compra** de ejemplo con sus items

## 3. Configuración de Credenciales (`backend/db.py`)

### Problemas encontrados:
- Credenciales hardcodeadas directamente en el código
- Riesgo de seguridad al versionar contraseñas

### Soluciones aplicadas:
- Implementadas variables de entorno con `python-dotenv`
- Creado archivo `.env` con las credenciales actuales
- Creado archivo `.env.example` como plantilla
- Agregados valores por defecto seguros
- Agregada dependencia `python-dotenv==1.0.0` a `requirments.txt`

## 4. CORS en Backend (`backend/app.py`)

### Problemas encontrados:
- `flask-cors` instalado pero no configurado
- Posibles problemas de CORS al comunicarse con frontend

### Soluciones aplicadas:
- Importado y habilitado Flask-CORS
- CORS ahora permite todas las peticiones desde el frontend

## 5. Archivos Adicionales Creados

### `.gitignore`
- Protege archivos sensibles (.env)
- Excluye archivos generados por Python (__pycache__, etc.)
- Excluye archivos de IDEs y sistema operativo

### `README.md`
- Documentación completa del proyecto
- Instrucciones de instalación paso a paso
- Documentación de todos los endpoints
- Diagrama de base de datos
- Guía de uso

### `database/init_db.sh`
- Script automatizado para inicializar la base de datos
- Crea la base de datos
- Ejecuta schema.sql y data.sql
- Uso: `./database/init_db.sh [usuario] [contraseña]`

## Verificación de Requisitos

### ✅ Requisitos Cumplidos:

1. **Base de datos MySQL con al menos 2 tablas**
   - ✓ 5 tablas creadas (productos, usuarios, carrito, compras, items_compra)
   - ✓ Script de creación (schema.sql)
   - ✓ Script de carga (data.sql) con 30+ registros

2. **Backend con Flask conectado a MySQL**
   - ✓ Backend en Flask funcionando
   - ✓ Conexión a MySQL mediante mysql-connector-python
   - ✓ Variables de entorno para credenciales

3. **Endpoints RESTful con verbos correctos y JSON**
   - ✓ GET /api/productos
   - ✓ GET /api/productos/<id>
   - ✓ GET /api/carrito/<usuario_id>
   - ✓ POST /api/carrito
   - ✓ POST /api/compras
   - ✓ Todos usan formato JSON

4. **Frontend con Flask consumiendo backend**
   - ✓ Frontend en Flask separado
   - ✓ Consume API del backend con requests
   - ✓ Respeta arquitectura RESTful

## Próximos Pasos Recomendados

1. **Instalar la nueva dependencia:**
   ```bash
   pip install python-dotenv
   ```

2. **Verificar el archivo .env:**
   - Revisar `backend/.env` con tus credenciales correctas

3. **Reinicializar la base de datos:**
   ```bash
   cd database
   ./init_db.sh tu_usuario
   ```
   O manualmente:
   ```bash
   mysql -u root -p < schema.sql
   mysql -u root -p base_tp < data.sql
   ```

4. **Probar la aplicación:**
   - Terminal 1: `cd backend && python app.py`
   - Terminal 2: `cd frontend && python app.py`
   - Abrir navegador en: http://localhost:5001

## Mejoras Adicionales Sugeridas (Opcionales)

- [ ] Agregar endpoint DELETE para el carrito
- [ ] Agregar endpoint PUT para actualizar cantidad en carrito
- [ ] Implementar autenticación de usuarios
- [ ] Agregar manejo de errores más robusto
- [ ] Agregar validaciones de entrada
- [ ] Implementar paginación en listado de productos
- [ ] Agregar tests unitarios
- [ ] Dockerizar la aplicación
