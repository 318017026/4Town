from alchemyClasses import db
from sqlalchemy import Numeric

class Usuario(db.Model):
    __tablename__ = 'Usuario'
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50), nullable = False)
    apellidoP = db.Column(db.String(50), nullable = False)
    apellidoM = db.Column(db.String(50), nullable = False)
    fechaNacimiento = db.Column(db.Date, nullable = False)
    correo = db.Column(db.String(50), nullable = False)
    contrasena = db.Column(db.String(50), nullable = False)
    estatusSesion = db.Column(db.Boolean, nullable = False)
    credencial = db.Column(db.Integer, db.ForeignKey('Credencial.id'), nullable = False)

    def __init__(self, id, nombre, apellidoP, apellidoM, fechaNacimiento, correo, contrasena, estatusSesion, credencial):
        self.id = id
        self.nombre = nombre
        self.apellidoP = apellidoP
        self.apellidoM = apellidoM
        self.fechaNacimiento = fechaNacimiento
        self.correo = correo
        self.contrasena = contrasena
        self.estatusSesion = estatusSesion
        self.credencial = credencial

class Administrador(db.Model):
    __tablename__='Administrador'
    id = db.Column(db.Integer, db.ForeignKey('Usuario.id'), primary_key = True)

    def __init__(self, id):
        self.id = id

class Vendedor(db.Model):
    __tablename__='Vendedor'
    id = db.Column(db.Integer, db.ForeignKey('Usuario.id'), primary_key = True)

    def __init__(self, id):
        self.id = id

class Cliente(db.Model):
    __tablename__='Cliente'
    id = db.Column(db.Integer, db.ForeignKey('Usuario.id'), primary_key = True)
    direccion = db.Column(db.String(100), nullable = True)
    informacion_envio = db.Column(db.String(100), nullable = True)
    tarjeta = db.Column(db.BigInteger, nullable = True)
    numero = db.Column(db.BigInteger, nullable = True)

    def __init__(self, id, direccion, informacion_envio, tarjeta, numero):
        self.id = id
        self.direccion = direccion
        self.informacion_envio = informacion_envio
        self.tarjeta = tarjeta
        self.numero = numero

class Producto(db.Model):
    __tablename__='Producto'
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(20), nullable = False)
    descripcion = db.Column(db.String(100), nullable = False)
    costo = db.Column(Numeric(6,2), nullable = False)

    def __init__(self, nombre, descripcion, costo):
        self.nombre = nombre
        self.descripcion = descripcion
        self.costo = costo

class Bebida(db.Model):
    __tablename__='Bebida'
    id = db.Column(db.Integer, db.ForeignKey('Producto.id'), primary_key = True)
    ventas = db.Column(db.Integer, nullable = False)

    def __init__(self, id, ventas):
        self.id = id
        self.ventas = ventas

class Insumo(db.Model):
    __tablename__='Insumo'
    id = db.Column(db.Integer, db.ForeignKey('Producto.id'),primary_key = True)
    piezas = db.Column(db.Integer, nullable = False)

    def __init__(self, id, piezas):
        self.id = id
        self.piezas = piezas

class Pedido(db.Model):
    __tablename__='Pedido'
    id = db.Column(db.Integer, primary_key = True)
    id_cliente = db.Column(db.Integer, nullable = False)
    id_vendedor = db.Column(db.Integer, nullable = False)
    direccion = db.Column(db.String(100), nullable = False)
    metodoPago = db.Column(db.String(50), nullable = False)
    fecha = db.Column(db.Date, nullable = False)
    total = db.Column(db.Numeric(6,2), nullable = True)


    def __init__(self, id, id_cliente, id_vendedor, direccion, metodoPago, fecha, total):
        self.id = id
        self.id_cliente = id_cliente
        self.id_vendedor = id_vendedor
        self.direccion = direccion
        self.metodoPago = metodoPago
        self.fecha = fecha
        self.total = total

class Venta(db.Model):
    __tablename__='Venta'
    id = db.Column(db.Integer, primary_key = True)
    id_pedido = db.Column(db.Integer, db.ForeignKey('Pedido.id'), nullable = False)
    id_bebida = db.Column(db.Integer, db.ForeignKey('Bebida.id'), nullable = False)

    def __init__(self, id, id_pedido, id_bebida):
        self.id = id
        self.id_pedido = id_pedido
        self.id_bebida = id_bebida

class Credencial(db.Model):
    __tablename__='Credencial'
    id = db.Column(db.Integer, primary_key = True)
    tipo = db.Column(db.String(20), nullable = False)