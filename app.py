from alchemyClasses.db import db

from controllers.controller_inventario import inventario_bp

from flask import Flask, redirect, url_for, session

app = Flask(__name__, instance_relative_config=True)
app.register_blueprint(inventario_bp)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://4town:turningred@localhost:3306/4town'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.from_mapping(
    SECRET_KEY = 'dev'
)
db.init_app(app)

@app.route('/', methods = ['POST','GET'])
def index():
    session['usuario'] = 'Ejemplo'
    session['ventas'] = 'si'
    return redirect(url_for('inventario.inventario'))

if __name__ == '__main__':
    app.run(host = "localhost", port = 8000, debug = True)