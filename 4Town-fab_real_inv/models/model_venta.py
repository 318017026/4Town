from alchemyClasses.__init__ import db
from alchemyClasses.Venta import Venta

def atenderPedido(id_pedido, id_bebida):
    venta = Venta(id_pedido, id_bebida)
    db.session.add(venta)
    db.session.commit()
