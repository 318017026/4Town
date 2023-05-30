from alchemyClasses.__init__ import db

class Cliente(db.Model): # type: ignore
    __tablename__='Cliente'
    id = db.Column(db.Integer, db.ForeignKey('Usuario.id'), primary_key = True)
    direccion = db.Column(db.String(100), nullable = True)
    informacion_envio = db.Column(db.String(100), nullable = True)
    tarjeta = db.Column(db.BigInteger, nullable = True)
    numero = db.Column(db.BigInteger, nullable = True)

    def __init__(self, id, direccion, informacion_envio, tarjeta, numero):
        self.id = id
        self.direccion = direccion
        self.informacion_envio = informacion_envio
        self.tarjeta = tarjeta
        self.numero = numero