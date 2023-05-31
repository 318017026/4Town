from controllers.__init__ import Blueprint, session, flash, render_template
from controllers.__init__ import enlistaPedidosVendedor

venta_bp = Blueprint('venta', __name__, url_prefix='/venta')

@venta_bp.route('/', methods=['GET'])
def venta():
    if session.get('usuario') == None:
        flash('Error: no se ha iniciado sesión')
        return "No se ha iniciado sesión" # Redirigir a iniciar sesión
    if session.get('credencial') != 12:
        flash('Error: no permitido')
        return "No permitido" # Redirigir a iniciar sesión o inicio de Usuario
    pedidosDia = enlistaPedidosVendedor(session.get('usuario'), "dia")
    pedidosSemana = enlistaPedidosVendedor(session.get('usuario'), "semana")
    return render_template('reportes_venta/pantalla_pedidos.html', pedidosDia = pedidosDia, pedidosSemana = pedidosSemana)