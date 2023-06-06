from models.__init__ import db, Cliente, Usuario

"""
Función que dado un id regresa el cliente con ese id
"""
def getCliente(id_cliente):
    return Cliente.query.filter(Cliente.id == id_cliente).first()

'''
Función obtiene los datos de los clientes
'''
def getClientes():
    result = db.session.query(Usuario.id, Usuario.nombre, Usuario.apellidoP, Usuario.apellidoM, Usuario.fechaNacimiento, Usuario.correo, Cliente.direccion).join(Cliente).all()
    return result



