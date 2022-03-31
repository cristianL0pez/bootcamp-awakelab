use grupal_db;

SET TIME_ZONE='-03:00';

--crea tabla de usuario (id_usuario, nombre, apellido, contraseña,zona horaria (por defecto UTC-3), género y teléfono de contacto). 
CREATE TABLE usuarios (
    id_usuario INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    contraseña VARCHAR(50) NOT NULL,
    zona_horaria VARCHAR(50) NOT NULL,
    genero VARCHAR(50) NOT NULL,
    telefono VARCHAR(50) NOT NULL,
    correo VARCHAR(50) NOT NULL DEFAULT 'correo@mail.com',
    PRIMARY KEY (id_usuario)
);

--tabla almacena información relacionada a la fecha-hora de ingreso de los usuarios a la plataforma (id_ingreso, id_usuario y la fecha-hora de ingreso (por defecto la fecha-hora actual)).
CREATE TABLE ingreso (
    id_ingreso INT NOT NULL AUTO_INCREMENT,
    id_usuario INT NOT NULL,
    fecha_hora_ingreso VARCHAR(50) NOT NULL,
    PRIMARY KEY (id_ingreso),
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
);

INSERT INTO usuarios (id_usuario, nombre, apellido, contraseña, zona_horaria, genero, telefono,correo) VALUES
(101, 'Juan', 'Perez', '1234', @@SESSION.time_zone, 'Masculino', '123456789','correo@mail.com'),
(102, 'Maria', 'Gonzalez', '1234', @@SESSION.time_zone, 'Femenino', '123456789','correo@mail.com'),
(103, 'Pedro', 'Lopez', '1234', @@SESSION.time_zone, 'Masculino', '123456789','correo@mail.com'),
(104, 'Ana', 'Gonzalez', '1234', @@SESSION.time_zone, 'Femenino', '123456789','correo@mail.com'),
(105, 'Juan', 'Perez', '1234', @@SESSION.time_zone, 'Masculino', '123456789','correo@mail.com'),
(106, 'Maria', 'Gonzalez', '1234', @@SESSION.time_zone, 'Femenino', '123456789','correo@mail.com'),
(107, 'Pedro', 'Lopez', '1234', @@SESSION.time_zone, 'Masculino', '123456789','correo@mail.com'),
(108, 'Ana', 'Gonzalez', '1234', @@SESSION.time_zone, 'Femenino', '123456789','correo@mail.com');

INSERT INTO usuarios (id_usuario, nombre, apellido, contraseña, zona_horaria, genero, telefono,correo) VALUES
(109, 'Juan', 'lopez', '1234', @@SESSION.time_zone, 'Masculino', '123456789','correo@mail.com');

INSERT INTO usuarios (id_usuario, nombre, apellido, contraseña, zona_horaria, genero, telefono,correo) VALUES
(110, 'cristian', 'lopez', '1234', @@SESSION.time_zone, 'Masculino', '123456789','correo@mail.com');


INSERT INTO ingreso (id_ingreso, id_usuario,fecha_hora_ingreso) VALUES
(101, 101, NOW()),
(102, 102, NOW()),
(103, 103, NOW()),
(104, 104, NOW()),
(105, 105, NOW()),
(106, 106, NOW()),
(107, 107, NOW()),
(108, 108, NOW());


SET TIME_ZONE='-02:00';

CREATE TABLE contactos
    as (SELECT id_usuario,telefono,correo FROM usuarios);

--actualizar los datos de clientes en contactos
INSERT INTO contactos(id_usuario,telefono,correo) 
SELECT id_usuario,telefono,correo FROM usuarios;
select current_timestamp();





