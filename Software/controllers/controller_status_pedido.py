from controllers.__init__ import Blueprint, session, flash, render_template
from controllers.__init__ import enlistaPedidosCliente

status_pedido_bp = Blueprint('status_pedido', __name__, url_prefix='/status_pedido')

"""
Método que enlista los productos del cliente y le muestra el estatus en el que se encuentra
"""
@status_pedido_bp.route('/', methods = ['GET'])
def status_pedido():
    if session.get('usuario') == None:
        flash('Error: no se ha iniciado sesión')
        return "No se ha iniciado sesión" # Redirigir a iniciar sesión
    if session.get('credencial') != 10: # No es un cliente
        flash("Error: No permitido")
        return "No permitido"
    # Verificar la credencial de cliente
    pedidos = enlistaPedidosCliente(session.get('usuario'))
    id_user = session.get('usuario')
    return render_template("monitorear_status/pantalla_pedidos_cliente.html", pedidos = pedidos, id_user = id_user)