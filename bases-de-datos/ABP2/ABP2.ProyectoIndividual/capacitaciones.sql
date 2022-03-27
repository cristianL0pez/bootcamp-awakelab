--se usa la base de datos capacitaciones anteriormente creada
USE capacitaciones;
ALTER TABLE capacitacion ADD costo INT not null after horario;

ALTER TABLE capacitacion ADD fecha_realizacion DATE after costo;


ALTER TABLE operadores ADD fecha_creacion DATE after correo;

ALTER table usuarios add fecha_creacion DATE after telefono;

--costo de realizacion de capacitaciones
SELECT costo FROM capacitacion;
--suma los costos de las capacitaciones
SELECT SUM(costo) FROM capacitacion;
--Muestre los 5 operadores más recientemente registrados.
SELECT * FROM operadores ORDER BY fecha_creacion DESC LIMIT 5;
--Muestre los 5 usuarios más recientemente registrados
SELECT * FROM usuarios ORDER BY fecha_creacion DESC LIMIT 5;
--Calcule cuántos días han transcurrido desde que se registró a operadores y clientes. Indague en la función DATEDIFF() de MySQL.
SELECT AVG(DATEDIFF(fecha_creacion,NOW())) FROM operadores;

--Calcule cuántos días transcurrieron desde que se realizó el último curso de capacitación.
SELECT AVG(DATEDIFF(fecha_realizacion,NOW())) FROM capacitacion;

--, indique cuál fue el curso de capacitación más costoso y el menos costoso.
SELECT MAX(costo) FROM capacitacion;
SELECT MIN(costo) FROM capacitacion;