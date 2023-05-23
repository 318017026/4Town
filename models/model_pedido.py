from datetime import datetime

from alchemyClasses.db import db, Pedido

def crearPedido(id_cliente, id_bebida, direccion, metodoPago, total):
    nuevo_predido = Pedido(id_cliente, id_bebida, direccion, metodoPago, datetime.utcnow, total)
    db.session.add(nuevo_predido)
    db.session.commit()