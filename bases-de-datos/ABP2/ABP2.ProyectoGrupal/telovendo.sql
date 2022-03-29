
use telovendo;

SELECT * FROM `Productos` WHERE precio > (SELECT AVG(precio) FROM `Productos`);
SELECT * FROM `Vendedores` WHERE salrario > (SELECT AVG(salrario) FROM `Vendedores`);

SELECT * FROM `Clientes` WHERE total_pagado > (SELECT AVG(total_pagado) FROM `Clientes`);

SELECT * FROM `Vendedores` WHERE salrario< (SELECT AVG(salrario)from `Vendedores`);

SELECT * FROM `Productos` WHERE precio < (SELECT AVG(precio) from `Productos`);

SELECT nombre, apellidos FROM `Vendedores` WHERE salrario > (SELECT AVG(salrario)from `Vendedores`); 

SELECT nombre,precio FROM `Productos` WHERE precio = (SELECT MIN(precio) FROM `Productos`);
SELECT nombre,precio FROM `Productos` WHERE precio = (SELECT MAX(precio) FROM `Productos`);
                                           
SELECT SUM(precio) FROM  `Productos`;

SELECT nombre, precio from `Productos` WHERE stock > 1;

--comuna com mas clientes   
SELECT nombre, precio from `Productos` WHERE stock = (SELECT MIN(stock) FROM `Productos`);


