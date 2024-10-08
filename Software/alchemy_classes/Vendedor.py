from alchemy_classes.__init__ import db
from alchemy_classes.Usuario import Usuario

class Vendedor(db.Model): # type: ignore
    __tablename__='Vendedor'
    id = db.Column("id",db.Integer, db.ForeignKey(Usuario.id), primary_key = True)

    def __init__(self, id):
        self.id = id