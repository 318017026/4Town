from models.__init__ import db, Pedido, datetime, timedelta

def enlistaPedidos():
    return Pedido.query.all()

"""
Función que enlista todos los pedidos que ha atentido un vendedor, ya sea por dia o por semana.
"""
def enlistaPedidosVendedor(id_vendedor, tiempo):
    if tiempo == "dia":
        actual = datetime.now()
        limite = actual - timedelta(days = 1)
        return Pedido.query.filter_by(id_vendedor=id_vendedor).filter(Pedido.fecha >= limite).all()
    if tiempo == "semana":
        actual = datetime.now()
        limite = actual - timedelta(days = 7)
        return Pedido.query.filter_by(id_vendedor=id_vendedor).filter(Pedido.fecha >= limite).all()

"""
Función que dado un id de un cliente, enlista los pedidos que ha realizado un vendedor
"""    
def enlistaPedidosCliente(id_cliente):
    return Pedido.query.filter_by(id_cliente=id_cliente).all()

"""
Función que registra un pedido en la base de datos
"""
def crearPedido(id_cliente, direccion, metodoPago):
    nuevo_pedido = Pedido(id_cliente=id_cliente, direccion=direccion, metodoPago=metodoPago)
    db.session.add(nuevo_pedido)
    db.session.commit()
    return nuevo_pedido

"""
Función que le asigna un vendedor a un pedido cuando es atendido
"""
def agregarVendedor(id_pedido, id_vendedor):
    pedido = Pedido.query.filter(Pedido.id == id_pedido).first()
    pedido.id_vendedor = id_vendedor
    db.session.commit()

"""
Función que te regresa un pedido por su id
"""
def getPedido(id_pedido):
    return Pedido.query.filter(Pedido.id == id_pedido).first()