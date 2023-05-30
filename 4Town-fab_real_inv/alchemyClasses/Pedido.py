from alchemyClasses.__init__ import db

class Pedido(db.Model): # type: ignore
    __tablename__='Pedido'
    id = db.Column(db.Integer, primary_key = True)
    id_cliente = db.Column(db.Integer, db.ForeignKey('Cliente.id'), nullable = False)
    id_vendedor = db.Column(db.Integer, db.ForeignKey('Vendedor.id'), nullable = True)
    id_bebida = db.Column(db.Integer, db.ForeignKey('Bebida.id'), nullable = False)
    direccion = db.Column(db.String(100), nullable = False)
    metodoPago = db.Column(db.String(50), nullable = False)
    fecha = db.Column(db.Date, nullable = False)
    total = db.Column(db.Numeric(6,2), nullable = False)

    def __init__(self, id_cliente, id_bebida, direccion, metodoPago, total):
        self.id_cliente = id_cliente
        self.id_bebida = id_bebida
        self.direccion = direccion
        self.metodoPago = metodoPago
        self.total = total