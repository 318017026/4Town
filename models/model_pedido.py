from datetime import datetime

from alchemyClasses.db import db, Pedido

def enlistaPedidos():
    return Pedido.query.all()

def crearPedido(id_cliente, id_bebida, direccion, metodoPago, total):
    nuevo_predido = Pedido(id_cliente, id_bebida, direccion, metodoPago, datetime.utcnow, total)
    db.session.add(nuevo_predido)
    db.session.commit()

def agregarVendedor(id_pedido, id_vendedor):
    pedido = Pedido.query.filter(Pedido.id == id_pedido).first()
    pedido.id_vendedor = id_vendedor
    db.session.commit()

def getPedido(id_pedido):
    pedido = Pedido.query.filter(Pedido.id == id_pedido).first()