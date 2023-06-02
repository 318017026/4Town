from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'eA20052014'
app.config['MYSQL_DB'] = 'Templete_DB'
mysql = MySQL(app)

@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/consultar_cliente')
def consultar_cliente():
    return render_template('index.html')

@app.route('/consultar_cliente_nombre', methods=['POST'])
def consultar_cliente_nombre():
    if request.method == 'POST':
        nombre=request.form['nombre']        
        cursor=mysql.connection.cursor()
        cursor.execute('SELECT * FROM (Usuario JOIN Cliente) WHERE (nombre='+nombre+')')
        print(nombre)
        return 'Los datos del cliente son los siguientes:'

@app.route('/consultar_cliente_apellidoP', methods=['POST'])
def consultar_cliente_apellidoP():
    if request.method == 'POST':
        apellidoP=request.form['apellidoP']        
        cursor=mysql.connection.cursor()
        cursor.execute('SELECT * FROM Usuario WHERE (apellidoP==%s)',(apellidoP))
        mysql.connection.commit()
        return 'Los datos del cliente son los siguientes:'

@app.route('/consultar_cliente_edad', methods=['POST'])
def consultar_cliente_edad():
    if request.method == 'POST':
        edad=request.form['edad']        
        cursor=mysql.connection.cursor()
        cursor.execute('SELECT * FROM Usuario WHERE (edad)')
        print(edad)
        return 'Los datos del cliente son los siguientes:'
    

@app.route('/consultar_reporte_venta')
def consultar_reporte_venta():
    return "Consultar reporte de venta"
if __name__ == '__main__':
    app.run(port = 80, debug = True)
