from models.__init__ import db, Venta, Pedido, Bebida, OperationalError, VentaEliminados # type: ignore

"""
Función que registra una venta en la base de datos
"""
def generaVenta(id_pedido, id_bebida):
    venta = Venta(id_pedido, id_bebida)
    db.session.add(venta)
    db.session.commit()

"""
Función que registra una lista de bebidas para crear una venta para cada una de ellas 
"""
def generaVentas(id_pedido, id_bebidas):
    for id in id_bebidas:
        db.session.add(Venta(id_pedido, id))
    db.session.commit()

#def consultar_reporte_venta():
    #result = db.session.query(Venta, Pedido, Bebida, Producto).join(Pedido).join(Bebida).join(Producto).all()
    #return result
'''
Función que obtiene la información de la tabla Venta de la base de datos
Nota: Contiene validaciones.
'''
def obtener_ventas():
    if estatus_conexion():
        rows_Venta = Venta.query.all()
        if rows_Venta is not None:
            return rows_Venta
        else:
            print("ERROR: No se encontró ningún reporte de venta.")
            return None
    else:
        return None
    
'''
Función que obtiene la información de la tabla Venta de la base de datos
Nota: Contiene validaciones.
'''
def obtener_ventas_eliminados():
    if estatus_conexion():
        rows_VentaEliminados = VentaEliminados.query.all()
        if rows_VentaEliminados is not None:
            return rows_VentaEliminados
        else:
            print("ERROR: No se encontró ningún reporte de venta.")
            return None
    else:
        return None

'''
Función que verifica la conexión a la base de datos
'''   
def estatus_conexion():
    session = db.session
    try:
        # Realizar una consulta a la tabla Venta
        ventas = session.query(Venta).all()
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