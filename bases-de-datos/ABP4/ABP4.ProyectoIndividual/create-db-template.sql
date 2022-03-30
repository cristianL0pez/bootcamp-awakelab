--link de las preguntas
--https://docs.google.com/document/d/1dzzgdqRS-RSvPCW60WG5VlztKAH1K3e8AmaghZgEC4U/edit?usp=sharing
CREATE DATABASE Control_usuarios
    DEFAULT CHARACTER SET = 'utf8mb4';
use Control_usuarios;
--SHOW VARIABLES LIKE '%innodb%'; ver si innodb esta activado
--crear usuario con todos los privilegios
CREATE USER 'cristianadmin'@'localhost' IDENTIFIED BY '1234';

GRANT ALL PRIVILEGES ON Control_usuarios.* TO 'cristianadmin'@'localhost';
--Crea dos tablas en la base de datos. La primera almacena todos los usuarios sin una participación




--Crea dos tablas en la base de datos
--La primera almacena todos los usuarios sin una participación
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT,
    nombre VARCHAR(255),
    apellido VARCHAR(255),
    email VARCHAR(255),
    telefono VARCHAR(255),
    genero VARCHAR(255) ,
    PRIMARY KEY (id)
);

--tabla de usuarios que son considerados especiales
CREATE TABLE usuarios_especiales (
    id INT AUTO_INCREMENT,
    nombre VARCHAR(255),
    apellido VARCHAR(255),
    email VARCHAR(255),
    telefono VARCHAR(255),
    genero VARCHAR(255) ,
    PRIMARY KEY (id)
);

--La primera tabla debe tener 5 usuarios en un comienzo de la aplicación
INSERT INTO usuarios (nombre, apellido, email, telefono, genero) 
VALUES ('Juan', 'Perez', 'juan@mail.com', '123456789', 'Masculino'),
('Maria', 'Gonzalez', 'maria@mail.com', '123456789', 'Femenino'),
('Pedro', 'Gonzalez', 'pedro@mail.com', '123456789', 'Masculino'),
('Ana', 'Gonzalez', 'ana@mail.com', '123456789', 'Femenino'),
('Juan', 'Gonzalez', 'juan@mail.com', '123456789', 'Masculino');


--- Transfiera tres usuarios desde la tabla usuarios  a la tabla usuarios_especiales
START TRANSACTION;

SELECT @@autocommit;
set autocommit=0;

INSERT INTO usuarios_especiales(id,nombre, apellido, email, telefono, genero)
SELECT * 
FROM usuarios WHERE genero = 'Masculino';
DELETE FROM usuarios_especiales WHERE id = (SELECT MAX(id) FROM usuarios_especiales);

ROLLBACK;


COMMIT;

--cambio de primary key a int nos incremental
ALTER TABLE usuarios_especiales MODIFY id INT;
ALTER TABLE usuarios MODIFY id INT;


















