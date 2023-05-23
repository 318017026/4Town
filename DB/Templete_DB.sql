CREATE DATABASE ingsoft;
USE ingsoft;
CREATE TABLE Usuario (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
    apellidoP VARCHAR(50) NOT NULL,
	apellidoM VARCHAR(50) NOT NULL,
    fechaNacimiento date NOT NULL,
    correo VARCHAR(50) NOT NULL,
    contrasena VARCHAR(50) NOT NULL,
    estatusSesion boolean NOT NULL,
    credencial INT NOT NULL,
    FOREIGN KEY (credencial) REFERENCES Credencial(id)
    -- Pueden agregar constraints
);
CREATE TABLE Administrador (
    id INT PRIMARY KEY AUTO_INCREMENT,
    FOREIGN KEY (id) REFERENCES Usuario(id)
    -- Pueden agregar constraints o atributos
);
CREATE TABLE Vendedor (
    id INT PRIMARY KEY AUTO_INCREMENT,
    FOREIGN KEY (id) REFERENCES Usuario(id)
    -- Pueden agregar constraints o atributos
);
CREATE TABLE Cliente (
    id INT PRIMARY KEY AUTO_INCREMENT,
    direccion VARCHAR(100),
    informacion_envio VARCHAR(100),
    tarjeta BIGINT,
    numero BIGINT,
    FOREIGN KEY (id) REFERENCES Usuario(id)
    -- Pueden agregar constraints o atributos
);

CREATE TABLE Producto(
	id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(20) NOT NULL,
    descripcion VARCHAR(100) NOT NULL,
    costo decimal(6,2) NOT NULL
    -- Pueden agregar constraints o atributos
);

CREATE TABLE Bebida(
	id INT PRIMARY KEY AUTO_INCREMENT,
    ventas INT NOT NULL,
    FOREIGN KEY (id) REFERENCES Producto(id)
    -- Pueden agregar constraints o atributos
);
CREATE TABLE Insumo(
	id INT PRIMARY KEY AUTO_INCREMENT,
    piezas INT NOT NULL,
    FOREIGN KEY (id) REFERENCES Producto(id)
    -- Pueden agregar constraints o atributos
);

CREATE TABLE Pedido(
	id INT PRIMARY KEY AUTO_INCREMENT,
    id_cliente INT NOT NULL,
    id_vendedor INT, -- Lo hice posiblemente null para que después un vendedor lo pueda atender
    id_bebida INT NOT NULL, -- para guardar la bebida que se compró
    direccion VARCHAR(100) NOT NULL,
    metodoPago VARCHAR(50) NOT NULL,
    fecha date NOT NULL,
    total decimal(6,2) NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES Cliente(id),
    FOREIGN KEY (id_vendedor) REFERENCES Vendedor(id),
    FOREIGN KEY (id_bebida) REFERENCES Bebida(id)
    -- Pueden agregar constraints o atributos
);

CREATE TABLE Venta(
	id INT PRIMARY KEY AUTO_INCREMENT,
    id_pedido INT NOT NULL,
    id_bebida INT NOT NULL,
	FOREIGN KEY (id_pedido) REFERENCES Pedido(id),
	FOREIGN KEY (id_bebida) REFERENCES Bebida(id)
    -- Pueden agregar constraints o atributos
);

CREATE TABLE Credencial(
	id INT PRIMARY KEY AUTO_INCREMENT,
    tipo VARCHAR(20) NOT NULL
);