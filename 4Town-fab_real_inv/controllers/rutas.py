from flask import Blueprint, render_template, request, redirect, url_for, flash
#from models.clientes import Cliente, Usuario, Credencial
from alchemyClasses import Cliente, Usuario, Credencial
from alchemyClasses.Cliente import Cliente
from alchemyClasses.Usuario import Usuario
from alchemyClasses.Credencial import Credencial
from alchemyClasses.__init__ import db
import mysql.connector

clientes = Blueprint('clientes', __name__)

@clientes.route("/menucliente")
def home():
    usuarios = Usuario.query.all()

    return render_template('index.html', usuarios=usuarios)

@clientes.route("/crear_cliente", methods=['POST'])
def addclient():
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
    n = totalregistros()

    nuevo_usuario = Usuario(n, nombre, apellidoP, apellidoM, fecha, correo, contra, True, n)
    nuevo_cliente = Cliente(n, direcc, infoenv, tarj, numtel) 
    credencial = Credencial(n, "Cliente")
    
    db.session.add(credencial)

    db.session.commit()

    db.session.add(nuevo_usuario)

    db.session.commit()

    db.session.add(nuevo_cliente)
    
    db.session.commit()
    
    flash("Cliente añadido satisfactoriamente")
    
    return redirect(url_for('clientes.home'))

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

        return redirect(url_for('clientes.home'))

    return render_template('actualizarDatos.html', users=users, clientes=clientes)

@clientes.route("/eliminar/<id>")
def deleteclient(id):
    user = Usuario.query.get(id)
    client = Cliente.query.get(id)
    db.session.delete(client)
    db.session.delete(user)
    db.session.commit()

    flash("Cliente eliminado satisfactoriamente")

    return redirect(url_for('clientes.home'))

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
