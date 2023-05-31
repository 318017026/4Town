from alchemy_classes.__init__ import db

class Credencial(db.Model): # type: ignore
    __tablename__='Credencial'
    id = db.Column(db.Integer, primary_key = True)
    tipo = db.Column(db.String(20), nullable = False)

    def __init__(self, id, tipo):
        self.id = id
        self.tipo = tipo

