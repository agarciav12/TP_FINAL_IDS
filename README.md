# TP Final - Introducción al Desarrollo de Software

Aplicación web de e-commerce desarrollada con Flask (backend y frontend) y MySQL, siguiendo buenas prácticas de programación.

## Características del Proyecto

- ✅ Sin variables globales (Factory Pattern)
- ✅ Código modularizado y reutilizable
- ✅ Manejo completo de errores
- ✅ Validaciones de entrada
- ✅ Arquitectura RESTful
- ✅ Base de datos MySQL con 5 tablas
- ✅ 30+ productos de ejemplo precargados

## Requisitos

- Python 3.8+
- MySQL 5.7+
- pip

## Estructura del Proyecto

```
TP_FINAL_IDS/
├── backend/              # API RESTful con Flask
│   ├── app.py            # Endpoints (Factory Pattern)
│   ├── db.py             # Conexión a la base de datos
│   ├── config.py         # Configuración (sin variables globales)
│   ├── utils.py          # Decoradores y validaciones
│   ├── .env              # Variables de entorno (no versionado)
│   ├── .env.example      # Plantilla de variables de entorno
│   └── requirments.txt   # Dependencias
├── frontend/             # Interfaz web con Flask
│   ├── app.py            # Rutas (Factory Pattern)
│   ├── config.py         # Configuración
│   ├── utils.py          # Funciones auxiliares
│   ├── templates/        # Plantillas HTML
│   │   └── error.html    # Página de error personalizada
│   ├── static/           # CSS, JS, imágenes
│   ├── .env              # Variables de entorno (no versionado)
│   └── .env.example      # Plantilla de variables de entorno
├── database/             # Scripts de base de datos
│   ├── schema.sql        # Creación de tablas
│   ├── data.sql          # 30+ productos de ejemplo
│   └── init_db.sh        # Script de inicialización
├── BUENAS_PRACTICAS.md   # Verificación de buenas prácticas
├── CORRECCIONES.md       # Detalle de correcciones realizadas
└── README.md             # Este archivo
```

## Instalación

### 1. Clonar el repositorio

```bash
git clone <url-del-repositorio>
cd TP_FINAL_IDS
```

### 2. Crear entorno virtual

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 3. Instalar dependencias del backend

```bash
cd backend
pip install -r requirments.txt
cd ..
```

**Nota:** El frontend usa las mismas dependencias del backend.

### 4. Configurar la base de datos

#### Crear la base de datos en MySQL:

```bash
mysql -u root -p
```

```sql
CREATE DATABASE base_tp;
USE base_tp;
SOURCE database/schema.sql;
SOURCE database/data.sql;
```

#### Configurar variables de entorno:

**Backend:**
```bash
cp backend/.env.example backend/.env
```

Edita `backend/.env` con tus credenciales de MySQL:
```
DB_HOST=localhost
DB_USER=tu_usuario
DB_PASSWORD=tu_contraseña
DB_NAME=base_tp
DB_PORT=3306

FLASK_DEBUG=True
FLASK_HOST=127.0.0.1
FLASK_PORT=5000

CORS_ORIGINS=*
```

**Frontend:**
```bash
cp frontend/.env.example frontend/.env
```

Edita `frontend/.env` si necesitas cambiar la configuración:
```
FLASK_DEBUG=True
FLASK_HOST=127.0.0.1
FLASK_PORT=5001

BACKEND_URL=http://127.0.0.1:5000/api
```

## Ejecución

### Iniciar el Backend (Terminal 1)

```bash
cd backend
python app.py
```

El backend estará disponible en: `http://localhost:5000`

### Iniciar el Frontend (Terminal 2)

```bash
cd frontend
python app.py
```

El frontend estará disponible en: `http://localhost:5001`

## Endpoints de la API

### Productos

- **GET** `/api/productos` - Listar todos los productos
  - Query params: `?categoria=<nombre>` (opcional)

- **GET** `/api/productos/<id>` - Obtener un producto específico

### Carrito

- **GET** `/api/carrito/<usuario_id>` - Obtener carrito del usuario

- **POST** `/api/carrito` - Agregar producto al carrito
  ```json
  {
    "usuario_id": 1,
    "producto_id": 5,
    "cantidad": 2
  }
  ```

### Compras

- **POST** `/api/compras` - Finalizar compra
  ```json
  {
    "usuario_id": 1
  }
  ```

## Base de Datos

### Tablas

1. **productos** - Catálogo de productos
2. **usuarios** - Usuarios registrados
3. **carrito** - Items en el carrito de cada usuario
4. **compras** - Registro de compras finalizadas
5. **items_compra** - Detalle de productos en cada compra

### Diagrama de Relaciones

```
usuarios ──┬── carrito ── productos
           └── compras ── items_compra ── productos
```

## Tecnologías Utilizadas

- **Backend**: Flask 3.1.2, MySQL Connector 9.5.0
- **Frontend**: Flask 3.1.2, Jinja2, Requests 2.32.5
- **Base de Datos**: MySQL
- **Seguridad**: python-dotenv 1.0.0, variables de entorno
- **Otros**: Flask-CORS 6.0.1, Bootstrap (frontend)

## Características

- Arquitectura RESTful
- Separación frontend/backend
- Gestión de carrito de compras
- Sistema de compras
- Filtrado por categorías
- Datos de ejemplo precargados

## Buenas Prácticas Implementadas

Este proyecto sigue estrictamente las buenas prácticas de programación:

### ✅ Evitado:
- ❌ Variables globales (se usa Factory Pattern)
- ❌ Ciclos infinitos
- ❌ Código repetido (decoradores y funciones reutilizables)
- ❌ Errores sin manejar (try-catch completo)

### ✅ Implementado:
- ✅ Modularización del código (4 módulos por aplicación)
- ✅ Manejo completo de errores y validaciones
- ✅ Documentación (docstrings y comentarios)
- ✅ Seguridad (credenciales en .env, SQL parametrizado)
- ✅ Patrones de diseño (Factory, Decorator)

Ver [BUENAS_PRACTICAS.md](BUENAS_PRACTICAS.md) para verificación completa.

## Notas de Seguridad

- Las contraseñas en `data.sql` están hasheadas con bcrypt (password de ejemplo: `demo123`)
- Los archivos `.env` contienen credenciales sensibles y NO deben versionarse
- CORS está habilitado para permitir comunicación entre frontend y backend
- Todas las queries SQL están parametrizadas (previene SQL injection)
- Se validan todas las entradas del usuario

## Documentación Adicional

- **[README_PRUEBAS.md](README_PRUEBAS.md)** - 🧪 **Guía completa para probar el proyecto paso a paso**
- **[EXPLICACION_CAMBIOS.md](EXPLICACION_CAMBIOS.md)** - 📝 **Explicación detallada de TODOS los cambios realizados**
- [BUENAS_PRACTICAS.md](BUENAS_PRACTICAS.md) - Verificación detallada de todas las buenas prácticas
- [CORRECCIONES.md](CORRECCIONES.md) - Historial de correcciones aplicadas al proyecto
- [RESUMEN_FINAL.md](RESUMEN_FINAL.md) - Resumen ejecutivo del proyecto
- [CAMBIOS_APLICADOS.md](CAMBIOS_APLICADOS.md) - Resumen de cambios realizados

## 🚀 Inicio Rápido

Si quieres probar el proyecto rápidamente:

```bash
# 1. Instalar dependencias
pip3 install -r backend/requirments.txt

# 2. Configurar base de datos (te pedirá credenciales de MySQL)
./setup_database.sh

# 3. Iniciar backend (Terminal 1)
cd backend && python3 app.py

# 4. Iniciar frontend (Terminal 2)
cd frontend && python3 app.py

# 5. Abrir navegador
# http://localhost:5001
```

Para instrucciones detalladas, ver **[README_PRUEBAS.md](README_PRUEBAS.md)**
