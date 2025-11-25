# 🛒 TP Final IDS – Carrito de Compras *ZonaGamer*

**Materia:** Introducción al Desarrollo de Software (IDS)  
**Equipo:** Agustín García – Ana Angélica Moshkov  
**Tema:** Aplicación de comercio electrónico (e-commerce) para venta de componentes y periféricos de PC.

---

# 🎯 1. Alcance del Proyecto

El proyecto implementa un **carrito de compras funcional** que demuestra la comunicación **RESTful** entre un *Frontend* y un *Backend* conectados a una base de datos.

### ✔️ Incluye (Requerimientos Funcionales)
- Catálogo de productos con precios  
- Vista de detalle de producto  
- Funcionalidad para agregar y quitar productos del carrito  
- Vista del carrito con cálculo del total  
- Proceso básico de checkout  

### ❌ No incluye
- Autenticación de usuarios (se usa un ID fijo)  
- Pasarelas de pago reales  
- Gestión de stock en tiempo real  

---

# ⚙️ 2. Arquitectura y Tecnologías

El proyecto está dividido en **dos aplicaciones Flask** independientes (Frontend y Backend) siguiendo una arquitectura **RESTful**.

### 🧰 Tecnologías Utilizadas
- **Lenguaje:** Python 3.x  
- **Framework:** Flask  
- **Base de Datos:** MySQL  
- **Frontend:** HTML5, CSS (Template *Zay*), Jinja2  

---

## 📁 Estructura de Carpetas

TP_FINAL_IDS/
├─ backend/                     # API RESTful (Puerto 5000)
│  ├─ app.py                    # Endpoints y conexión a la BD
│  ├─ db.py
│  ├─ requirements.txt          # Dependencias de Python
│  └─ database/                 # Scripts SQL
│
├─ frontend/                    # Aplicación Web (Puerto 5001)
│  ├─ app.py                    # Rutas HTML que consumen la API
│  ├─ static/                   # CSS, JS, imágenes
│  └─ templates/                # HTML (index, productos, about, contact, etc.)
│
└─ .gitignore


---

# 🚀 3. Guía de Instalación y Ejecución

Para ejecutar la aplicación localmente, se deben iniciar **Backend** y **Frontend** por separado.

---

## A. Configuración Inicial (solo una vez)

### 1️⃣ Clonar el repositorio

git clone https://github.com/agarciav12/TP_FINAL_IDS.git
cd TP_FINAL_IDS

### 2️⃣ Crear y activar entorno virtual
python3 -m venv venv
source venv/bin/activate

### 3️⃣ Instalar dependencias
pip install -r backend/requirements.txt

### 4️⃣ Configurar Base de Datos MySQL

- Requiere un servidor MySQL corriendo

- Usar el script dentro de backend/database/ para crear la BD

- Incluye también setup_database.sh

---

### B. Ejecución
🟦 Terminal 1 – Backend (API)
(venv) python backend/app.py


Disponible en: http://127.0.0.1:5000/

🟩 Terminal 2 – Frontend (Web)
(venv) python frontend/app.py


Disponible en: http://127.0.0.1:5001/

---

### 🔗 4. Endpoints Clave del Backend (API)

| Método | Endpoint | Descripción | Requisito |
| :--- | :--- | :--- | :--- |
| **GET** | `/api/productos` | Obtiene el catálogo completo (o filtrado). | Mostrar catálogo |
| **GET** | `/api/productos/<id>` | Obtiene el detalle de un solo producto. | Detalle de Producto |
| **POST** | `/api/carrito` | Agrega un producto al carrito. | Funcionalidad Carrito |
| **GET** | `/api/carrito/<uid>` | Obtiene el contenido del carrito de un usuario. | Mostrar Carrito |

---

### 🧑‍💻 5. Metodología y Contribución

- Se utilizó GitHub para la gestión del código
- Las tareas se organizaron con un tablero Kanban en GitHub Projects
- Todos los integrantes realizaron commits asociados a tareas
- Se aplicaron buenas prácticas de programación durante el desarrollo
