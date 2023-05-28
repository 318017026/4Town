from models.__init__ import Bebida, db, OperationalError

'''
Función que dado un 'id' obtiene el registro de la base de datos
Nota: Contiene validaciones.
'''
def obtener_bebida_por_id(id):
    if estatus_conexion():
        row = Bebida.query.filter(Bebida.id == id).first()
        if row is not None:
            print(f"EXITO: Se encontro registro {row}. -Modelo CRUD Bebida.")
            return row
        else:
            print("ERROR: No se encontro el registro -Modelo CRUD Bebida.")
        return None
    else:
        return None
'''
Función obtiene todos los registros de la tabla Bebida
Nota: Contiene validaciones.
'''
def obtener_bebidas():
    if estatus_conexion():
        rows = Bebida.query.all()
        # Verificar si la lista de resultados no está vacía
        if len(rows) > 0:
            print('EXITO: La consulta ha sido exitosa. Se han encontrado {} resultados.  -Modelo CRUD Bebida.'.format(len(rows)))
        else:
            print('ALERTA: La consulta no ha producido resultados.  -Modelo CRUD Bebida.')
        return rows;
    else:
        return None

'''
Función que dado un 'id', lo busca y elimina de la base de datos
Nota: Contiene validaciones.
'''
def eliminar_bebida(id):
    if estatus_conexion():
        session = db.session
        # Buscar el producto que deseamos eliminar
        row = session.query(Bebida).filter_by(id=id).first()
        #row = Bebida.query.get(id)
        if row is not None:
            # Eliminar el producto
            session.delete(row)
            # Confirmar la transacción
            try:
                session.commit()
                print('EXITO: El registro se ha eliminado correctamente. -Modelo CRUD Bebida.')
            except Exception as e:
                session.rollback()
                print('ERROR: Ha ocurrido un error al eliminar el registro: {} -Modelo CRUD Bebida.'.format(str(e)))
            finally:
                session.close()
        else:
            print('ERROR: El producto que deseas eliminar no existe. -Modelo CRUD Bebida.')
    

'''
Función que actualiza un registro dados los parámetros
Nota: Contiene validaciones.
'''
def actualizar_bebida(id, nombre, descripcion, costo, ventas):
    if estatus_conexion():
        # Crear un objeto session
        session = db.session
        row = session.query(Bebida).filter_by(id=id).first()
        if row is not None:
            # Actualizar el registro
            row.nombre = nombre
            row.descripcion = descripcion
            row.costo = abs(float(costo))
            row.ventas = abs(int(ventas))
            try:
                # Confirmar la transacción
                session.add(row)
                session.commit()
                print('EXITO: El registro se ha actualizado correctamente. -Modelo CRUD Bebida.')
            except Exception as e:
                # Si ocurre algún error, deshacemos las transacciones no confirmadas
                session.rollback()
                print('ERROR: Ha ocurrido un error al actualizar el registro: {} -Modelo CRUD Bebida.'.format(str(e)))
            finally:
                session.close()
        else:
            print('ERROR: El producto que deseas actualizar no existe. -Modelo CRUD Bebida.')
 
'''
Función que inserta un registro en la base de datos.
Nota: Contiene Validaciones.
'''   
def agregar_bebida(n, desc, cos, vent=0):
    if estatus_conexion():
        new_row = Bebida(nombre=n, descripcion=desc, costo=abs(float(cos)), ventas=vent)
        session = db.session
        try:
            session.add(new_row)
            # Confirmar la transacción
            session.commit()
            print('EXITO: El registro se ha insertado correctamente. -Modelo CRUD Bebida.')
        except Exception as e:
            # Si ocurre algún error, deshacemos las transacciones no confirmadas
            session.rollback()
            print('ERROR: Ha ocurrido un error al insertar el registro: {} -Modelo CRUD Bebida.'.format(str(e)))
        finally:
            session.close()
        
'''
Función que verifica la conexión a la base de datos
'''
def estatus_conexion():
    session = db.session
    try:
        # Realizar una consulta a la tabla Product
        products = session.query(Bebida).all()
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