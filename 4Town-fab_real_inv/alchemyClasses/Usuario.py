from alchemyClasses.__init__ import db

class Usuario(db.Model): # type: ignore
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