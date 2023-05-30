from alchemyClasses.__init__ import db
from alchemyClasses.Pedido import Pedido

def enlistaPedidos():
    return Pedido.query.all()

def crearPedido(id_cliente, id_bebida, direccion, metodoPago, total):
    nuevo_pedido = Pedido(id_cliente, id_bebida, direccion, metodoPago, total)
    db.session.add(nuevo_pedido)
    db.session.commit()

def agregarVendedor(id_pedido, id_vendedor):
    pedido = Pedido.query.filter(Pedido.id == id_pedido).first()
    pedido.id_vendedor = id_vendedor
    db.session.commit()

def getPedido(id_pedido):
    return Pedido.query.filter(Pedido.id == id_pedido).first()