from models.model_pedido import crearPedido
from models.model_producto import getProducto
from models.model_cliente import getCliente

from flask import Blueprint, flash, render_template, request, redirect, url_for, session

pedido_bp = Blueprint('pedido', __name__, url_prefix='/pedido')

@pedido_bp.route('/', methods=['POST'])
def pedido():
    if session.get('id_usuario') == None: # No se ha iniciado sesión
        flash("Error: no se ha iniciado sesión")
        return "No se ha iniciado sesión" # Redirigir a iniciar sesión
    id_producto = request.get('producto')
    if id_producto == None:
        flash("Error: no se ha seleccionado producto") # Debe conectarse con el de visualizar producto
        return "No se ha seleccionado producto"
    producto = getProducto(id_producto)
    
@pedido_bp.route('/', methods=['POST'])
def hacer_pedido():
    if session.get('id_usuario') == None: # No se ha iniciado sesión
        flash("Error: no se ha iniciado sesión")
        return "No se ha inciado sesión" # Redirigir a inciar sesión
    id_producto = request.get('producto')
    if id_producto == None:
        flash("Error: no hay producto seleccionado")
        return "No hay producto seleccionado"
    cliente = getCliente(session.get('id_usuario'))
    id_producto = request.form.get('producto')
    metodoPago = request.form.get('metodoPago')
    producto = getProducto(id_producto)
    crearPedido(cliente.id, 
                id_producto,
                metodoPago,
                producto.costo)
    flash("Pedido creado exitosamente")
    return "Pedido creado exitosamente" # Debe mandar a otra página

