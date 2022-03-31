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
    PRIMARY KEY (id_usuario)
);

--tabla almacena información relacionada a la fecha-hora de ingreso de los usuarios a la plataforma (id_ingreso, id_usuario y la fecha-hora de ingreso (por defecto la fecha-hora actual)).
CREATE TABLE ingreso (
    id_ingreso INT NOT NULL AUTO_INCREMENT,
    id_usuario INT NOT NULL,
    fecha_hora_ingreso DATETIME NOT NULL,
    PRIMARY KEY (id_ingreso),
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
);

alter table ingreso CHANGE fecha_hora_ingreso fecha_hora_ingreso VARCHAR(50);


INSERT INTO usuarios (id_usuario, nombre, apellido, contraseña, zona_horaria, genero, telefono) VALUES
(101, 'Juan', 'Perez', '1234', @@SESSION.time_zone, 'Masculino', '123456789'),
(102, 'Maria', 'Gonzalez', '1234', @@SESSION.time_zone, 'Femenino', '123456789'),
(103, 'Pedro', 'Lopez', '1234', @@SESSION.time_zone, 'Masculino', '123456789'),
(104, 'Ana', 'Gonzalez', '1234', @@SESSION.time_zone, 'Femenino', '123456789'),
(105, 'Juan', 'Perez', '1234', @@SESSION.time_zone, 'Masculino', '123456789'),
(106, 'Maria', 'Gonzalez', '1234', @@SESSION.time_zone, 'Femenino', '123456789'),
(107, 'Pedro', 'Lopez', '1234', @@SESSION.time_zone, 'Masculino', '123456789'),
(108, 'Ana', 'Gonzalez', '1234', @@SESSION.time_zone, 'Femenino', '123456789');


INSERT INTO ingreso (id_ingreso, id_usuario,fecha_hora_ingreso) VALUES
(101, 101, NOW()),
(102, 102, NOW()),
(103, 103, NOW()),
(104, 104, NOW()),
(105, 105, NOW()),
(106, 106, NOW()),
(107, 107, NOW()),
(108, 108, NOW());




--Contactos (id_contacto, id_usuario, numero de telefono,correo electronico) y Modifique la columna teléfono de contacto, para crear un vínculo entre la tabla Usuarios y la tabla Contactos.
CREATE TABLE contactos (
    id_contacto INT AUTO_INCREMENT,
    id_usuario INT ,
    telefono VARCHAR(50),
    correo VARCHAR(50) DEFAULT 'correo@mail.com',
    PRIMARY KEY (id_contacto),
    CONSTRAINT fk_contacto_usuario  FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
);


--crear 8 registros para tabla contactos 
INSERT INTO contactos(id_contacto, id_usuario, telefono,correo) VALUES
(101, 101, '123456789','correo@mail.com'),
(102, 102, '123456789','correo@mail.com'),
(103, 103, '123456789','correo@mail.com'),
(104, 104, '123456789','correo@mail.com'),
(105, 105, '123456789','correo@mail.com'),
(106, 106, '123456789','correo@mail.com'),
(107, 107, '123456789','correo@mail.com'),
(108, 108, '123456789','correo@mail.com');

