USE telovendo;

--Ingrese 5 clientes nuevos
INSERT INTO Clientes(nombre,apellido,telefono,correo,fecha_registro,total_pagado)
VALUES('camilo','fuentes',0418098-69-0252,'camilo@mail.com',100,67334),
('marcelo','mendez',59876028,'marcelo@mail.com','2014-06-01',10334),
('santiago','perez',09987659222,'santiago@mail.com',100,6734),
('renata','perez',0998222,'renata@mail.com',100,323545),
('juan','lopez',0343433998222,'juan@mail.com',100,674);

--ingrese 5 vendedores nuevos
INSERT INTO Vendedores(RUN,nombre,apellidos,fecha_nacimiento,seccion,salrario)
VALUES(2132133123,'camilo','fuentes','2014-06-01','zapateria',6334),
(2132223,'marcelo','lagos','2014-06-01','zapateria',1034),
(2167723,'santiagito','perez','2014-06-01','zapateria',6734),
(2771323,'renato','perez','2014-06-01','zapateria',3245),
(7777323,'juanito','lopez','2014-06-01','zapateria',674);

--ingrese 5 productos nuevos
INSERT INTO Productos(nombre,categoria,precio,fabricante,stock)
VALUES('arroz','categoria1',2.500,'arroz de la casa',100),
('carne','categoria2',2.000,'arroz de la casa',100),
('fideos','categoria1',3.500,'arroz de la casa',100),
('macarrones','categoria1',4.500,'arroz de la casa',100),
('queso','categoria2',1.500,'arroz de la casa',100);

--Identifique cual es el salrario mínimo entre vendedores. 
SELECT MIN(salrario) FROM Vendedores;

--Identifique cual es el salario máximo entre vendedores.
SELECT MAX(salrario) FROM Vendedores;

--Súmele el salario mínimo identificado al salario de todos los vendedores. 
UPDATE Vendedores SET salrario = salrario + MIN(salrario);

--G. Elimine el producto más caro del inventario. 
DELETE FROM Productos WHERE precio = (SELECT MAX(precio) FROM Productos);

--Cree una tabla que contenga solo los clientes que han pagado más que el promedio. 

CREATE TABLE Clientes_con_pago_mayor_promedio(
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    telefono VARCHAR(50),
    correo VARCHAR(50),
    fecha_registro VARCHAR(50),
    total_pagado VARCHAR(50)
);
--Cree una tabla que contenga solo los clientes que han pagado más que el promedio. 
INSERT INTO Clientes_con_pago_mayor_promedio(nombre,apellido,telefono,correo,fecha_registro,total_pagado) SELECT nombre,apellido,telefono,correo,fecha_registro,total_pagado FROM Clientes WHERE total_pagado > (SELECT AVG(total_pagado) FROM Clientes);

--Actualice los datos de 3 productos.
UPDATE Productos SET nombre = 'arroz con leche', categoria = 'categoria1', precio = 2.500, fabricante = 'arroz de la casa', stock = 100 WHERE nombre = 'arroz';
UPDATE Productos SET nombre = 'carne amarga', categoria = 'categoria2', precio = 2.000, fabricante = 'carne de la casa', stock = 100 WHERE nombre = 'carne';
UPDATE Productos SET nombre = 'fideos cabellos', categoria = 'categoria1', precio = 2.500, fabricante = 'fideos de la casa', stock = 100 WHERE nombre = 'fideos';


--J. Actualice los datos de tres vendedores.
UPDATE Vendedores SET RUN = 211222222, nombre = 'camilo', apellidos = 'fuentes', fecha_nacimiento = '2014-06-01', seccion = 'zapateria', salrario = 6334 WHERE RUN = 2132133123;
UPDATE Vendedores SET RUN = 212222222, nombre = 'marcelo', apellidos = 'lagos', fecha_nacimiento = '2014-06-01', seccion = 'zapateria', salrario = 1034 WHERE RUN = 2132223;
UPDATE Vendedores SET RUN = 212222233, nombre = 'santiagito', apellidos = 'perez', fecha_nacimiento = '2014-06-01', seccion = 'zapateria', salrario = 6734 WHERE RUN = 2167723;

--Actualice los datos de cliente
UPDATE Clientes SET nombre = 'camilo', apellido = 'fuentes', telefono = 0418098, direccion = 'calle falsa 123',comuna = 'santiago', correo = 'camilo@mail.com', fecha_registro = '2014-06-01', total_pagado = 67334 WHERE nombre = 'camilo';
UPDATE Clientes SET nombre = 'marcelo', apellido = 'mendez', telefono = 999999999, direccion = 'calle falsa 123',comuna = 'santiago', correo = 'marcelo@mail.com' , fecha_registro = '2014-06-01', total_pagado = 10334 WHERE nombre = 'marcelo';
UPDATE Clientes SET nombre = 'santiago', apellido = 'perez', telefono = 888888888, direccion = 'calle falsa 123',comuna = 'santiago', correo = 'santiago@mail.com' , fecha_registro = '2014-06-01', total_pagado = 6734 WHERE nombre = 'santiago'; 


--Seleccione el nombre y el apellido de los vendedores que tienen un salario superior al promedio. 
SELECT nombre,apellido FROM Vendedores WHERE salrario > (SELECT AVG(salrario) FROM Vendedores);

--Indique cuál es el cliente con mayor gasto.
SELECT nombre,apellido,total_pagado FROM Clientes WHERE total_pagado = (SELECT MAX(total_pagado) FROM Clientes);











