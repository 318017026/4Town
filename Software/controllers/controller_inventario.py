#from models.model_insumo import enlistaInsumos, getInsumo, modificaInsumo, insertaInsumo
from controllers.__init__ import Blueprint, session, flash, request, redirect, url_for,render_template, getInsumo
from controllers.__init__ import enlistaInsumos, modificaInsumo,insertaInsumo

inventario_bp = Blueprint('inventario' , __name__, url_prefix='/inventario')

@inventario_bp.route('/', methods=['GET']) # type: ignore
def inventario():
    if session.get('usuario') == None: # No se ha iniciado sesión
        flash("Error: no se ha iniciado sesión")
        return "No se ha iniciado sesión" # Redirgir a iniciar sesión
    if session.get('credencial') != 12: # No es un vendedor.
        flash("Error: no permitido") # Redirigir al menú de usuario correspondiente
        return "No permitido" # Redirigir a iniciar sesión o inicio de Usuario
    if request.method == 'GET':
       
        insumos = enlistaInsumos()
        return render_template('realizar_inventario/pantalla_inventario.html', insumos = insumos)
    
@inventario_bp.route('/modify', methods=['POST'])
def modify():
    if session.get('usuario') == None: # No se ha inicado sesion
        flash("Error: no se ha iniciado sesion")
        return "No se ha iniciado sesion"
    if session.get('credencial') != 12: # No es un vendedor
        flash("Error: no permitido")
        return "No permitido" # Redirigir a iniciar sesion o incio de Usuario
    id_insumo = request.form.get('id')
    if id_insumo == None: # No se ha seleccionado un producto
        flash("Error: no se ha seleccionado un producto")
        return redirect(url_for('inventario.inventario'))
    insumo = getInsumo(id_insumo)
    #if isBebida(id_producto):
    #    return render_template('modificar_bebida.html', producto = producto)
    return render_template('realizar_inventario/modificar_insumo.html', insumo = insumo)



@inventario_bp.route('/modify_insumo', methods=['POST'])
def modify_insumo():
    if session.get('usuario') == None: # No se ha inicado sesion
        flash("Error: no se ha iniciado sesion")
        return "No se ha iniciado sesion"
    if session.get('credencial') != 12: # No es un vendedor
        flash("Error: no permitido")
        return "No permitido" # Redirigir a iniciar sesion o incio de Usuario
    id_insumo = request.form.get('id')
    if id_insumo == None: # No se ha seleccionado un producto
        flash("Error: no se ha seleccionado un producto")
        return redirect(url_for('inventario.inventario'))
    nombre_insumo = request.form.get('nombre')
    if len(nombre_insumo) > 20: # type: ignore
        flash("Error: nombre sobrepasa los 20 caracteres")
        return redirect(url_for('inventario.inventario'))
    descripcion_insumo = request.form.get('descripcion')
    if len(descripcion_insumo) > 100: # type: ignore
        flash("Error: nombre sobrepasa los 100 caracteres")
        return redirect(url_for('inventario.inventario'))
    costo_insumo = request.form.get('costo')
    piezas_insumo = request.form.get('piezas')
    modificaInsumo(id_insumo, nombre_insumo, descripcion_insumo, costo_insumo, piezas_insumo)
    flash('Insumo modificado exitosamente')
    return redirect(url_for('inventario.inventario'))

    
@inventario_bp.route('/add_insumo', methods=['GET','POST'])
def add_insumo():
    if session.get('usuario') == None: # No se ha inicado sesion
        flash("Error: no se ha iniciado sesion")
        return "No se ha iniciado sesion"
    if session.get('credencial') != 12: # No es un vendedor
        flash("Error: no permitido")
        return "No permitido" # Redirigir a iniciar sesion o incio de Usuario
    if request.method == 'POST':
        nombre_insumo = request.form.get('nombre')
        if len(nombre_insumo) > 20: # type: ignore
            flash("Error: nombre sobrepasa los 20 caracteres")
            return redirect(url_for('inventario.inventario'))
        descripcion_insumo = request.form.get('descripcion')
        if len(descripcion_insumo) > 100: # type: ignore
            flash("Error: nombre sobrepasa los 100 caracteres")
            return redirect(url_for('inventario.inventario'))
        costo_insumo = request.form.get('costo')
        piezas_insumo = request.form.get('piezas')
        insertaInsumo(nombre_insumo, descripcion_insumo, costo_insumo, piezas_insumo)
        flash("Insumo agregado con éxito")
        return redirect(url_for('inventario.inventario'))
    else:
        return render_template('realizar_inventario/agregar_insumo.html')
  
@inventario_bp.route('/inventario', methods=['POST'])
def read_insumos():
    session = db.session
    insumos = session.query(Insumo).all()
    return render_template('realizar_inventario/inventario_insumo.html', insumos=insumos)
