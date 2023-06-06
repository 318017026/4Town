from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

    
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Pa55word'
app.config['MYSQL_DB'] = 'ingsoft'#'Templete_DB'
mysql = MySQL(app)

#Muestra las opciones de consulta en la pestaña consultar cliente
@app.route('/consultar_cliente')
def consultar_cliente():
    try:
        cursor=mysql.connection.cursor()
        cursor.execute('SELECT (nombre, apellidoP, apellidoM, fechaNacimiento, correo, direccion) FROM (Usuario JOIN Cliente)')
        result = cursor.fetchall()
        if result == []:
            return 'No existen clientes en este momento'
        else: 
            return render_template('consultar_cliente.html', results=result)
    except Exception as e:
        return 'Lo sentimos, ocurrió un error, intente de nuevo más tarde.  \n Error: '+ str(e)

        
#Realiza la consulta del cliente tomando en cuenta el nombre
@app.route('/consultar_cliente', methods=['POST'])
def consultar_cliente_nombre():
    try:
        if request.method == 'POST':
            nombre=request.form['nombre']  
            cursor=mysql.connection.cursor()
            cursor.execute('SELECT (nombre, apellidoP, apellidoM, fechaNacimiento, correo, direccion) FROM (Usuario JOIN Cliente) WHERE (nombre= %s)',(nombre))
            result=cursor.fetchall()
            if result == []:
                return "No se encontró ningún cliente con los datos ingresados. \n Si cree que se trata de un error revise los datos ingresados e intente de nuevo. "
            else:
                return render_template('consultar_cliente.html', results=result)
    except Exception as e: 
        print("Lo sentimos, ocurrió un error: ", e)

#Realiza la consulta del cliente tomando en cuenta el apellido paterno
@app.route('/consultar_cliente', methods=['POST'])
def consultar_cliente_apellidoP():
    try:
        if request.method == 'POST':
            apellidoP=request.form['apellidoP']        
            cursor=mysql.connection.cursor()
            cursor.execute('SELECT (nombre, apellidoP, apellidoM, fechaNacimiento, correo, direccion) FROM (Usuario JOIN Cliente) WHERE (apellidoP=%s)',(apellidoP))
            result=cursor.fetchall()
            if result == [] :
                return "No se encontró ningún cliente con los datos ingresados. \n Si cree que se trata de un error revise los datos ingresados e intente de nuevo. "
            else:
                return render_template('consultar_cliente.html', results=result)
    except TypeError as type_e:
        return "Lo sentimos, ocurrió un error: ", type_e
    except Exception as e:
        return "Lo sentimos, ocurrió un error: ", e

#Realiza la consulta del cliente tomando en cuenta su edad
@app.route('/consultar_cliente', methods=['POST'])
def consultar_cliente_edad():
    try:
        if request.method == 'POST':
            edad=request.form['edad']        
            cursor=mysql.connection.cursor()
            cursor.execute('SELECT (nombre, apellidoP, apellidoM, fechaNacimiento, correo, direccion) FROM (Usuario JOIN Cliente) WHERE (DATEDIFF(YEAR, fechaNacimiento, GETDATE())=%s)',(edad))
            result=cursor.fetchall()
            if result == []:
                return "No se encontró ningún cliente con los datos ingresados. \n Si cree que se trata de un error revise los datos ingresados e intente de nuevo. "
            else:
                return render_template('consultar_cliente.html', results=result)
    except Exception as e:
        print ("Lo sentimos, ocurrió un error:", e)

app.run(port=80, debug=True)
