from alchemyClasses.db import Cliente

def getCliente(id_cliente):
    return Cliente.query.filter(Cliente.id == id).first()