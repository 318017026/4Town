from alchemyClasses.__init__ import db
from alchemyClasses.Bebida import Bebida

import numpy as np # Agregar a requirements.txt

def getBebida(id):
    return Bebida.query.filter_by(id = id).first()

def getBebidas(id_bebidas): # Recibe una lista de ids
    bebidas = []
    for id in id_bebidas:
        bebidas.append(getBebida(id))
    return bebidas

def calculaTotal(id_bebidas):
    return db.session.query(db.func.sum(Bebida.costo)).filter(Bebida.id.in_(id_bebidas)).scalar()
