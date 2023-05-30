from alchemyClasses.__init__ import db

class Insumo(db.Model): # type: ignore
    __tablename__='Insumo'
    id = db.Column(db.Integer,primary_key = True)
    nombre = db.Column('nombre', db.String(30)) 
    descripcion = db.Column('descripcion', db.String(100))
    costo = db.Column('costo', db.Float)
    piezas = db.Column(db.Integer, nullable = False)

    def __init__(self, nombre, descripcion, costo, piezas):
        self.nombre = nombre
        self.descripcion = descripcion
        self.costo = costo
        self.piezas = piezas