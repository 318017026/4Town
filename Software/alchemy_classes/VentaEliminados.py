from alchemy_classes.__init__ import db
from alchemy_classes.Pedido import Pedido

class VentaEliminados(db.Model): # type: ignore
    __tablename__='VentaEliminados'
    id = db.Column('id',db.INTEGER, primary_key=True, nullable = False)
    id_pedido = db.Column('id_pedido',db.INTEGER,db.ForeignKey(Pedido.id), nullable=False)
    bebida = db.Column('bebida', db.String(30), nullable = False)
    costo = db.Column('costo', db.Float, nullable = False)
    
    def __init__(self, id=None, id_pedido=None, bebida=None, costo=0):
        self.id = id
        self.id_pedido = id_pedido
        self.bebida = bebida
        self.costo = costo
        