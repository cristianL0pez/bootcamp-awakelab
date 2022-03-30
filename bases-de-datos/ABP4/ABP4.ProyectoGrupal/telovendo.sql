USE telovendo;

--agregar TLV Coins a usuario ALTER
ALTER TABLE Clientes ADD COLUMN tlvcoins INT(11) UNSIGNED DEFAULT 0;

--actualizar campo saldo en TLV Coins a todos los clientes en 1000
UPDATE Clientes SET tlvcoins = 1000;
--autocommit
SELECT @@autocommit;



--transaccion 1
START TRANSACTION;
set autocommit=0;
SELECT * FROM Clientes WHERE tlvcoins >=100;
--Verificar que la clienteId=11 exista
SELECT * FROM Clientes WHERE clienteId=11;
--Verificar que la clienteId=12 exista
SELECT * FROM Clientes WHERE clienteId=12;
UPDATE Clientes SET tlvcoins = tlvcoins - 200 WHERE clienteId = 11;
UPDATE Clientes SET tlvcoins = tlvcoins + 200 WHERE clienteId = 12;
ROLLBACK;




--transaccion 2
START TRANSACTION;
set autocommit=0;
--Verificar que la clienteId=12 exista
SELECT * FROM Clientes WHERE clienteId=12;
--Verificar que la clienteId=13 exista
SELECT * FROM Clientes WHERE clienteId=13;
SELECT * FROM Clientes WHERE tlvcoins >= 1000;
UPDATE Clientes SET tlvcoins = tlvcoins - 150 WHERE clienteId = 12;
UPDATE Clientes SET tlvcoins = tlvcoins + 150 WHERE clienteId = 13;
ROLLBACK;




--transaccion 3
START TRANSACTION;
--Verificar que la clienteId=13 exista
SELECT * FROM Clientes WHERE clienteId=13;
--Verificar que la clienteId=14 exista
SELECT * FROM Clientes WHERE clienteId=14;
SELECT * FROM Clientes WHERE tlvcoins >= 1000;
UPDATE Clientes SET tlvcoins = tlvcoins - 500 WHERE clienteId = 13;
UPDATE Clientes SET tlvcoins = tlvcoins + 500 WHERE clienteId = 14;
COMMIT;



--transaccion 4
START TRANSACTION;
--Verificar que la clienteId=14 exista
SELECT * FROM Clientes WHERE clienteId=14;
--Verificar que la clienteId=11 exista
SELECT * FROM Clientes WHERE clienteId=11;

SELECT * FROM Clientes WHERE tlvcoins >= 1000;
UPDATE Clientes SET tlvcoins = tlvcoins - 500 WHERE clienteId = 14;
UPDATE Clientes SET tlvcoins = tlvcoins + 500 WHERE clienteId = 11;
COMMIT;















