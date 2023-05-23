from alchemyClasses.db import db

from controllers.controller_inventario import inventario_bp
from controllers.controller_pedido import pedido_bp
from controllers.controller_venta import venta_bp

from flask import Flask, redirect, url_for, session

app = Flask(__name__, instance_relative_config=True)
app.register_blueprint(inventario_bp)
app.register_blueprint(pedido_bp)
app.register_blueprint(venta_bp)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://4town:turningred@localhost:3306/4town'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.from_mapping(
    SECRET_KEY = 'dev'
)
db.init_app(app)

@app.route('/', methods = ['POST','GET'])
def index():
    ###
    # Caso de uso realizar inventario
    session['usuario'] = 'Ejemplo'
    session['venta'] = 'si'
    return redirect(url_for('inventario.inventario'))
    ###
    # Caso de uso hacer pedido
    # session['usuario'] = 2
    # session['producto'] = 8
    # return redirect(url_for('pedido.pedido'))
    ###
    # Caso de uso reportar venta
    # session['usuario'] = 1
    # session['venta'] = 'si'
    # return redirect(url_for('venta.venta'))

if __name__ == '__main__':
    app.run(host = "localhost", port = 8000, debug = True)