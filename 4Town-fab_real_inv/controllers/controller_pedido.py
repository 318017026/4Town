from models.model_pedido import crearPedido
from models.model_cliente import getCliente
from models.model_bebida import getBebidas, calculaTotal
from models.model_venta import generaVentas
from alchemyClasses.Bebida import Bebida
from flask import Blueprint, flash, render_template, request, redirect, url_for, session

pedido_bp = Blueprint('pedido', __name__, url_prefix='/pedido')

@pedido_bp.route('/', methods=['GET','POST'])
def pedido():
    if session.get('usuario') == None: # No se ha iniciado sesión
        flash("Error: no se ha iniciado sesión")
        return "No se ha iniciado sesión" # Redirigir a iniciar sesión
    id_bebidas = session.get('bebidas') # Hay que guardar una lista con los ids de los productos seleccionados / añadidos al carrito
                    # Hay que mandar un request a ésta página con la lista de ids seleccionados
                    # cuando se haga, hay que cambiar session.get('bebidas') por donde se almacene esta lista. 
    if id_bebidas == None:
        flash("Error: no se ha seleccionado productos") # Debe conectarse con el de visualizar producto
        return "No se han seleccionado productos"
    bebidas = getBebidas(id_bebidas)
    return render_template('hacer_pedido.html', bebidas = bebidas)
    
@pedido_bp.route('/hacer_pedido', methods=['POST'])
def hacer_pedido():
    if session.get('usuario') == None: # No se ha iniciado sesión
        flash("Error: no se ha iniciado sesión")
        return "No se ha inciado sesión" # Redirigir a inciar sesión
    id_bebidas = request.form.getlist('bebidas[]')
    if id_bebidas == None:
        flash("Error: no hay productos seleccionados")
        return "No hay productos seleccionados"
    cliente = getCliente(session.get('usuario'))
    metodoPago = request.form.get('metodoPago')
    total = calculaTotal(id_bebidas)
    nuevo_pedido = crearPedido(cliente.id, cliente.direccion, metodoPago, total)
    generaVentas(nuevo_pedido.id, id_bebidas)
    flash("Pedido creado exitosamente")
    return "Pedido creado exitosamente" # Debe mandar a otra página

