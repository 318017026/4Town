from alchemy_classes.__init__ import db
from alchemy_classes.Vendedor import Vendedor
from alchemy_classes.Cliente import Cliente

class Pedido(db.Model): # type: ignore
    __tablename__='Pedido'
    id = db.Column("id",db.Integer, primary_key = True)
    id_cliente = db.Column("id_cliente", db.Integer, db.ForeignKey(Cliente.id), nullable = False)
    id_vendedor = db.Column("id_vendedor", db.Integer, db.ForeignKey(Vendedor.id), nullable = True)
    direccion = db.Column("direccion",db.String(100), nullable = False)
    metodoPago = db.Column("metodoPago",db.String(50), nullable = False)
    fecha = db.Column("fecha",db.Date, nullable = True)
    total = db.Column("total",db.Numeric(6,2), nullable = False)

    def __init__(self, id_cliente, id_vendedor=None, direccion=None, metodoPago=None, total=0): # El vendedor puede ser nulo hasta que sea atendido
        self.id_cliente = id_cliente
        self.id_vendedor = id_vendedor
        self.direccion = direccion
        self.metodoPago = metodoPago
        self.total = total