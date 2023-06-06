from controllers.__init__ import Blueprint, redirect, render_template, url_for, request, agregar_bebida, estatus_conexion, db, flash
from controllers.__init__ import obtener_bebidas, eliminar_bebida, actualizar_bebida, session, obtener_vendedores, eliminar_vendedor, obtener_vendedor_por_id, actualizar_vendedor
from controllers.__init__ import Usuario, getUserByName, Vendedor

# Declaracion de Blueprints
createSellerBluePrint = Blueprint("createSeller", __name__, url_prefix="/create_seller")
readSellerBluePrint = Blueprint("readSellers",__name__,url_prefix="/read_seller")
updateSellerBluePrint = Blueprint("updateSeller", __name__, url_prefix="/update_seller")
deleteSellerBluePrint = Blueprint("deleteSeller",__name__, url_prefix="/delete_seller")

@createSellerBluePrint.route("/create_seller", methods=["GET","POST"])# type: ignore
def create_seller():
    if request.method == "POST":
        nombre = request.form['nombre']
        apellidoP = request.form['apellidoP']
        apellidoM = request.form['apellidoM']
        fecha = request.form['fechaNac']
        correo = request.form['correo']
        contra = request.form['contra']
        nuevo_usuario = Usuario(username=nombre,nombre=nombre, apellidoP=apellidoP, apellidoM=apellidoM, fechaNacimiento=fecha, correo=correo, contrasena=contra, estatusSesion=True, credencial=12)
        db.session.add(nuevo_usuario)
        db.session.commit()
        user = getUserByName(name=nombre, password=contra)
        if user is not None:
            print(user.id)
            nuevo_vendedor = Vendedor(user.id) 
            db.session.add(nuevo_vendedor)
            db.session.commit()
            session["usuario"]= user.id
            session["credencial"]=user.credencial
            flash("Vendedor añadido satisfactoriamente")

            vendedores = obtener_vendedores()
            return render_template("Vendedor/index_administrar_vendedores.html", vendedores=vendedores)
    else:
        return render_template("Vendedor/formulario_nuevo_vendedor.html")
    
@readSellerBluePrint.route('/read_seller', methods=["GET","POST"]) # type: ignore
def read_seller():
    if estatus_conexion:
        vendedores = obtener_vendedores()
        return render_template("Vendedor/index_administrar_vendedores.html", vendedores=vendedores)
        
@deleteSellerBluePrint.route("/delete_seller/<int:id>",methods=["GET","POST"])# type: ignore
def delete_seller(id):
    if estatus_conexion:
        eliminar_vendedor(id)
        return redirect(url_for('readSellers.read_seller'))

   
@updateSellerBluePrint.route("/update_seller/<int:id>", methods=["GET","POST"])# type: ignore
def update_seller(id):
    row = obtener_vendedor_por_id(id)
    if estatus_conexion:
        if request.method == "POST":
            nombre = request.form['nombre']
            username = request.form['username']
            apellidoP = request.form['apellidoPa']
            apellidoM = request.form['apellidoMa']
            fecha = request.form['fechaNacimiento']
            correo = request.form['correo']
            contra = request.form['contrasena']

            nombre = row.nombre if nombre=='' else nombre
            username = row.username if username=='' else username
            apellidoP = row.apellidoP if apellidoP=='' else apellidoP
            apellidoM = row.apellidoM if apellidoM=='' else apellidoM
            fecha = row.fechaNacimiento if fecha=='' else fecha
            correo = row.correo if correo=='' else correo
            contra = row.contrasena if contra=='' else contra 

            actualizar_vendedor(id, nombre, username, apellidoP, apellidoM, fecha, correo, contra)

            return redirect(url_for('readSellers.read_seller'))
        else:
            return render_template("Vendedor/edit_vendedor.html", id_p=id, nombre_p=row.nombre, username_p=row.username, apellido_Pa_p=row.apellidoP, 
                                    apellido_Ma_p=row.apellidoM, fecha_Nacimiento_p = row.fechaNacimiento, correo_p=row.correo, contra_p=row.contrasena)