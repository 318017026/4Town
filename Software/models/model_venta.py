from models.__init__ import db, Venta # type: ignore

def generaVenta(id_pedido, id_bebida):
    venta = Venta(id_pedido, id_bebida)
    db.session.add(venta)
    db.session.commit()

def generaVentas(id_pedido, id_bebidas):
    for id in id_bebidas:
        db.session.add(Venta(id_pedido, id))
    db.session.commit()
