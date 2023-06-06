from controllers.__init__ import request,render_template, redirect, url_for, flash, mysql, Blueprint, db, session
from controllers.__init__ import Usuario, Cliente, getUserByName # type: ignore
import re

clientes = Blueprint('clientes', __name__)

# Clase auxiliar para formato adecuado de fechas
class fecha():
    def __init__(self, dia, mes, año):
        dian = int(dia)
        if dian <= 9:
            dia = "0" + str(dian)
        mesn = int(mes)
        if mesn <= 9:
            mes = "0" + str(mesn)
        self.dia = dia
        self.mes = mes
        self.año = año

@clientes.route("/crear_cliente", methods=['GET','POST']) # type: ignore
def addclient():
    if request.method == "POST":
        # Validación para día
        dia = request.form['diaNac']
        if not re.match(r'^\d{2}$', dia):
            flash("El día de nacimiento debe contener exactamente 2 números")
            # Guardar datos para su correcion
            nombre = request.form['nombre']
            apellidoP = request.form['apellidoP']
            apellidoM = request.form['apellidoM']
            dia = request.form['diaNac']
            mes = request.form['mesNac']
            año = request.form['anioNac']
            correo = request.form['correo']
            contra = request.form['contra']
            direcc = request.form['direcc']
            infoenv = request.form['infoenv']
            tarj = request.form['tarj']
            numtel = request.form['numtel']
            # Redireccion para corregir datos
            return render_template("partials/formulario.html", nombre=nombre, apellidoP= apellidoP, apellidoM=apellidoM, diaNac=dia, mesNac=mes, anioNac=año,
                                   correo=correo, contra=contra, direcc=direcc, infoenv=infoenv, tarj=tarj, numtel=numtel)
        if not (1 <= int(dia) <= 31):
            flash("El día de nacimiento debe estar entre 1 y 31")
            # Guardar datos para su correcion
            nombre = request.form['nombre']
            apellidoP = request.form['apellidoP']
            apellidoM = request.form['apellidoM']
            dia = request.form['diaNac']
            mes = request.form['mesNac']
            año = request.form['anioNac']
            correo = request.form['correo']
            contra = request.form['contra']
            direcc = request.form['direcc']
            infoenv = request.form['infoenv']
            tarj = request.form['tarj']
            numtel = request.form['numtel']
            # Redireccion para corregir datos
            return render_template("partials/formulario.html", nombre=nombre, apellidoP= apellidoP, apellidoM=apellidoM, diaNac=dia, mesNac=mes, anioNac=año,
                                   correo=correo, contra=contra, direcc=direcc, infoenv=infoenv, tarj=tarj, numtel=numtel)
        # Validación para mes
        mes = request.form['mesNac']
        if not re.match(r'^\d{2}$', mes):
            flash("El mes de nacimiento debe contener exactamente 2 números")
            # Guardar datos para su correcion
            nombre = request.form['nombre']
            apellidoP = request.form['apellidoP']
            apellidoM = request.form['apellidoM']
            dia = request.form['diaNac']
            mes = request.form['mesNac']
            año = request.form['anioNac']
            correo = request.form['correo']
            contra = request.form['contra']
            direcc = request.form['direcc']
            infoenv = request.form['infoenv']
            tarj = request.form['tarj']
            numtel = request.form['numtel']
            # Redireccion para corregir datos
            return render_template("partials/formulario.html", nombre=nombre, apellidoP= apellidoP, apellidoM=apellidoM, diaNac=dia, mesNac=mes, anioNac=año,
                                   correo=correo, contra=contra, direcc=direcc, infoenv=infoenv, tarj=tarj, numtel=numtel)
        if not (1 <= int(mes) <= 12):
            flash("El mes de nacimiento debe estar entre 1 y 12")
            # Guardar datos para su correcion
            nombre = request.form['nombre']
            apellidoP = request.form['apellidoP']
            apellidoM = request.form['apellidoM']
            dia = request.form['diaNac']
            mes = request.form['mesNac']
            año = request.form['anioNac']
            correo = request.form['correo']
            contra = request.form['contra']
            direcc = request.form['direcc']
            infoenv = request.form['infoenv']
            tarj = request.form['tarj']
            numtel = request.form['numtel']
            # Redireccion para corregir datos
            return render_template("partials/formulario.html", nombre=nombre, apellidoP= apellidoP, apellidoM=apellidoM, diaNac=dia, mesNac=mes, anioNac=año,
                                   correo=correo, contra=contra, direcc=direcc, infoenv=infoenv, tarj=tarj, numtel=numtel)
        # Validación para año
        año = request.form['anioNac']
        if not re.match(r'^\d{4}$', año):
            flash("El año de nacimiento debe contener exactamente 4 números")
            # Guardar datos para su correcion
            nombre = request.form['nombre']
            apellidoP = request.form['apellidoP']
            apellidoM = request.form['apellidoM']
            dia = request.form['diaNac']
            mes = request.form['mesNac']
            año = request.form['anioNac']
            correo = request.form['correo']
            contra = request.form['contra']
            direcc = request.form['direcc']
            infoenv = request.form['infoenv']
            tarj = request.form['tarj']
            numtel = request.form['numtel']
            # Redireccion para corregir datos
            return render_template("partials/formulario.html", nombre=nombre, apellidoP= apellidoP, apellidoM=apellidoM, diaNac=dia, mesNac=mes, anioNac=año,
                                   correo=correo, contra=contra, direcc=direcc, infoenv=infoenv, tarj=tarj, numtel=numtel)
        if not (1900 <= int(año) <= 2023):
            flash("El año de nacimiento debe estar entre 1900 y 2023")
            # Guardar datos para su correcion
            nombre = request.form['nombre']
            apellidoP = request.form['apellidoP']
            apellidoM = request.form['apellidoM']
            dia = request.form['diaNac']
            mes = request.form['mesNac']
            año = request.form['anioNac']
            correo = request.form['correo']
            contra = request.form['contra']
            direcc = request.form['direcc']
            infoenv = request.form['infoenv']
            tarj = request.form['tarj']
            numtel = request.form['numtel']
            # Redireccion para corregir datos
            return render_template("partials/formulario.html", nombre=nombre, apellidoP= apellidoP, apellidoM=apellidoM, diaNac=dia, mesNac=mes, anioNac=año,
                                   correo=correo, contra=contra, direcc=direcc, infoenv=infoenv, tarj=tarj, numtel=numtel)
        fecha = año + mes + dia
        correo = request.form['correo']
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', correo):
            flash("El correo electrónico ingresado no tiene un formato válido")
            # Guardar datos para su correcion
            nombre = request.form['nombre']
            apellidoP = request.form['apellidoP']
            apellidoM = request.form['apellidoM']
            dia = request.form['diaNac']
            mes = request.form['mesNac']
            año = request.form['anioNac']
            correo = request.form['correo']
            contra = request.form['contra']
            direcc = request.form['direcc']
            infoenv = request.form['infoenv']
            tarj = request.form['tarj']
            numtel = request.form['numtel']
            # Redireccion para corregir datos
            return render_template("partials/formulario.html", nombre=nombre, apellidoP= apellidoP, apellidoM=apellidoM, diaNac=dia, mesNac=mes, anioNac=año,
                                   correo=correo, contra=contra, direcc=direcc, infoenv=infoenv, tarj=tarj, numtel=numtel)
        # Realizar cambios en la base de datos
        nombre = request.form['nombre']
        apellidoP = request.form['apellidoP']
        apellidoM = request.form['apellidoM']
        contra = request.form['contra']
        direcc = request.form['direcc']
        infoenv = request.form['infoenv']
        tarj = request.form['tarj']
        numtel = request.form['numtel']
        nuevo_usuario = Usuario(username=nombre,nombre=nombre, apellidoP=apellidoP, apellidoM=apellidoM, fechaNacimiento=fecha, correo=correo, contrasena=contra, estatusSesion=True, credencial=10)
        db.session.add(nuevo_usuario)
        db.session.commit()
        # Inicio de sesion con cuenta recien creada
        user = getUserByName(name=nombre, password=contra)
        if user is not None:
            nuevo_cliente = Cliente(user.id, direcc, infoenv, tarj, numtel) 
            db.session.add(nuevo_cliente)
            db.session.commit()
            session["usuario"]= user.id
            session["credencial"]=user.credencial
            # Redireccion a pantalla principal de cliente
            flash("Cliente añadido satisfactoriamente")
            return render_template("Cliente/layout.html", id_user = user.id)
    else:
        # Redireccion a pantalla para crear usuario
        return render_template("partials/formulario.html",nombre="", apellidoP="", apellidoM="", diaNac="", mesNac="", anioNac="", correo="", contra="", direcc="", infoenv="", tarj="", numtel="")

@clientes.route("/actualizar/<id>", methods = ['POST', 'GET'])
def updateclient(id):
    users = Usuario.query.get(id)
    clientes = Cliente.query.get(id)
    fechaNac = users.fechaNacimiento.strftime("%Y-%m-%d")
    partes = fechaNac.split("-")
    # Asignar las partes a las variables correspondientes
    año = int(partes[0])
    mes = int(partes[1])
    dia = int(partes[2])
    fechacliente = fecha(dia, mes, año)
    if request.method == "POST":
        # Validación para día
        dia = request.form['diaNac']
        if not re.match(r'^\d{2}$', dia):
            # Redireccion para corregir datos
            flash("El día de nacimiento debe contener exactamente 2 números")
            return render_template('Cliente/actualizarDatos.html', users=users, clientes=clientes, fechas=fechacliente)
        if not (1 <= int(dia) <= 31):
            # Redireccion para corregir datos
            flash("El día de nacimiento debe estar entre 1 y 31")
            return render_template('Cliente/actualizarDatos.html', users=users, clientes=clientes, fechas=fechacliente)
        # Validación para mes
        mes = request.form['mesNac']
        if not re.match(r'^\d{2}$', mes):
            # Redireccion para corregir datos
            flash("El mes de nacimiento debe contener exactamente 2 números")
            return render_template('Cliente/actualizarDatos.html', users=users, clientes=clientes, fechas=fechacliente)
        if not (1 <= int(mes) <= 12):
            # Redireccion para corregir datos
            flash("El mes de nacimiento debe estar entre 1 y 12")
            return render_template('Cliente/actualizarDatos.html', users=users, clientes=clientes, fechas=fechacliente)
        # Validación para año
        año = request.form['anioNac']
        if not re.match(r'^\d{4}$', año):
            # Redireccion para corregir datos
            flash("El año de nacimiento debe contener exactamente 4 números")
            return render_template('Cliente/actualizarDatos.html', users=users, clientes=clientes, fechas=fechacliente)
        if not (1900 <= int(año) <= 2023):
            # Redireccion para corregir datos
            flash("El año de nacimiento debe estar entre 1900 y 2023")
            return render_template('Cliente/actualizarDatos.html', users=users, clientes=clientes, fechas=fechacliente)
        fechaNac = año + mes + dia
        correo = request.form['correo']
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', correo):
            # Redireccion para corregir datos
            flash("El correo electrónico ingresado no tiene un formato válido")
            return render_template('Cliente/actualizarDatos.html', users=users, clientes=clientes, fechas=fechacliente)
        # Realizar cambios en la base de datos
        users.nombre = request.form['nombre']
        users.apellidoP = request.form['apellidoP']
        users.apellidoM = request.form['apellidoM']
        users.fechaNacimiento = fechaNac
        users.correo = correo
        users.contra = request.form['contra']
        clientes.direcc = request.form['direcc']
        clientes.infoenv = request.form['infoenv']
        clientes.tarj = request.form['tarj']
        clientes.numtel = request.form['numtel']
        # Redireccion a pantalla principal del cliente
        db.session.commit()
        flash("Datos del cliente actualizados")
        return redirect(url_for('cliente'))
    # Redireccion a pantalla para actualizar datos
    return render_template('Cliente/actualizarDatos.html', users=users, clientes=clientes, fechas=fechacliente)

@clientes.route("/eliminar/<int:id>")
def deleteclient(id):
    # Obtener datos de usuario
    user = Usuario.query.get(id)
    # Obtener datos de cliente
    client = Cliente.query.get(id)
    # Realizar cambios en la base de datos
    db.session.delete(client)
    db.session.delete(user)
    db.session.commit()
    # Redireccion a pantalla de inicio de sesion
    flash("Cliente eliminado satisfactoriamente")
    return redirect(url_for('login.login'))

@clientes.route("/perfil/<int:id>")
def readclient(id):
    # Confirmar inicio de sesion
    user_id = session.get("usuario")
    # Obtener datos de usuario
    users = Usuario.query.get(id)
    # Obtener datos de cliente
    clientes = Cliente.query.get(id)
    fechaNac = users.fechaNacimiento.strftime("%Y-%m-%d")
    partes = fechaNac.split("-")
    # Asignar las partes a las variables correspondientes
    año = int(partes[0])
    mes = int(partes[1])
    dia = int(partes[2])
    # Obtener datos de fecha en formato adecuado
    fechacliente = fecha(dia, mes, año)

    # Redireccion a pantalla donde se muestran los datos del cliente
    return render_template('Cliente/mostrarDatos.html', users=users, clientes=clientes, fechas=fechacliente)


@clientes.route("/buscar", methods = ['POST', 'GET'])
def buscar():
    if request.method == 'GET':
        return render_template('buscar_cliente/buscar_cliente.html', cliente=None, users=None)
    if request.method == 'POST':
        id = request.form['Id']
        users = Usuario.query.get(id)
        cliente = Cliente.query.get(id)
        return render_template('buscar_cliente/buscar_cliente.html', cliente=cliente, users=users)

@clientes.route("/buscar_vendedor", methods = ['POST', 'GET'])
def buscar_vendedor():
    if request.method == 'GET':
        return render_template('buscar_cliente/buscar_cliente_vendedor.html', cliente=None, users=None)
    if request.method == 'POST':
        id = request.form['Id']
        users = Usuario.query.get(id)
        cliente = Cliente.query.get(id)
        return render_template('buscar_cliente/buscar_cliente_vendedor.html', cliente=cliente, users=users)