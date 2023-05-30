from models.model_pedido import enlistaPedidosCliente

from flask import Blueprint, flash, render_template, request, redirect, url_for, session

status_pedido_bp = Blueprint('status_pedido', __name__, url_prefix='/status_pedido')

@status_pedido_bp.route('/', methods = ['GET'])
def status_pedido():
    if session.get('usuario') == None:
        flash('Error: no se ha iniciado sesión')
        return "No se ha iniciado sesión" # Redirigir a iniciar sesión
    # Verificar la credencial de cliente
    pedidos = enlistaPedidosCliente(session.get('usuario'))
    return render_template("pantalla_pedidos_cliente.html", pedidos = pedidos)