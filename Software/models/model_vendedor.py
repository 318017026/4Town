from models.__init__ import Vendedor, Usuario, db

'''
Función obtiene todos los registros de la tabla Usuario
Nota: Contiene validaciones.
'''
def obtener_vendedores():
    session = db.session 
    rows = session.query(Usuario).join(Vendedor).all()
    return rows

def eliminar_vendedor(id):
    session = db.session
    # Buscar el producto que deseamos eliminar
    row = session.query(Vendedor).filter_by(id=id).first()
    if row is not None:
        # Eliminar el producto
        session.delete(row)
        # Confirmar la transacción
        try:
            session.commit()
            print('EXITO: El registro se ha eliminado correctamente. -Modelo CRUD Vendedor.')
        except Exception as e:
            session.rollback()
            print('ERROR: Ha ocurrido un error al eliminar el registro: {} -Modelo CRUD Vendedor.'.format(str(e)))
        finally:
            session.close()
    else:
        print('ERROR: El producto que deseas eliminar no existe. -Modelo CRUD Vendedor.')


def obtener_vendedor_por_id(id):
    row = Usuario.query.filter(Usuario.id == id).first()
    if row is not None:
        print(f"EXITO: Se encontro registro {row}. -Modelo CRUD Vendedor.")
        return row
    else:
        print("ERROR: No se encontro el registro -Modelo CRUD Vendedor.")
    return None


def actualizar_vendedor(id, nombre, username, apellidoP, apellidoM, fechaNac, correo, contra):
    print(nombre)
    session = db.session
    row = session.query(Usuario).filter_by(id=id).first()
    if row is not None:
        # Actualizar el registro
        row.nombre = nombre
        row.username = username
        row.apellidoP = apellidoP
        row.apellidoM = apellidoM
        row.fechaNac = fechaNac
        row.correo = correo
        row.contra = contra
        try:
            # Confirmar la transacción
            session.add(row)
            session.commit()
            print('EXITO: El registro se ha actualizado correctamente. -Modelo CRUD Vendedor.')
        except Exception as e:
            # Si ocurre algún error, deshacemos las transacciones no confirmadas
            session.rollback()
            print('ERROR: Ha ocurrido un error al actualizar el registro: {} -Modelo CRUD Vendedor.'.format(str(e)))
        finally:
            session.close()
    else:
        print('ERROR: El producto que deseas actualizar no existe. -Modelo CRUD Vendedor.')