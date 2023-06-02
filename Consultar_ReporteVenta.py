from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Pa55word'
app.config['MYSQL_DB'] = 'Templete_DB'
mysql = MySQL(app)

@app.route('/consultar_reporteVenta')
def consultar_reporte():
    return render_template('consultar_reporteVenta.html')

@app.route('/consultar_reporteVenta', methods=['POST'])
def consultar_reporteVenta():

    if request.method == 'POST':       
        cursor=mysql.connection.cursor()
        cursor.execute('SELECT * FROM (Venta JOIN Pedido JOIN Bebida JOIN Producto)')
        result=cursor.fetchall()
        return render_template('consultar_reporteVenta.html', results=result)