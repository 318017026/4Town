from alchemy_classes.__init__ import db

'''
Clase Usuario representa una entidad de la base de datos
'''
class Usuario(db.Model):  
    id = db.Column('id',db.INTEGER, primary_key=True)
    username = db.Column('username', db.String(50))
    nombre = db.Column('nombre', db.String(30)) 
    apellidoP = db.Column('apellidoP', db.String(50))
    apellidoM = db.Column('apellidoM', db.String(50))
    fechaNacimiento = db.Column('fechaNacimiento', db.DateTime)
    correo = db.Column('correo', db.String(50))
    contrasena = db.Column('contrasena', db.String(50))
    estatusSesion = db.Column('estatusSesion', db.Boolean)
    credencial = db.Column('credencial', db.INTEGER)
    
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