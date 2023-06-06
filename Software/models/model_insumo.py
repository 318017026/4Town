from models.__init__ import db, Insumo

"""
Función que consulta en la base de datos los Insumos
"""
def enlistaInsumos():
    return db.session.query(Insumo).all()
    
"""
Función que dado un id busca un Insumo con ese ID 
"""
def getInsumo(id):
    return Insumo.query.filter_by(id = id).first()

"""
Funcion que modifica un insumo de la base de datos
"""
def modificaInsumo(id, nombre, descripcion, costo, piezas):
    insumo = Insumo.query.filter_by(id = id).first()
    insumo.nombre = nombre
    insumo.descripcion = descripcion
    insumo.costo = costo
    insumo.piezas = piezas
    db.session.commit()

"""
Función que inserta un Insumo a la base datos
"""
def insertaInsumo(nombre, descripcion, costo, piezas):
    insumo = Insumo(nombre, descripcion, costo, piezas)
    db.session.add(insumo)
    db.session.commit()