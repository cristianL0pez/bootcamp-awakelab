CREATE DATABASE capacitaciones;
use capacitaciones;
CREATE TABLE operadores(RUN INT AUTO_INCREMENT PRIMARY KEY,nombre VARCHAR(50) NOT NULL,apellido VARCHAR(50) NOT NULL,direccion VARCHAR(50) NOT NULL,correo VARCHAR(25) NOT NULL) ENGINE=INNODB;

CREATE TABLE usuarios(idcoder INT AUTO_INCREMENT PRIMARY KEY,nombre VARCHAR(50) NOT NULL,apellido VARCHAR(50) NOT NULL,correo VARCHAR(25) NOT NULL,telefono VARCHAR(12)) ENGINE=INNODB;

CREATE TABLE capacitacion(cod_cusro INT AUTO_INCREMENT PRIMARY KEY, nombre  VARCHAR(50), horario DATETIME) ENGINE=INNODB;



INSERT INTO capacitacion(nombre, horario) VALUES ('Curso de PHP', '2020-05-20'), ('Curso de Java', '2020-05-20'), ('Curso de Python', '2020-05-20'), ('Curso de C#', '2020-05-20'), ('Curso de Javascript', '2020-05-20'), ('Curso de Angular', '2020-05-20'),  ('Curso de React', '2020-05-20'), ('Curso de Node', '2020-05-20'), ('Curso de MySQL', '2020-05-20'), ('Curso de MongoDB', '2020-05-20'), ('Curso de PostgreSQL', '2020-05-20'), ('Curso de Oracle', '2020-05-20'), ('Curso de SQL', '2020-05-20');
                                                   

INSERT  INTO operadores(nombre, apellido, direccion, correo) VALUES ('Juan','Perez','Calle falsa 123','Juan@Perez.com'), ('carlos','lopez','Calle falsa 123','carlos@lopez.cl'), ('jose','gonzalez','Calle falsa 123','jose@gonzalez.cl'), ('maria','perez','Calle falsa 123','maria@perez.cl'), ('juan','nieto','Calle falsa 123','juan@nieto.cl'), ('pedro','martinez','Calle falsa 123','pedro@martinez.cl'), ('alejandro','ramirez','Calle falsa 123','alejandro@ramirez'), ('daniel','lopez','Calle falsa 123','daniel@lopez'),('jose','martinez','Calle falsa 123','jose@martinez');

INSERT INTO usuarios(nombre, apellido, correo, telefono) VALUES ('Juan','Perez','Juan@Perez.cl',"999999999"),('Juan1','Perez','Juan1@Perez.cl',"999999999"),('Juan2','Perez','Juan2@Perez.cl',"999999999"),('Juan3','Perez','Juan3@Perez.cl',"999999999"),('Juan4','Perez','Juan4@Perez.cl',"999999999"),('Juan5','Perez','Juan5@Perez.cl',"999999999"),('Juan6','Perez','Juan6@Perez.cl',"999999999"),('Juan7','Perez','Juan7@Perez.cl',"999999999"),('Juan8','Perez','Juan8@Perez.cl',"999999999"),('Juan9','Perez','Juan9@Perez.cl',"999999999"),('Juan10','Perez','Juan10@Perez.cl',"999999999");






