
--link del diagrama de base de datos
--https://lucid.app/lucidchart/e981766a-1115-4b62-9ead-a8f136b6d453/edit?invitationId=inv_9525b2d5-baf7-4f62-8537-75ef82517261

CREATE DATABASE sprint_db;

--CREAR USUARIO
CREATE USER 'sprint_user'@'localhost' IDENTIFIED BY 'sprint_user';

--darle permisos a usuario
GRANT ALL PRIVILEGES ON sprint_db.* TO 'sprint_user'@'localhost';
use sprint_db;

/* Cada proveedor debe
informarnos el nombre del representante legal, su nombre corporativo, al menos dos teléfonos de
contacto (y el nombre de quien recibe las llamadas), la categoría de sus productos (solo nos pueden
indicar una categoría) y un correo electrónico para enviar la factura. Sabemos que la mayoría de los
proveedores son de productos electrónicos. Agregue 5 proveedores a la base de datos. En general, los
proveedores venden muchos productos.
 */
--crear tabla proveedores
CREATE TABLE proveedores (
  id INT NOT NULL AUTO_INCREMENT,
  nombre_representante VARCHAR(255) NOT NULL,
  nombre_corporativo VARCHAR(255) NOT NULL,
  telefono_representante VARCHAR(255) NOT NULL,
  telefono_corporativo VARCHAR(255) NOT NULL,
  categoria VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL,
  PRIMARY KEY (id)
);
--crear 5 proveedores
INSERT INTO proveedores (nombre_representante, nombre_corporativo, telefono_representante, telefono_corporativo, categoria, email) VALUES
('Juan', 'Juan', '123456789', '123456789', 'Electronico', 'juan@mail.com'),
('Pedro', 'Pedro', '123456789', '123456789', 'Electronico', 'pedro@mail.com'),
('Maria', 'Maria', '123456789', '123456789', 'Electronico', 'maria@mailcom'),
('Juan', 'Juan', '123456789', '123456789', 'Electronico', 'juan@mail.com'),
('Pedro', 'Pedro', '123456789', '123456789', 'Electronico', 'pedro@mail.com');

--TeLoVendo tiene actualmente muchos clientes, pero nos piden que ingresemos solo 5 para probar lanueva base de datos. Cada cliente tiene un nombre, apellido, dirección (solo pueden ingresar una).
--crear tabla clientes
CREATE TABLE clientes (
  id INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(255) NOT NULL,
  apellido VARCHAR(255) NOT NULL,
  direccion VARCHAR(255) NOT NULL,
  PRIMARY KEY (id)
);
--crear 5 clientes
INSERT INTO clientes (nombre, apellido, direccion) VALUES
('Juan', 'Juan', 'Calle falsa 123'),
('Pedro', 'Pedro', 'Calle falsa 123'),
('Maria', 'Maria', 'Calle falsa 123'),
('Juan', 'Juan', 'Calle falsa 123'),
('Pedro', 'Pedro', 'Calle falsa 123');

--TeLoVendo tiene diferentes productos. Ingrese 10 productos y su respectivo stock. Cada producto tiene información sobre su precio, su categoría, proveedor y color. Los productos pueden tener muchos proveedores.
--crear tabla productos
CREATE TABLE productos (
  id INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(255) NOT NULL,
  precio DECIMAL(10,2) NOT NULL,
  stock INT NOT NULL,
  categoria VARCHAR(255) NOT NULL,
  proveedor INT NOT NULL,
  color VARCHAR(255) NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (proveedor) REFERENCES proveedores(id)
); 
--crear 10 productos
INSERT INTO productos (nombre, precio, stock, categoria, proveedor, color) VALUES
('Monitor', '90', '10', 'Electronico', '1', 'negro'),
('Monitor', '100', '10', 'Electronico', '3', 'negro'),
('Monitor', '100', '10', 'Electronico', '3', 'negro'),
('Monitor', '100', '10', 'Electronico', '2', 'negro'),
('Monitor', '100', '10', 'Electronico', '2', 'negro'),
('Monitor', '100', '10', 'Electronico', '1', 'negro'),
('Monitor', '100', '10', 'Electronico', '5', 'negro'),
('zapato', '100', '10', 'zapateria', '1', 'negro'),
('Monitor', '100', '10', 'Electronico', '3', 'negro'),
('Monitor', '100', '10', 'Electronico', '1', 'negro'),



CREATE TABLE productos_proveedores (
  id INT NOT NULL AUTO_INCREMENT,
  producto INT NOT NULL,
  proveedor INT NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (producto) REFERENCES productos(id),
  FOREIGN KEY (proveedor) REFERENCES proveedores(id)
);

--mostrar la categoria masrepetida
SELECT categoria, COUNT(*) AS cantidad FROM productos GROUP BY categoria ORDER BY cantidad DESC LIMIT 1;


--Cuáles son los productos con mayor stock
SELECT nombre, stock FROM productos ORDER BY stock DESC LIMIT 5;

--Qué color de producto es más común en nuestra tienda
SELECT color, COUNT(*) AS cantidad FROM productos GROUP BY color ORDER BY cantidad DESC LIMIT 1;

--Cual o cuales son los proveedores con menor stock de productos.
SELECT nombre_corporativo, stock FROM productos GROUP BY proveedor ORDER BY stock ASC LIMIT 1; 


--Cambien la categoría de productos más popular por ‘Electrónica y computación’
UPDATE productos SET categoria = 'Electronico y computacion' WHERE categoria = 'Electronico';