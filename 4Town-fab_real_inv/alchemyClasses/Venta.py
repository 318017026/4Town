from alchemyClasses.__init__ import db

class Venta(db.Model): # type: ignore
    __tablename__='Venta'
    id = db.Column(db.Integer, primary_key = True)
    id_pedido = db.Column(db.Integer, db.ForeignKey('Pedido.id'), nullable = False)
    id_bebida = db.Column(db.Integer, db.ForeignKey('Bebida.id'), nullable = False)

    def __init__(self, id_pedido, id_bebida):
        self.id_pedido = id_pedido
        self.id_bebida = id_bebida
