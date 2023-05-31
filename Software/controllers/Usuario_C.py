from controllers.__init__ import Blueprint, render_template, request, getUserByName, getUserByEmail, flash, get_flashed_messages
from controllers.__init__ import getCrendential, session, g,  url_for, redirect, re, dominios_validos, deactivate_user, activate_user

# Declaracion de blueprint de inicio de sesion
loginBluePrint = Blueprint("login", __name__, url_prefix="/login") # type: ignore

@loginBluePrint.route("/login", methods = ["GET", "POST"])# type: ignore
def login():
    if request.method == "POST":
        userOrEmail = request.form['username']
        password =  request.form['password']
        userOrEmail = userOrEmail.strip()
        password = password.strip()
        if verify_email(userOrEmail,dominios_validos):
            usuario = getUserByEmail(email=userOrEmail, password=password)
            if usuario is None:
                flash('El correo o contraseña no están vinculados a ninguna cuenta.')
                return render_template("inicio_sesion/log.html", mensajes = get_flashed_messages())
            else:
                print("Estatus:" , usuario.estatusSesion)
                if usuario.estatusSesion:
                    flash('Esta sesión ya se encuentra abierta. Cierrala en tu navegador si deseas ingresar.')
                    return render_template("inicio_sesion/log.html", mensajes = get_flashed_messages())
                session['usuario']=usuario.id
                session['credencial']=usuario.credencial
                g.user = usuario
                activate_user(usuario.id)
                return render_template(getCrendential(usuario), id_user=usuario.id)
        else:
            usuario = getUserByName(name=userOrEmail, password=password)
            if usuario is None:
                flash('El usuario o contraseña no están vinculados a ninguna cuenta.')
                return render_template("inicio_sesion/log.html", mensajes = get_flashed_messages())
            else:
                if usuario.estatusSesion:
                    flash('Esta sesión ya se encuentra abierta. Cierrala en tu navegador si deseas ingresar.')
                    return render_template("inicio_sesion/log.html", mensajes = get_flashed_messages())
                session['usuario']=usuario.id
                session['credencial']=usuario.credencial
                g.user = usuario
                activate_user(usuario.id)
                return render_template(getCrendential(usuario), id_user=usuario.id)
    else:
        close_session(session=session)
        return render_template("inicio_sesion/log.html")
    
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

'''
    Funcion para limpiar y cerrar la sesion
'''
def close_session(session):
    if session.get("usuario") is not None:
        deactivate_user(session.get("usuario"))
    session.clear() 