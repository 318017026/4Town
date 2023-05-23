from alchemyClasses.db import db, Venta

def atenderPedido(id_pedido, id_bebida):
    venta = Venta(id_pedido, id_bebida)
    db.session.add(venta)
    db.session.commit()
