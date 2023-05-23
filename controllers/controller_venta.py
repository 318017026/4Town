from models.model_pedido import enlistaPedidos, agregarVendedor, getPedido
from models.model_venta import atenderPedido

from flask import Blueprint, flash, render_template, request, redirect, url_for, session

venta_bp = Blueprint('venta', __name__, url_prefix='/venta')

@venta_bp.route('/', methods=['GET','POST'])
def venta():
    if session.get('usuario') == None:
        flash('Error: no se ha iniciado sesión')
        return "No se ha iniciado sesión" # Redirigir a iniciar sesión
    if session.get('ventas') == None:
        flash('Error: no permitido')
        return "No permitido" # Redirigir a iniciar sesión o inicio de Usuario
    if request.method == 'GET':
        pedidos = enlistaPedidos()
        return render_template('pantalla_pedidos.html', pedidos = pedidos)
    
@venta_bp.route('/atender', methods=['POST'])
def atender():
    id_pedido = request.form.get('id')
    pedido = getPedido(id_pedido)
    return render_template('atender_pedido.html', pedido = pedido)

@venta_bp.route('/reportar', methods=['POST'])
def reportar():
    id_pedido = request.form.get('id')
    agregarVendedor(session.get('usuario'))
    pedido = getPedido(id_pedido)
    atenderPedido(id_pedido, pedido.id_bebida)
    flash('Pedido reportado exitosamente')
    return "Pedido reportado exitosamente"