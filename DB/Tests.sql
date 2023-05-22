-- CREDENCIALES DEFAULT
INSERT INTO Credencial(id,tipo) VALUES(10,"Cliente");
INSERT INTO Credencial(id,tipo) VALUES(11,"Administrador");
INSERT INTO Credencial(id,tipo) VALUES(12,"Vendedor");
-- USUARIOS
INSERT INTO Usuario(id, nombre, apellidoP, apellidoM, fechaNacimiento, correo, contrasena, estatusSesion, credencial)
	VALUES(1,"E","A","M","2023-05-03","adsas@gmail.com","1234567",1,10);
INSERT INTO Usuario(id, nombre, apellidoP, apellidoM, fechaNacimiento, correo, contrasena, estatusSesion, credencial)
	VALUES(2,"H","R","T","2022-03-03","ads3232as@gmail.com","165332567",0,11);
-- CLIENTES
INSERT Cliente(id, direccion, informacion_envio, tarjeta, numero) VALUES (1,"Calle 2","Calle 4", 4343223236,55432323);
-- ADMINISTRADOR
INSERT Administrador(id) VALUES(2);

-- PRODUCTO
INSERT INTO Producto(id, nombre, descripcion, costo) VALUES(1,"Mojito", "Bebida normal", 80.00);
INSERT INTO Producto(id, nombre, descripcion, costo) VALUES(2,"Michelada", "Bebida anormal", 100.00);

-- BEBIDAS
INSERT INTO Bebida(id, ventas) VALUES(1, 0);
INSERT INTO Bebida(id, ventas) VALUES(2, 0);

-- PEDIDO
INSERT INTO Pedido(id , id_cliente, direccion, metodoPago, fecha, total) VALUES(101,1,"NONE","Efectivo","2021-02-03", 240.56);

-- VENTAS
INSERT INTO Venta(id, id_pedido, id_bebida) VALUES(21,101,1);
INSERT INTO Venta(id, id_pedido, id_bebida) VALUES(22,101,1);
INSERT INTO Venta(id, id_pedido, id_bebida) VALUES(23,101,1);

-- CONSULTA TIPO REPORTE DE VENTA
SELECT Pedido.id, CONCAT_WS(" ", Usuario.nombre, Usuario.apellidoP) AS Cliente, Pedido.metodoPago, Pedido.fecha, Pedido.total FROM Venta
	INNER JOIN Pedido ON Venta.id_pedido = Pedido.id
		INNER JOIN Bebida ON Venta.id_bebida = Bebida.id
			INNER JOIN Usuario ON Pedido.id_cliente = Usuario.id;
				-- GROUP BY Pedido.id;




