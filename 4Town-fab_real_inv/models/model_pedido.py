from alchemyClasses.__init__ import db
from alchemyClasses.Pedido import Pedido

from datetime import datetime, timedelta

def enlistaPedidos():
    return Pedido.query.all()

def enlistaPedidosVendedor(id_vendedor, tiempo):
    if tiempo == "dia":
        actual = datetime.now()
        limite = actual - timedelta(days = 1)
        return Pedido.query.filter_by(id_vendedor=id_vendedor).filter(Pedido.fecha >= limite).all()
    if tiempo == "semana":
        actual = datetime.now()
        limite = actual - timedelta(days = 7)
        return Pedido.query.filter_by(id_vendedor=id_vendedor).filter(Pedido.fecha >= limite).all()
    
def enlistaPedidosCliente(id_cliente):
    return Pedido.query.filter_by(id_cliente=id_cliente).all()

def crearPedido(id_cliente, direccion, metodoPago, total):
    nuevo_pedido = Pedido(id_cliente, direccion, metodoPago, total)
    db.session.add(nuevo_pedido)
    db.session.commit()
    return nuevo_pedido

def agregarVendedor(id_pedido, id_vendedor):
    pedido = Pedido.query.filter(Pedido.id == id_pedido).first()
    pedido.id_vendedor = id_vendedor
    db.session.commit()

def getPedido(id_pedido):
    return Pedido.query.filter(Pedido.id == id_pedido).first()