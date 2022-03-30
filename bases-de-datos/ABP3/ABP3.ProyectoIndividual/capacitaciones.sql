--usar capacitacion
USE capacitaciones;

--incluir salario operador
ALTER TABLE operadores ADD COLUMN salario INT;

--Inserte 3 cursos nuevos
INSERT INTO capacitacion(nombre, horario,costo,fecha_realizacion) VALUES ('Curso de css', '2020-05-20', 96 ,'2020-05-20 '), ('Curso de laravel', '2020-05-20', 96 ,'2020-05-20'), ('Curso de hacking', '2020-05-20', 96 ,'2020-05-20');

--Inserte 3 profesores nuevos
INSERT  INTO operadores(nombre, apellido, direccion, correo,fecha_creacion) VALUES ('esteban','carmona','Calle falsa 123','esteban@carmona.com','2020-05-20'), ('eusebio','lillo','Calle falsa 123','eusebio@lillo.cl','2020-05-20'), ('jorge','gonzalez','Calle falsa 123','jorge@gomzalez.cl','2020-05-20');

-- curso más costoso
SELECT * FROM capacitacion WHERE costo = (SELECT MAX(costo) FROM capacitacion);

 --profesor menos con menor salario
SELECT * FROM operadores WHERE salario = (SELECT MIN(salario) FROM operadores);

--curso más costoso avg
SELECT * FROM capacitacion WHERE costo > (SELECT AVG(costo) FROM capacitacion);

--Cree una tabla Cursos económicos con las capacitaciones con costo menor al avg
CREATE TABLE cursos_economicos(
    id INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(50),
    horario VARCHAR(50),
    costo INT ,
    fecha_realizacion DATE,
    PRIMARY KEY (id)
);

INSERT INTO cursos_economicos(nombre, horario,costo,fecha_realizacion) SELECT nombre, horario,costo,fecha_realizacion FROM capacitacion WHERE costo < (SELECT AVG(costo) FROM capacitacion);

--A la tabla Cursos económicos, agrégale dos campos. ‘Cantidad mínima estudiantes’ y ‘Aportes públicos’
ALTER TABLE cursos_economicos ADD COLUMN cantidad_minima_estudiantes INT;
ALTER TABLE cursos_economicos ADD COLUMN aportes_publicos INT;

--Renombre la columna “Costo realización”
ALTER TABLE cursos_economicos CHANGE COLUMN costo costo_efectivo INT;

--Costo efectivo. En dicha columna, a cada valor se le debe restar el valor de ‘Aportes públicos’
UPDATE cursos_economicos SET costo_efectivo = costo_efectivo - aportes_publicos;

--actualiza 3 operadores
UPDATE operadores SET salario = salario + (SELECT AVG(costo_efectivo) FROM cursos_economicos);

--actualize 5 capacitaciones
UPDATE capacitacion SET costo = costo + (SELECT AVG(costo_efectivo) FROM cursos_economicos);




























