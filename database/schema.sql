CREATE table productos (id INTEGER AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(50), 
precio DECIMAL(10, 2), stock INTEGER );

CREATE table usuarios (id INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(100),
email VARCHAR(100) UNIQUE NOT NULL, password VARCHAR(255) NOT NULL);

CREATE table carrito (usuario_id INT, producto_id INT, cantidad INT, 
PRIMARY KEY (usuario_id, producto_id), FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
FOREIGN KEY (producto_id) REFERENCES productos(id))

CREATE table compras(
	id INT AUTO_INCREMENT PRIMARY KEY,
	usuario_id INT NOT NULL,
	fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
	total DECIMAL(10, 2),
	FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);

CREATE table items_compra(
	id INT AUTO_INCREMENT PRIMARY KEY,
	compra_id INT NOT NULL,
	producto_id INT NOT NULL,
	precio_unitario DECIMAL(10, 2),
	cantidad INT,
	subtotal DECIMAL(10,2),
	FOREIGN KEY (producto_id) REFERENCES productos(id),
	FOREIGN KEY (compra_id) REFERENCES compras(id)
);