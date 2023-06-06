from controllers.__init__ import Blueprint, session, flash, render_template
from controllers.__init__ import enlistaPedidosVendedor, obtener_ventas, obtener_ventas_eliminados

venta_bp = Blueprint('venta', __name__, url_prefix='/venta')
reporteVenta_bp = Blueprint('reporte_venta', __name__, url_prefix='/venta')

"""
Método que enlista los pedidos que ha atendido un vendedor
"""
@venta_bp.route('/venta', methods=['GET'])
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
""""
Método que enlista el reporte de las ventas realizadas
Nota: Contiene reestricción, sólo el administrador puede realizar esta operación
"""
@reporteVenta_bp.route('/reporte_venta', methods=['GET'])
def reporteVenta():
    if session.get('usuario') == None:
        flash('Error: no se ha iniciado sesión')
        return "No se ha iniciado sesión" # Redirigir a iniciar sesión
    print(session.get('credencial'))
    if session.get('credencial') == 11:
        r_ventas = obtener_ventas() # type: ignore
        r_ventasEliminados = obtener_ventas_eliminados()    
        return render_template('Administrador/consultar_reporteVenta.html', ventas = r_ventas, ventasEliminadas= r_ventasEliminados, nv=1, nve=1)
    else:
        flash('Error: no permitido')
        return "No permitido" # Redirigir a iniciar sesión o inicio de Usuario
    
    
