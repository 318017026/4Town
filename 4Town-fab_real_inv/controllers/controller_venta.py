from models.model_pedido import enlistaPedidosVendedor

from flask import Blueprint, flash, render_template, request, redirect, url_for, session

venta_bp = Blueprint('venta', __name__, url_prefix='/venta')

@venta_bp.route('/', methods=['GET'])
def venta():
    if session.get('usuario') == None:
        flash('Error: no se ha iniciado sesión')
        return "No se ha iniciado sesión" # Redirigir a iniciar sesión
    if session.get('ventas') == None:
        flash('Error: no permitido')
        return "No permitido" # Redirigir a iniciar sesión o inicio de Usuario
    pedidosDia = enlistaPedidosVendedor(session.get('usuario'), "dia")
    pedidosSemana = enlistaPedidosVendedor(session.get('usuario'), "semana")
    return render_template('pantalla_pedidos.html', pedidosDia = pedidosDia, pedidosSemana = pedidosSemana)