from flask import Flask
from routes.rutas import clientes
from flask_sqlalchemy import SQLAlchemy
from utils.db import *

app = Flask(__name__)

app.secret_key = "secret key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:wintermute@localhost/ingsoft'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.register_blueprint(clientes)

with app.app_context():
    db.init_app(app)
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
