-- Insertar usuarios de ejemplo
INSERT INTO usuarios (nombre, email, password) VALUES
<<<<<<< HEAD
('Juan Perez', 'juan@example.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5GyYIeWIgNW2m'), -- password: demo123
('María García', 'maria@example.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5GyYIeWIgNW2m'),
('Carlos Lopez', 'carlos@example.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5GyYIeWIgNW2m');

-- Insertar productos de ejemplo
INSERT INTO productos (nombre, categoria, precio, stock) VALUES
-- Electronica
('Laptop Dell XPS 13', 'Equipos', 1299.99, 15),
('iPhone 14 Pro', 'Electronica', 999.99, 25),
('Samsung Galaxy S23', 'Electronica', 849.99, 20),
('iPad Air', 'Electronica', 599.99, 30),
('AirPods Pro', 'Electronica', 249.99, 50),
('Monitor LG 27"', 'Monitores', 349.99, 12),
('Teclado Mecanico Logitech', 'Teclados', 129.99, 40),
('Mouse Gamer Razer', 'Mouse', 79.99, 35),
('Teclado Mecánico Redragon Kumara K552', 'Teclados', 45.00, 30),
('Teclado HyperX Alloy Origins', 'Teclados', 119.99, 15),
('Mouse Logitech G502 HERO', 'Mouse', 49.99, 25),
('Mouse Razer DeathAdder V2', 'Mouse', 59.99, 20),
('Mouse Redragon Cobra M711', 'Mouse', 28.00, 35),
('Auriculares HyperX Cloud II', 'Headset', 89.99, 18),
('Auriculares Razer Kraken Tournament', 'Headset', 79.99, 22),
('Auriculares Logitech G733 Lightspeed', 'Headset', 149.99, 10),
('Auriculares Redragon H350 Pandora RGB', 'Headset', 39.99, 28),
('Mousepad SteelSeries QcK Large', 'Extras', 19.99, 40),
('Mousepad Razer Goliathus Extended', 'Extras', 29.99, 25),
('Mousepad HyperX Fury S Speed XL', 'Extras', 24.99, 30),
('Micrófono HyperX QuadCast', 'Extras', 139.99, 12),
('Micrófono Fifine K690', 'Extras', 64.99, 18),
('Volante Logitech G29 Driving Force', 'Extras', 299.99, 6),
('Control Xbox Series Wireless', 'Joysticks', 59.99, 20),
('Soporte Auriculares RGB Newskill', 'Extras', 34.99, 22),
('Base Refrigerante KLIM Ultimate RGB', 'Extras', 49.99, 15),
('Barra de Sonido Redragon Waltz GS550', 'Extras', 32.99, 30),
('Parlantes Logitech G560 Lightsync', 'Extras', 199.99, 8);


-- Insertar algunos items en el carrito de ejemplo
INSERT INTO carrito (usuario_id, producto_id, cantidad) VALUES
(1, 1, 1),  
(1, 5, 2),  
(2, 9, 3),  
(2, 15, 1), 
(3, 21, 1); 

-- Insertar una compra de ejemplo
INSERT INTO compras (usuario_id, total) VALUES
(1, 349.99);

-- Insertar items de la compra
INSERT INTO items_compra (compra_id, producto_id, precio_unitario, cantidad, subtotal) VALUES
(1, 2, 999.99, 1, 999.99),
(1, 7, 129.99, 2, 259.98);
=======
('Juan P�rez', 'juan@example.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5GyYIeWIgNW2m'), 
('Mar�a Garc�a', 'maria@example.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5GyYIeWIgNW2m'),
('Carlos L�pez', 'carlos@example.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5GyYIeWIgNW2m');


INSERT INTO productos (nombre, categoria, precio, stock, imagen) VALUES
('Teclado Mecánico Logitech', 'Teclados', 129.99, 40, 'teclado_logitech_mecanico.jpg'),
('Mouse Gamer Razer', 'Mouse', 79.99, 35, 'mouse_razer.jpg'),
('Teclado Mecánico Redragon Kumara K552', 'Teclados', 45.00, 30, 'redragon_k552.jpg'),
('Teclado HyperX Alloy Origins', 'Teclados', 119.99, 15, 'hyperx_alloy_origins.jpg'),
('Mouse Logitech G502 HERO', 'Mouse', 49.99, 25, 'logitech_g502_hero.jpg'),
('Mouse Razer DeathAdder V2', 'Mouse', 59.99, 20, 'razer_deathadder_v2.jpg'),
('Mouse Redragon Cobra M711', 'Mouse', 28.00, 35, 'redragon_m711.jpg'),
('Auriculares HyperX Cloud II', 'Headset', 89.99, 18, 'hyperx_cloud_ii.jpg'),
('Auriculares Razer Kraken Tournament', 'Headset', 79.99, 22, 'razer_kraken_tournament.jpg'),
('Auriculares Logitech G733 Lightspeed', 'Headset', 149.99, 10, 'logitech_g733.jpg'),
('Auriculares SteelSeries Arctis 7', 'Headset', 129.99, 12, 'steelseries_arctis7.jpg'),
('Mouse Corsair M65 RGB Elite', 'Mouse', 69.99, 18, 'corsair_m65_rgb.jpg'),
('Teclado Corsair K70 RGB MK.2', 'Teclados', 139.99, 20, 'corsair_k70_mk2.jpg'),
('NVIDIA GeForce RTX 3060', 'Placas de video', 499.99, 8, 'rtx_3060.jpg'),
('AMD Radeon RX 6600 XT', 'Placas de video', 399.99, 10, 'rx_6600_xt.jpg'),
('NVIDIA GeForce RTX 3070', 'Placas de video', 699.99, 5, 'rtx_3070.jpg'),
('Mousepad Gamer XXL', 'Extras', 29.99, 50, 'mousepad_xxl.jpg'),
('Soporte Vertical para GPU', 'Extras', 39.99, 15, 'gpu_vertical_stand.jpg'),
('Kit de Limpieza PC', 'Extras', 19.99, 30, 'kit_limpieza_pc.jpg'),
('Joystick Xbox Wireless', 'Joysticks', 59.99, 20, 'joystick_xbox_wireless.jpg'),
('Joystick PS5 DualSense', 'Joysticks', 69.99, 18, 'joystick_ps5_dualsense.jpg'),
('Joystick Logitech F310', 'Joysticks', 29.99, 25, 'joystick_logitech_f310.jpg'),
('PC Gamer Intel i5 / RTX 3060', 'Equipos', 1299.99, 5, 'pc_gamer_i5_rtx3060.jpg'),
('PC Gamer AMD Ryzen 7 / RX 6700 XT', 'Equipos', 1499.99, 3, 'pc_gamer_ryzen7_rx6700xt.jpg'),
('PC Home Office Intel i3', 'Equipos', 699.99, 8, 'pc_home_i3.jpg');

>>>>>>> ff66d95 (Actualizar proyecto final: Terminado carrito y correcciones de archivos .html)
