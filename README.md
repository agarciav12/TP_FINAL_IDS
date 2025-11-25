
# 🛒 TP Final IDS - Carrito de Compras ZonaGamer

**Materia:** Introducción al Desarrollo de Software (IDS)
**Equipo:** Agustin García - Ana Angélica Moshkov
**Tema:** Aplicación de comercio electrónico (e-commerce) para la venta de componentes y periféricos de PC.

---

## 🎯 1. Alcance del Proyecto

[cite_start]El proyecto implementa un carrito de compras funcional que demuestra la **comunicación RESTful** entre un Frontend y un Backend, conectados a una base de datos[cite: 29, 31].

**Incluye (Requerimientos Funcionales):**
* Catálogo de productos con precios.
* Vista de detalle de producto.
* Funcionalidad para **agregar y quitar productos del carrito**.
* Vista de carrito que calcula el total.
* Proceso de finalización de compra (*checkout*).

**No Incluye:**
* Autenticación de usuarios (trabaja con un ID de usuario fijo para el carrito).
* Pasarelas de pago reales.
* Gestión de stock en tiempo real.

---

## ⚙️ 2. Arquitectura y Tecnologías

[cite_start]El proyecto está dividido en dos aplicaciones Flask separadas (Frontend y Backend), respetando la arquitectura RESTful[cite: 31].

### Tecnologías Utilizadas

* **Lenguaje:** Python 3.x
* [cite_start]**Framework:** **Flask** (para Backend API y Frontend)[cite: 29, 31].
* [cite_start]**Base de Datos:** **MySQL**[cite: 28].
* **Front-End:** HTML5, CSS (Template Zay), Jinja2 (para renderizado dinámico).

### Estructura de Carpetas
TP_FINAL_IDS/ 
            ├─ backend/ # Aplicación de la API RESTful (Puerto 5000) 
                │ 
                ├─ app.py # Lógica de Endpoints y conexión a la BD 
                │ 
                ├─ db.py
                │ 
                ├─ requirments.txt # Dependencias de Python 
                │ 
                └─ database/ # Contiene scripts SQL 
            ├─ frontend/ # Aplicación Web (Puerto 5001) 
                │ 
                ├─ app.py # Lógica de rutas que renderizan HTML y consumen la API 
                │ 
                ├─ static/ # CSS, JS, imágenes 
                │ 
                └─ templates/ # Archivos HTML (index.html, productos.html, about.html, contact.html, etc.) 
                    └─ .gitignore

---

## 🚀 3. Guía de Instalación y Ejecución

Para ejecutar la aplicación localmente, se deben iniciar el Backend (API) y el Frontend (Web) simultáneamente en dos terminales separadas.

### A. Configuración Inicial (Solo una vez)

1.  **Clonar el Repositorio:**
    ```bash
    git clone [https://github.com/agarciav12/TP_FINAL_IDS.git](https://github.com/agarciav12/TP_FINAL_IDS.git)
    cd TP_FINAL_IDS
    ```
2.  **Crear y Activar el Entorno Virtual:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
3.  **Instalar Dependencias:** (Usando el nombre de archivo provisto)
    ```bash
    pip install -r backend/requirments.txt
    ```
4.  **Configurar Base de Datos MySQL:**
    Se requiere tener un servidor MySQL corriendo. Utilizar el script de la carpeta `database/` para crear la base de datos y cargar los datos iniciales[cite: 28].
    *(El script de creación/carga se encuentra en `setup_database.sh`)*

### B. Ejecución

1.  **Terminal 1: Iniciar el Backend (API)**
    ```bash
    (venv) python backend/app.py
    ```
    *API disponible en: `http://127.0.0.1:5000/`*

2.  **Terminal 2: Iniciar el Frontend (Web)**
    ```bash
    (venv) python frontend/app.py
    ```
    *Aplicación Web disponible en: `http://127.0.0.1:5001/`*

---

## 4. 🔗 Endpoints Clave del Backend (API)

| Método | Endpoint | Descripción | Requisito |
| :--- | :--- | :--- | :--- |
| **GET** | `/api/productos` | Obtiene el catálogo completo (o filtrado)[cite: 30]. | Mostrar catálogo [cite: 29] |
| **GET** | `/api/productos/<id>` | Obtiene el detalle de un solo producto[cite: 30]. | Detalle de Producto [cite: 29] |
| **POST** | `/api/carrito` | Agrega un producto al carrito[cite: 30]. | Funcionalidad Carrito |
| **GET** | `/api/carrito/<uid>` | Obtiene el contenido del carrito de un usuario[cite: 30]. | Mostrar Carrito [cite: 29] |

---

## 5. 🧑‍💻 Metodología y Contribución

* Se utilizó **GitHub** para la gestión del código[cite: 23].
* Las tareas se gestionaron con un tablero **Kanban** (GitHub Project)[cite: 24].
* Todos los integrantes del equipo realizaron *commits* útiles asociados a tareas[cite: 26, 27].
* Se buscaron **buenas prácticas de programación** a lo largo del desarrollo[cite: 72].