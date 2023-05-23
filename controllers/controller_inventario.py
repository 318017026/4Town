from models.model_producto import enlistaBebidas, enlistaInsumos, getProducto, isBebida, getInsumo, modificaInsumo, modificaProducto, insertaBebida, insertaInsumo

from flask import Blueprint, flash, render_template, request, redirect, url_for, session

inventario_bp = Blueprint('inventario' , __name__, url_prefix='/inventario')

@inventario_bp.route('/', methods=['GET'])
def inventario():
    if session.get('usuario') == None: # No se ha iniciado sesión
        flash("Error: no se ha iniciado sesión")
        return "No se ha iniciado sesión" # Redirgir a iniciar sesión
    if session.get('ventas') == None: # No es un vendedor.
        flash("Error: no permitido")
        return "No permitido" # Redirigir a iniciar sesión o inicio de Usuario
    if request.method == 'GET':
        bebidas = enlistaBebidas()
        insumos = enlistaInsumos()
        return render_template('pantalla_inventario.html', bebidas = bebidas, insumos = insumos)
    
@inventario_bp.route('/modify', methods=['POST'])
def modify():
    if session.get('usuario') == None: # No se ha inicado sesion
        flash("Error: no se ha iniciado sesion")
        return "No se ha iniciado sesion"
    if session.get('ventas') == None: # No es un vendedor
        flash("Error: no permitido")
        return "No permitido" # Redirigir a iniciar sesion o incio de Usuario
    id_producto = request.form.get('id')
    if id_producto == None: # No se ha seleccionado un producto
        flash("Error: no se ha seleccionado un producto")
        return redirect(url_for('inventario.inventario'))
    producto = getProducto(id_producto)
    #if isBebida(id_producto):
    #    return render_template('modificar_bebida.html', producto = producto)
    return render_template('modificar_insumo.html', producto = producto, insumo = getInsumo(id_producto))

@inventario_bp.route('/modify_bebida', methods=['POST'])
def modify_bebida():
    if session.get('usuario') == None: # No se ha inicado sesion
        flash("Error: no se ha iniciado sesion")
        return "No se ha iniciado sesion"
    if session.get('ventas') == None: # No es un vendedor
        flash("Error: no permitido")
        return "No permitido" # Redirigir a iniciar sesion o incio de Usuario
    id_producto = request.form.get('id')
    if id_producto == None: # No se ha seleccionado un producto
        flash("Error: no se ha seleccionado un producto")
        return redirect(url_for('inventario.inventario'))
    nombre_producto = request.form.get('nombre')
    if len(nombre_producto) > 20:
        flash("Error: nombre sobrepasa los 20 caracteres")
        return redirect(url_for('inventario.inventario'))
    descripcion_producto = request.form.get('descripcion')
    if len(descripcion_producto) > 100:
        flash("Error: nombre sobrepasa los 100 caracteres")
        return redirect(url_for('inventario.inventario'))
    costo_producto = request.form.get('costo')
    modificaProducto(id_producto, nombre_producto, descripcion_producto, costo_producto)
    flash('Producto modificado exitosamente')
    return redirect(url_for('inventario.inventario'))

@inventario_bp.route('/modify_insumo', methods=['POST'])
def modify_insumo():
    if session.get('usuario') == None: # No se ha inicado sesion
        flash("Error: no se ha iniciado sesion")
        return "No se ha iniciado sesion"
    if session.get('ventas') == None: # No es un vendedor
        flash("Error: no permitido")
        return "No permitido" # Redirigir a iniciar sesion o incio de Usuario
    id_producto = request.form.get('id')
    if id_producto == None: # No se ha seleccionado un producto
        flash("Error: no se ha seleccionado un producto")
        return redirect(url_for('inventario.inventario'))
    nombre_producto = request.form.get('nombre')
    if len(nombre_producto) > 20:
        flash("Error: nombre sobrepasa los 20 caracteres")
        return redirect(url_for('inventario.inventario'))
    descripcion_producto = request.form.get('descripcion')
    if len(descripcion_producto) > 100:
        flash("Error: nombre sobrepasa los 100 caracteres")
        return redirect(url_for('inventario.inventario'))
    costo_producto = request.form.get('costo')
    piezas_insumo = request.form.get('piezas')
    modificaInsumo(id_producto, nombre_producto, descripcion_producto, costo_producto, piezas_insumo)
    flash('Insumo modificado exitosamente')
    return redirect(url_for('inventario.inventario'))

@inventario_bp.route('/add_bebida', methods=['GET','POST'])
def add_bebida():
    if session.get('usuario') == None: # No se ha inicado sesion
        flash("Error: no se ha iniciado sesion")
        return "No se ha iniciado sesion"
    if session.get('ventas') == None: # No es un vendedor
        flash("Error: no permitido")
        return "No permitido" # Redirigir a iniciar sesion o incio de Usuario
    if request.method == 'POST':
        nombre_bebida = request.form.get('nombre')
        if len(nombre_bebida) > 20:
            flash("Error: nombre sobrepasa los 20 caracteres")
            return redirect(url_for('inventario.inventario'))
        descripcion_bebida = request.form.get('descripcion')
        if len(descripcion_bebida) > 100:
            flash("Error: nombre sobrepasa los 100 caracteres")
            return redirect(url_for('inventario.inventario'))
        costo_bebida = request.form.get('costo')
        insertaBebida(nombre_bebida, descripcion_bebida, costo_bebida)
        flash("Bebida creada con éxito")
        return redirect(url_for('inventario.inventario'))
    else:
        return render_template('agregar_bebida.html')
    
@inventario_bp.route('/add_insumo', methods=['GET','POST'])
def add_insumo():
    if session.get('usuario') == None: # No se ha inicado sesion
        flash("Error: no se ha iniciado sesion")
        return "No se ha iniciado sesion"
    if session.get('ventas') == None: # No es un vendedor
        flash("Error: no permitido")
        return "No permitido" # Redirigir a iniciar sesion o incio de Usuario
    if request.method == 'POST':
        nombre_insumo = request.form.get('nombre')
        if len(nombre_insumo) > 20:
            flash("Error: nombre sobrepasa los 20 caracteres")
            return redirect(url_for('inventario.inventario'))
        descripcion_insumo = request.form.get('descripcion')
        if len(descripcion_insumo) > 100:
            flash("Error: nombre sobrepasa los 100 caracteres")
            return redirect(url_for('inventario.inventario'))
        costo_insumo = request.form.get('costo')
        piezas_insumo = request.form.get('piezas')
        insertaInsumo(nombre_insumo, descripcion_insumo, costo_insumo, piezas_insumo)
        flash("Insumo agregado con éxito")
        return redirect(url_for('inventario.inventario'))
    else:
        return render_template('agregar_insumo.html')