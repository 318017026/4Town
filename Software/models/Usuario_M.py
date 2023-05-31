from models.__init__ import Usuario, db, OperationalError

'''
Funcion que consulta la base de datos para obtener el registro de un usuario a partir de su correo y su contraseña.
Nota: Retorna el objeto usuario.
email es de tipo str
password es de tipo str
'''
def getUserByEmail(email,password):
    if estatus_conexion():
        usuario = Usuario.query.filter_by(correo=email, contrasena=password).first()
        if usuario is not None:
            return usuario
        else:
            print(f"ERROR: El Usuario no fue encontrado - Modelo Usuario")
            return None
    else: 
        return None
    
'''
Funcion que consulta la base de datos para obtener el registro de un usuario a partir de su nombre
de usuario y su contraseña.
Nota: Retorna el objeto usuario.
name es de tipo str
password es de tipo str
'''
def getUserByName(name,password):
    if estatus_conexion():
        usuario = Usuario.query.filter_by(username=name, contrasena=password).first()
        if usuario is not None:
            return usuario
        else:
            print(f"ERROR: El Usuario no fue encontrado - Modelo Usuario")
            return None
    else: 
        return None
    
'''
Funcion que consulta a la base de datos para obtener el registro de un usuario
dado un id.
Nota: Retorna un objeto usuario.
id es de tipo INTEGER
'''
def getUserByID(id):
    if estatus_conexion():
        usuario = Usuario.query.filter_by(id=id).first()
        if usuario != None:
            return usuario
        else:
            print(f"ERROR: El Usuario no fue encontrado - Modelo Usuario")
            return None
    else: 
        return None
    
'''
Funcion que dado un usuario, obtiene su credencil y retorna el templemete correspondiente
'''
def getCrendential(user):
    credencial = user.credencial
    if credencial == 10:
        return "Cliente/layout.html"
    elif credencial == 11:
        return "Administrador/main_admin.html"
    elif credencial == 12:
        return "Vendedor/main_vendedor.html"
    else:
        return "None"

'''
Funcion que activa un usuario
'''
def activate_user(id):
    if estatus_conexion():
        # Crear un objeto session
        session = db.session
        row = session.query(Usuario).filter_by(id=id).first()
        if row is not None:
            # Actualizar el registro
            row.activate()
            try:
                # Confirmar la transacción
                session.add(row)
                session.commit()
                print(f'EXITO: El Usuario con id={id} ha iniciado sesion. -Modelo Usuario.')
            except Exception as e:
                # Si ocurre algún error, deshacemos las transacciones no confirmadas
                session.rollback()
                print(f'ERROR: Ha ocurrido un error al activar al Usuario con id={id} -Modelo Usuario.')
            finally:
                session.close()
        else:
            print('ERROR: El Usuario que deseas activar no existe. -Modelo Usuario.')
            
'''
Funcion que desactiva un usuario
'''
def deactivate_user(id):
    if estatus_conexion():
        # Crear un objeto session
        session = db.session
        row = session.query(Usuario).filter_by(id=id).first()
        if row is not None:
            # Actualizar el registro
            row.deactivate() 
            try:
                # Confirmar la transacción
                session.add(row)
                session.commit()
                print(f'EXITO: El Usuario con id={id} ha cerrado sesion. -Modelo Usuario.')
            except Exception as e:
                # Si ocurre algún error, deshacemos las transacciones no confirmadas
                session.rollback()
                print(f'ERROR: Ha ocurrido un error al desactivar al Usuario con id={id} -Modelo Usuario.')
            finally:
                session.close()
        else:
            print('ERROR: El Usuario que deseas desactivar no existe. -Modelo Usuario.')

'''
Función que verifica la conexión a la base de datos
'''
def estatus_conexion():
    session = db.session
    try:
        # Realizar una consulta a la tabla Product
        users = session.query(Usuario).all()
        # Si no se genera ninguna excepción, la conexión a la base de datos es exitosa
        print("Conexión a la base de datos exitosa")
        return True
    except OperationalError as e:
        # Si se genera una excepción de tipo OperationalError, significa que se ha perdido la conexión a la base de datos
        print("Error de conexión a la base de datos:", str(e))
        return False
    finally:
        # Cerrar la sesión de SQLAlchemy
        session.close()
    