from flask import Flask, render_template, redirect, url_for
from controllers.CRUD_Bebida_C import createBluePrint, readBluePrint, deleteBluePrint, updateBluePrint
from controllers.Usuario_C import loginBluePrint
from alchemy_classes.__init__ import db

app = Flask(__name__)
app.register_blueprint(readBluePrint)
app.register_blueprint(createBluePrint)
app.register_blueprint(deleteBluePrint)
app.register_blueprint(updateBluePrint)
app.register_blueprint(loginBluePrint) # type: ignore

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Intheend18*@localhost:3306/ingsoft'
app.config.from_mapping(
    SECRET_KEY='dev'
)

@app.route('/')
def log():
    return redirect(url_for("login.login"))
    #return render_template("log.html")


db.init_app(app)    
app.run(host="0.0.0.0", port=3000, debug=True)