from controllers.__init__ import request,render_template, redirect, url_for, flash, mysql, Blueprint, db, session
from controllers.__init__ import Usuario, Cliente, Credencial, getUserByName # type: ignore

clientes = Blueprint('clientes', __name__)


@clientes.route("/crear_cliente", methods=['GET','POST']) # type: ignore
def addclient():
    if request.method == "POST":
        nombre = request.form['nombre']
        apellidoP = request.form['apellidoP']
        apellidoM = request.form['apellidoM']
        fecha = request.form['fechaNac']
        correo = request.form['correo']
        contra = request.form['contra']
        direcc = request.form['direcc']
        infoenv = request.form['infoenv']
        tarj = request.form['tarj']
        numtel = request.form['numtel']
        nuevo_usuario = Usuario(username=nombre,nombre=nombre, apellidoP=apellidoP, apellidoM=apellidoM, fechaNacimiento=fecha, correo=correo, contrasena=contra, estatusSesion=True, credencial=10)
        db.session.add(nuevo_usuario)
        db.session.commit()
        user = getUserByName(name=nombre, password=contra)
        if user is not None:
            print(user.id)
            nuevo_cliente = Cliente(user.id, direcc, infoenv, tarj, numtel) 
            db.session.add(nuevo_cliente)
            db.session.commit()
            session["usuario"]= user.id
            session["credencial"]=user.credencial
            flash("Cliente añadido satisfactoriamente")
            return render_template("Cliente/layout.html", id_user = user.id)
    else:
        return render_template("partials/formulario.html")

@clientes.route("/actualizar/<id>", methods = ['POST', 'GET'])
def updateclient(id):
    users = Usuario.query.get(id)
    clientes = Cliente.query.get(id)
    if request.method == "POST":
        users.nombre = request.form['nombre']
        users.apellidoP = request.form['apellidoP']
        users.apellidoM = request.form['apellidoM']
        users.fecha = request.form['fechaNac']
        users.correo = request.form['correo']
        users.contra = request.form['contra']
        clientes.direcc = request.form['direcc']
        clientes.infoenv = request.form['infoenv']
        clientes.tarj = request.form['tarj']
        clientes.numtel = request.form['numtel']
        db.session.commit()
        flash("Datos del cliente actualizados")
        return redirect(url_for('cliente'))
    return render_template('Cliente/actualizarDatos.html', users=users, clientes=clientes)

@clientes.route("/eliminar/<int:id>")
def deleteclient(id):
    user = Usuario.query.get(id)
    client = Cliente.query.get(id)
    db.session.delete(client)
    db.session.delete(user)
    db.session.commit()
    flash("Cliente eliminado satisfactoriamente")
    return redirect(url_for('login.login'))

def totalregistros():
    conexion = conexionBD()
    mycursor = conexion.cursor(dictionary=True)
    query = ("SELECT * FROM Usuario")
    mycursor.execute(query)
    data = mycursor.fetchall()
    mycursor.close()
    conexion.close()
    total = mycursor.rowcount
    return total+1

def conexionBD():
    mybd = mysql.connector.connect(
        host ="localhost",
        user ="root",
        passwd ="Intheend18*",
        database = "ingsoft"
        )
    return mybd

@clientes.route("/perfil/<int:id>")
def readclient(id):
    user_id = session.get("usuario")
    users = Usuario.query.get(id)
    clientes = Cliente.query.get(id)
    return render_template('Cliente/mostrarDatos.html', users=users, clientes=clientes)
