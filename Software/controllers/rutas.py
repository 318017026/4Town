from controllers.__init__ import request,render_template, redirect, url_for, flash, mysql, Blueprint, db, session
from controllers.__init__ import Usuario, Cliente, Credencial, getUserByName # type: ignore
import re

clientes = Blueprint('clientes', __name__)

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
        nombre = request.form['nombre']
        apellidoP = request.form['apellidoP']
        apellidoM = request.form['apellidoM']

        # Validación para día
        dia = request.form['diaNac']
        if not re.match(r'^\d{2}$', dia):
            flash("El día de nacimiento debe contener exactamente 2 números")
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
            return render_template("partials/formulario.html", nombre=nombre, apellidoP= apellidoP, apellidoM=apellidoM, diaNac=dia, mesNac=mes, anioNac=año,
                                   correo=correo, contra=contra, direcc=direcc, infoenv=infoenv, tarj=tarj, numtel=numtel)
        if not (1 <= int(dia) <= 31):
            flash("El día de nacimiento debe estar entre 1 y 31")
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
            return render_template("partials/formulario.html", nombre=nombre, apellidoP= apellidoP, apellidoM=apellidoM, diaNac=dia, mesNac=mes, anioNac=año,
                                   correo=correo, contra=contra, direcc=direcc, infoenv=infoenv, tarj=tarj, numtel=numtel)

        # Validación para mes
        mes = request.form['mesNac']
        if not re.match(r'^\d{2}$', mes):
            flash("El mes de nacimiento debe contener exactamente 2 números")
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
            return render_template("partials/formulario.html", nombre=nombre, apellidoP= apellidoP, apellidoM=apellidoM, diaNac=dia, mesNac=mes, anioNac=año,
                                   correo=correo, contra=contra, direcc=direcc, infoenv=infoenv, tarj=tarj, numtel=numtel)
        if not (1 <= int(mes) <= 12):
            flash("El mes de nacimiento debe estar entre 1 y 12")
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
            return render_template("partials/formulario.html", nombre=nombre, apellidoP= apellidoP, apellidoM=apellidoM, diaNac=dia, mesNac=mes, anioNac=año,
                                   correo=correo, contra=contra, direcc=direcc, infoenv=infoenv, tarj=tarj, numtel=numtel)

        # Validación para año
        año = request.form['anioNac']
        if not re.match(r'^\d{4}$', año):
            flash("El año de nacimiento debe contener exactamente 4 números")
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
            return render_template("partials/formulario.html", nombre=nombre, apellidoP= apellidoP, apellidoM=apellidoM, diaNac=dia, mesNac=mes, anioNac=año,
                                   correo=correo, contra=contra, direcc=direcc, infoenv=infoenv, tarj=tarj, numtel=numtel)
        if not (1900 <= int(año) <= 2023):
            flash("El año de nacimiento debe estar entre 1900 y 2023")
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
            return render_template("partials/formulario.html", nombre=nombre, apellidoP= apellidoP, apellidoM=apellidoM, diaNac=dia, mesNac=mes, anioNac=año,
                                   correo=correo, contra=contra, direcc=direcc, infoenv=infoenv, tarj=tarj, numtel=numtel)
        
        fecha = año + mes + dia

        correo = request.form['correo']
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', correo):
            flash("El correo electrónico ingresado no tiene un formato válido")
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
            return render_template("partials/formulario.html", nombre=nombre, apellidoP= apellidoP, apellidoM=apellidoM, diaNac=dia, mesNac=mes, anioNac=año,
                                   correo=correo, contra=contra, direcc=direcc, infoenv=infoenv, tarj=tarj, numtel=numtel)
        
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
            nuevo_cliente = Cliente(user.id, direcc, infoenv, tarj, numtel) 
            db.session.add(nuevo_cliente)
            db.session.commit()
            session["usuario"]= user.id
            session["credencial"]=user.credencial
            flash("Cliente añadido satisfactoriamente")
            return render_template("Cliente/layout.html", id_user = user.id)
    else:
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
        users.nombre = request.form['nombre']
        users.apellidoP = request.form['apellidoP']
        users.apellidoM = request.form['apellidoM']
        
        # Validación para día
        dia = request.form['diaNac']
        if not re.match(r'^\d{2}$', dia):
            flash("El día de nacimiento debe contener exactamente 2 números")
            return render_template('Cliente/actualizarDatos.html', users=users, clientes=clientes, fechas=fechacliente)
        if not (1 <= int(dia) <= 31):
            flash("El día de nacimiento debe estar entre 1 y 31")
            return render_template('Cliente/actualizarDatos.html', users=users, clientes=clientes, fechas=fechacliente)

        # Validación para mes
        mes = request.form['mesNac']
        if not re.match(r'^\d{2}$', mes):
            flash("El mes de nacimiento debe contener exactamente 2 números")
            return render_template('Cliente/actualizarDatos.html', users=users, clientes=clientes, fechas=fechacliente)
        if not (1 <= int(mes) <= 12):
            flash("El mes de nacimiento debe estar entre 1 y 12")
            return render_template('Cliente/actualizarDatos.html', users=users, clientes=clientes, fechas=fechacliente)

        # Validación para año
        año = request.form['anioNac']
        if not re.match(r'^\d{4}$', año):
            flash("El año de nacimiento debe contener exactamente 4 números")
            return render_template('Cliente/actualizarDatos.html', users=users, clientes=clientes, fechas=fechacliente)
        if not (1900 <= int(año) <= 2023):
            flash("El año de nacimiento debe estar entre 1900 y 2023")
            return render_template('Cliente/actualizarDatos.html', users=users, clientes=clientes, fechas=fechacliente)

        fechaNac = año + mes + dia

        correo = request.form['correo']
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', correo):
            flash("El correo electrónico ingresado no tiene un formato válido")
            return render_template('Cliente/actualizarDatos.html', users=users, clientes=clientes, fechas=fechacliente)

        users.fechaNacimiento = fechaNac
        users.correo = correo
        users.contra = request.form['contra']
        clientes.direcc = request.form['direcc']
        clientes.infoenv = request.form['infoenv']
        clientes.tarj = request.form['tarj']
        clientes.numtel = request.form['numtel']
        
        db.session.commit()
        flash("Datos del cliente actualizados")
        return redirect(url_for('cliente'))
    return render_template('Cliente/actualizarDatos.html', users=users, clientes=clientes, fechas=fechacliente)

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
        passwd ="wintermute",
        database = "ingsoft"
        )
    return mybd

@clientes.route("/perfil/<int:id>")
def readclient(id):
    user_id = session.get("usuario")
    users = Usuario.query.get(id)
    clientes = Cliente.query.get(id)
    return render_template('Cliente/mostrarDatos.html', users=users, clientes=clientes)
        
'''       
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

'''
