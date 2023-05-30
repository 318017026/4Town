from alchemyClasses.__init__ import db
from alchemyClasses.Insumo import Insumo

def enlistaInsumos():
    return db.session.query(Insumo).all()
    
def getInsumo(id):
    return Insumo.query.filter_by(id = id).first()

def modificaInsumo(id, nombre, descripcion, costo, piezas):
    insumo = Insumo.query.filter_by(id = id).first()
    insumo.nombre = nombre
    insumo.descripcion = descripcion
    insumo.costo = costo
    insumo.piezas = piezas
    db.session.commit()

def insertaInsumo(nombre, descripcion, costo, piezas):
    insumo = Insumo(nombre, descripcion, costo, piezas)
    db.session.add(insumo)
    db.session.commit()