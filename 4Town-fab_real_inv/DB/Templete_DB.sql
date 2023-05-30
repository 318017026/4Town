CREATE DATABASE ingsoft;
USE ingsoft;
-- Entidad Credencial
CREATE TABLE Credencial(
	id INT PRIMARY KEY AUTO_INCREMENT,
    tipo VARCHAR(20) NOT NULL
);
-- Entidad Usuario (Entidad Padre)
CREATE TABLE Usuario (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL,
    nombre VARCHAR(50) NOT NULL,
    apellidoP VARCHAR(50) NOT NULL,
	apellidoM VARCHAR(50) NOT NULL,
    fechaNacimiento date NOT NULL,
    correo VARCHAR(50) NOT NULL,
    contrasena VARCHAR(50) NOT NULL,
    estatusSesion boolean NOT NULL,
    credencial INT NOT NULL,
    FOREIGN KEY (credencial) REFERENCES Credencial(id)
);
-- Entidad Administrador (Entidad hija de Usuario)
CREATE TABLE Administrador (
    id INT PRIMARY KEY AUTO_INCREMENT,
    FOREIGN KEY (id) REFERENCES Usuario(id)
);
-- Entidad Vendedor (Entidad hija de Usuario)
CREATE TABLE Vendedor (
    id INT PRIMARY KEY AUTO_INCREMENT,
    FOREIGN KEY (id) REFERENCES Usuario(id)
);
-- Entidad Cliente (Entidad hija de Usuario)
CREATE TABLE Cliente (
    id INT PRIMARY KEY AUTO_INCREMENT,
    direccion VARCHAR(100),
    informacion_envio VARCHAR(100),
    tarjeta BIGINT,
    numero BIGINT,
    FOREIGN KEY (id) REFERENCES Usuario(id)
);
-- Entidad Bebida
CREATE TABLE Bebida(
	id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(30) NOT NULL,
    descripcion VARCHAR(250) NOT NULL,
    costo decimal(6,2) NOT NULL,
    ventas INT NOT NULL DEFAULT(0)
);
-- Entidad Insumo
CREATE TABLE Insumo(
	id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(30) NOT NULL,
    descripcion VARCHAR(250) NOT NULL,
    costo decimal(6,2) NOT NULL,
    piezas INT NOT NULL
);
-- Entidad Pedido
CREATE TABLE Pedido(
	id INT PRIMARY KEY AUTO_INCREMENT,
    id_cliente INT NOT NULL,
    direccion VARCHAR(100) NOT NULL,
    metodoPago VARCHAR(50) NOT NULL,
    fecha DATE NOT NULL,
    total DECIMAL(6,2) NOT NULL
);

CREATE TABLE Venta(
	id INT PRIMARY KEY AUTO_INCREMENT,
    id_pedido INT NOT NULL,
    id_bebida INT NOT NULL,
	FOREIGN KEY (id_pedido) REFERENCES Pedido(id),
	FOREIGN KEY (id_bebida) REFERENCES Bebida(id) 
);

CREATE TABLE Venta_Eliminados(
	id INT PRIMARY KEY AUTO_INCREMENT,
    id_pedido INT NOT NULL,
    bebida VARCHAR(30) NOT NULL,
    costo DECIMAL(6,2) NOT NULL,
    FOREIGN KEY (id_pedido) REFERENCES Pedido(id)
);

-- Disparadores
-- Trigger que aumenta el numero de ventas de un producto cada vez que se crea un registro en venta
DELIMITER //
CREATE TRIGGER UPDATE_BEBIDA_AI AFTER INSERT ON Venta FOR EACH ROW
BEGIN
	UPDATE Bebida SET ventas = ventas + 1 WHERE Bebida.id=NEW.id_bebida;
END //
DELIMITER ;

-- Trigger para insertar ventas de productos eliminados
DELIMITER //
CREATE TRIGGER INSERT_VENTA_ELIMINADO_BD BEFORE DELETE ON Venta FOR EACH ROW
BEGIN
	DECLARE n VARCHAR(30);
    DECLARE c DECIMAL(6,2);
    DECLARE id_p INT;
    SELECT nombre INTO n FROM Bebida WHERE id=OLD.id_bebida;
	SELECT costo INTO c FROM Bebida WHERE id=OLD.id_bebida;
    SELECT id_pedido INTO id_p FROM venta WHERE id = OLD.id;
    INSERT INTO venta_eliminados(id_pedido, bebida, costo) VALUES (id_p, n, c);
END //
DELIMITER ;

-- Trigger para eliminar ventas relacionadas a una bebida
DELIMITER //
CREATE TRIGGER DELETE_VENTA_AD BEFORE DELETE ON Bebida FOR EACH ROW
BEGIN
	DELETE FROM Venta WHERE id_bebida = OLD.id;
END //
DELIMITER ;

-- Consultas básicas
select * from usuario;
select * from cliente;
select * from administrador;
select * from vendedor;
select * from credencial;
select * from insumo;
select * from bebida;
select * from venta;
select * from venta_eliminados;
select * from pedido;