# Importaciones generales (Flask)
from __init__ import Flask, render_template, redirect, url_for, g, session, db
# Importaciones de Controlador Bebida
from __init__  import createBluePrint, readBluePrint, deleteBluePrint, updateBluePrint
# Importaciones de Controlador Usuario
from __init__  import loginBluePrint
# Importaciones de Controlador Inventario
from __init__  import inventario_bp
# Importaciones de Controlador Hacer Pedido
from __init__  import pedido_bp
# Importaciones de Controlador Monitorear Estatus
from __init__  import status_pedido_bp
# Importaciones de Controlador Reportes de Venta
from __init__  import venta_bp
# Importaciones de Controlador Reportes de Venta
from __init__ import clientes

# Importaciones de Controlador Vendedor
from __init__ import readSellerBluePrint, createSellerBluePrint, deleteSellerBluePrint, updateSellerBluePrint

# Instacia de apicacion
app = Flask(__name__)
# Agregacion de blueprints de Bebida
app.register_blueprint(readBluePrint)
app.register_blueprint(createBluePrint)
app.register_blueprint(deleteBluePrint)
app.register_blueprint(updateBluePrint)
# Agragacion de blueprint de clientes
app.register_blueprint(clientes)
# Agregacion de blueprint de inicio de sesion
app.register_blueprint(loginBluePrint) # type: ignore
# Agregacion de blueprint de inventario
app.register_blueprint(inventario_bp)
# Agregacion de blueprint de pedido
app.register_blueprint(pedido_bp)
app.register_blueprint(status_pedido_bp)
# Agregacion de blueprint de venta
app.register_blueprint(venta_bp)
# Agregacion de blueprint de administracionVendedor
app.register_blueprint(readSellerBluePrint)
app.register_blueprint(createSellerBluePrint)
app.register_blueprint(deleteSellerBluePrint)
app.register_blueprint(updateSellerBluePrint)





# Confuguracion de la app
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost:3306/ingsoft'
app.config.from_mapping(
    SECRET_KEY='dev'
)

# Rutas principales
@app.route('/')
def log():
    return redirect(url_for("login.login"))

@app.route("/administrador")
def administrador():
    user = session.get("usuario")
    return render_template("Administrador/main_admin.html", id_user=user)

@app.route("/vendedor")
def vendedor():
    user = session.get("usuario")
    return render_template("Vendedor/main_vendedor.html", id_user=user)

@app.route("/cliente")
def cliente():
    user = session.get("usuario")
    return render_template("Cliente/layout.html", id_user=user)

# Inicializacion de la app
db.init_app(app)    
app.run(host="0.0.0.0", port=3000, debug=True)