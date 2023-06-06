from alchemy_classes.__init__ import db

'''
Clase Usuario representa una entidad de la base de datos
'''
class Usuario(db.Model): # type: ignore
    __tablename__ = 'Usuario'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50), nullable = False)
    nombre = db.Column(db.String(50), nullable = False)
    apellidoP = db.Column(db.String(50), nullable = False)
    apellidoM = db.Column(db.String(50), nullable = False)
    fechaNacimiento = db.Column(db.Date, nullable = False)
    correo = db.Column(db.String(50), nullable = False)
    contrasena = db.Column(db.String(50), nullable = False)
    estatusSesion = db.Column(db.Boolean, nullable = False)
    credencial = db.Column(db.Integer, db.ForeignKey('Credencial.id'), nullable = False)
    
    '''
    Constructor de clase
    '''
    def __init__(self, id=None, username=None, nombre=None, apellidoP=None, apellidoM=None, fechaNacimiento=None, 
                 correo=None, contrasena=None, estatusSesion=None, credencial=None):
        self.id = id
        self.username = username
        self.nombre = nombre
        self.apellidoP = apellidoP
        self.apellidoM = apellidoM
        self.fechaNacimiento = fechaNacimiento
        self.correo = correo
        self.contrasena = contrasena
        self.estatusSesion = estatusSesion
        self.credencial = credencial
        
    '''
    Metodo para imprimir el estado de un objeto
    '''
    def __str__(self):
        return f"id={self.id}, username={self.username}, nombre={self.nombre}, credencial={self.credencial}"
    
    '''
    Metodo que activa el estatusSesion de un Usuario
    '''
    def activate(self):
        self.estatusSesion = True
    '''
    Metodo que desactiva el estatusSesion de un Usuario
    '''
    def deactivate(self):
        self.estatusSesion = False