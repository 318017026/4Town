from alchemyClasses.__init__ import db

class Vendedor(db.Model): # type: ignore
    __tablename__='Vendedor'
    id = db.Column(db.Integer, db.ForeignKey('Usuario.id'), primary_key = True)

    def __init__(self, id):
        self.id = id