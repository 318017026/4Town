from controllers.__init__ import Blueprint, session, flash, render_template
from controllers.__init__ import getClientes

consultarCliente_bp = Blueprint('consultar_cliente', __name__, url_prefix='/consultar_cliente')

@consultarCliente_bp.route('/', methods=['GET'])
def consultarCliente():
    if session.get('usuario') == None:
        flash('Error: no se ha iniciado sesión')
        return "No se ha iniciado sesión" # Redirigir a iniciar sesión
    if session.get('credencial') == 10:
        flash('Error: no permitido')
        return "No permitido" # Redirigir a iniciar sesión o inicio de Usuario
    if session.get('credencial') == 11:
        clientes = getClientes()
        return render_template('Administrador/consultar_cliente.html', clientes=clientes)
    if session.get('credencial') == 12:
        clientes = getClientes()
        return render_template('Vendedor/consultar_cliente.html', clientes=clientes)

