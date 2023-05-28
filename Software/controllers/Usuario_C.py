from controllers.__init__ import Blueprint, render_template, request, getUserByName, getUserByEmail, flash, get_flashed_messages
from controllers.__init__ import getCrendential, session, g,  url_for, redirect, re, dominios_validos, deactivate_user, activate_user

# Declaracion de blueprint de inicio de sesion
loginBluePrint = Blueprint("login", __name__, url_prefix="/login") # type: ignore

@loginBluePrint.route("/login", methods = ["GET", "POST"])# type: ignore
def login():
    if session.get("user_id") is not None:
        deactivate_user(session.get("user_id"))
    session.clear() 
    if request.method == "POST":
        userOrEmail = request.form['username']
        password =  request.form['password']
        userOrEmail = userOrEmail.strip()
        password = password.strip()
        if verify_email(userOrEmail,dominios_validos):
            usuario = getUserByEmail(email=userOrEmail,password=password)
            if usuario is None:
                flash('El correo o contraseña no están vinculados a ninguna cuenta.')
                #print(f"ERROR: El usuario no fue encontrado - Usuario Controlador")
                return render_template("log.html", mensajes = get_flashed_messages())
            else:
                #Se activa al usuario
                session['user_id']=usuario.id
                g.user = usuario
                activate_user(usuario.id)
                ## Si es admin redirecionamos, no renderizamos
                if usuario.credencial==11:
                    return redirect(url_for("readDrink.read"))
                return render_template(getCrendential(usuario), nombre = usuario.nombre)
        else:
            usuario = getUserByName(name=userOrEmail,password=password)
            if usuario is None:
                flash('El usuario o contraseña no están vinculados a ninguna cuenta.')
                #print(f"ERROR: El usuario no fue encontrado - Usuario Controlador")
                return render_template("log.html", mensajes = get_flashed_messages())
            else:
                session['user_id']=usuario.id
                g.user = usuario
                activate_user(usuario.id)
                ## Si es admin redirecionamos, no renderizamos
                if usuario.credencial==11:
                    return redirect(url_for("readDrink.read"))
                return render_template(getCrendential(usuario), nombre = usuario.nombre)
    else:
        return render_template("log.html")
    
'''
Funcion que verifica si un correo es valido
'''
def verify_email(correo, dominios_validos):
    # Expresión regular para verificar el formato del correo electrónico
    patron_correo = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(patron_correo, correo):
        return False  # El formato del correo no es válido
    # Extraer el dominio del correo electrónico
    dominio = correo.split('@')[1]
    if dominio not in dominios_validos:
        return False  # El dominio no es válido
    return True  # El correo electrónico es válido