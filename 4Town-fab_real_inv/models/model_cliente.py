from alchemyClasses.Cliente import Cliente

def getCliente(id_cliente):
    return Cliente.query.filter(Cliente.id == id_cliente).first()