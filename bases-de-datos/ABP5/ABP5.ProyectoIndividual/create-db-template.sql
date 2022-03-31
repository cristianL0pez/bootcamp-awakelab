CREATE DATABASE bootcamp_cristian;

use bootcamp_cristian;
SET TIME_ZONE='-03:00';

--crear usuario con todos los permisos
CREATE USER 'cristian'@'localhost' IDENTIFIED BY '1234';
GRANT ALL PRIVILEGES ON *.* TO 'cristian'@'localhost';
--crear tabla con n (id_usuario, nombre, apellido, contraseña,zona horaria (por defecto UTC-3), género y teléfono de contacto)
CREATE TABLE usuarios (
  id_usuario INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(255),
  apellido VARCHAR(255),
  contraseña VARCHAR(255),
  zona_horaria VARCHAR(32),
  genero VARCHAR(255),
  telefono VARCHAR(255),
  PRIMARY KEY (id_usuario)
);

--tabla almacena información relacionada a la fecha-hora de ingreso de los usuarios ala plataforma (id_ingreso, id_usuario y la fecha-hora de ingreso (por defecto la fecha-hora actual))
CREATE TABLE ingresos_usuarios (
  id_ingreso INT NOT NULL AUTO_INCREMENT,
  id_usuario INT NOT NULL,
  fecha_hora_ingreso DATETIME DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id_ingreso),
  FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
);

--tabla almacena información sobre la cantidad de veces que los usuarios han visitado la aplicación
CREATE TABLE visitas_usuarios (
  id_visita INT NOT NULL AUTO_INCREMENT,
  id_usuario INT NOT NULL,
  cantidad_visitas INT NOT NULL,
  PRIMARY KEY (id_visita),
  FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
);

--crear 8 registros para tabla usuarios     
INSERT INTO usuarios (nombre, apellido, contraseña, zona_horaria, genero, telefono) VALUES
('Cristian', 'Gonzalez', '1234', @@SESSION.time_zone, 'Masculino', '12345678'),
('Juanito', 'Perez', '1234', @@SESSION.time_zone, 'Masculino', '12345678'),
('Maria', 'Gonzalez', '1234', @@SESSION.time_zone, 'Femenino', '12345678'),
('Juana', 'Perez', '1234', @@SESSION.time_zone, 'Femenino', '12345678'),
('Pedro', 'Gonzalez', '1234', @@SESSION.time_zone, 'Masculino', '12345678'),
('Juan', 'Perez', '1234', @@SESSION.time_zone, 'Masculino', '12345678'),
('Mariana', 'Gonzalez', '1234', @@SESSION.time_zone, 'Femenino', '12345678'),
('Juanita', 'Perez', '1234', @@SESSION.time_zone, 'Femenino', '12345678');


--crear 8 registros para tabla ingresos_usuarios
INSERT INTO ingresos_usuarios (id_usuario) VALUES
(1),
(2),
(3),
(4),
(5),
(6),
(7),
(8);


--crear 8 registros para tabla visitas_usuarios
INSERT INTO visitas_usuarios (id_usuario, cantidad_visitas) VALUES
(1, 1),
(2, 1),
(3, 1),
(4, 1),
(5, 1),
(6, 1),
(7, 1),
(8, 1);




