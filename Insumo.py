from Producto import *

class Insumo(Producto):

    def __init__(self, costo, descripción, id, nombre_prod, piezas):
        super.__init__(costo, descripción, id, nombre_prod)
        self.id=id
        self.piezas=piezas

    def agregar_insumo(self):

        super().agregar_producto()

        conexion = mysql.connector.connect(
            host="localhost",
            user="usuario_db",
            password="contrasena_db",
            database="ingsoft"
        )

        cursor = conexion.cursor()

        sql = "INSERT INTO Insumo (id, piezas) VALUES (%s, %s)"
        valores = (self.id, self.piezas)
        cursor.execute(sql, valores)

        conexion.commit()

        cursor.close()
        conexion.close()