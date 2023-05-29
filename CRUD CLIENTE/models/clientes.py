from utils.db import db

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

class Credencial(db.Model):
    __tablename__='Credencial'
    id = db.Column(db.Integer, primary_key = True)
    tipo = db.Column(db.String(20), nullable = False)

    def __init__(self, id, tipo):
        self.id = id
        self.tipo = tipo
