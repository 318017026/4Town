from alchemyClasses.__init__ import db
class Administrador(db.Model): # type: ignore
    __tablename__='Administrador'
    id = db.Column(db.Integer, db.ForeignKey('Usuario.id'), primary_key = True)

    def __init__(self, id):
        self.id = id