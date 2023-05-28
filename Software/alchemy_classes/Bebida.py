from alchemy_classes.__init__ import db

'''
Clase Bebida representa una entidad de la base de datos
'''
class Bebida(db.Model):
    id = db.Column('id',db.INTEGER, primary_key=True)
    nombre = db.Column('nombre', db.String(30)) 
    descripcion = db.Column('descripcion', db.String(100))
    costo = db.Column('costo', db.Float)
    ventas = db.Column('ventas', db.INTEGER)
    
    '''
    Constructor de clase
    '''
    def __init__(self, id=None, nombre=None, descripcion=None, costo=None, ventas=0):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.costo = costo
        self.ventas = ventas
        
    '''
    Metodo para imprimir el estado de un objeto
    '''
    def __str__(self):
        return f"id={self.id}, nombre={self.nombre}, costo={self.costo}, ventas={self.ventas}"