--link teorico
--https://docs.google.com/document/d/1YPstsep8HOEnF2jlAD7EjCj6XnxPP1pKCkhjTAbeF_Y/edit?usp=sharing
CREATE TABLE Vendedores(RUN INT,nombre VARCHAR(50) NOT NULL,apellidos VARCHAR(50) NOT NULL,fecha_nacimiento date NOT NULL,seccion VARCHAR(50) NOT NULL ) ENGINE=INNODB;

CREATE TABLE Productos(SKU INT,nombre VARCHAR(50) NOT NULL,categoria VARCHAR(50) NOT NULL,fabricante VARCHAR(30) NOT NULL,stock INT NOT NULL) ENGINE=INNODB;

CREATE TABLE Clientes(clienteId INT AUTO_INCREMENT PRIMARY KEY,nombre VARCHAR(50) NOT NULL,apellido VARCHAR(50) NOT NULL,telefono VARCHAR(12) NOT NULL,correo VARCHAR(25) NOT NULL,fecha_registro date NOT NULL) ENGINE=INNODB;


ALTER TABLE Productos ADD precio int not null after categoria;


ALTER TABLE Productos ADD precio int not null after categoria;

ALTER TABLE Clientes ADD total_pagado int not null after fecha_registro;



INSERT INTO Productos(SKU,nombre,categoria,precio,fabricante,stock) VALUES(1234,'clavo','ferreteria',7,'ferre',67),(1232,'martillo','herramienta',13,'ferre',10),(3424,'esmeril','herramienta',22,'ferre',68),(3344,'taladro','herramienta',22,'ferre',1000),(3434,'metro','herramienta',32,'ferre',16),(7577,'lija','ferreteria',4,'ferre',10000),(5355,'desarmardor','herramienta',12,'ferre',300),(3434,'soldador','herramienta',443,'ferre',56),(4321,'mascarilla','salud',321,'ferre',74),(7658,'tornillo','ferreteria',13,'ferre',34);



INSERT INTO Vendedores(RUN,nombre,apellidos,fecha_nacimiento,seccion,salrario) VALUES(12346789,'carlos','nieto','2013-07-04','ferreteria',6734),(12321232,'sergio','mendez','2014-06-01','ferreteria',1034),(34241232,'ruben','castro','2015-06-01','calzado',6834),(33441232,'francisco','ugarte','2016-05-01','calzado',1000),(34341232,'sandra','opazo','2017-04-01','moda',16343),(75775355,'marcela','echeverria','2018-01-01','moda',10000),(53554321,'claudio','lopez','2019-01-02','cafeteria',30034),(34345355,'gabriel','perez','2020-01-01','cafeteria',5634),(43214321,'camilo','fernandez','2021-04-01','ferreteria',7434),(76585355,'goku','uchija','2021-01-03','ferreteria',3434);



INSERT INTO Clientes(nombre,apellido,telefono,correo,fecha_registro,total_pagado) VALUES('marlon','perez',0418098-69-0252,'marlon@mail.com','2013-07-04',6734),('rodrigo','mendez',59876027-18-8528,'rodrigo@mail.com','2014-06-01',1034),('anibal','castro',482716-71-9343,'anibal@mail.com','2015-06-01',6834),('francisca','ugarte',38759764-64-9839,'francisca@mail.com','2016-05-01',1000),('sandro','opazo',34365470-72-3662,'sandro@mail.com','2017-04-01',16343),('marcelo','echeverria',8705513-50-6530,'marcelo@mail.com','2018-01-01',10000),('claudia','pinochet',8344142-48-8002,'claudian@mail.com','2019-01-02',30034),('gabriela','perez',859445054-59-5979,'gabriela@mail.com','2020-01-01',5634),('camila','de las mercedes',1866217-16-6856,'camila@mail.com','2021-04-01',7434),('vegeta','peron',1538776-88-9764,'vegeta@mail.com','2013-07-04',3434);
