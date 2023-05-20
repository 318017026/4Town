from Producto import *

class Bebida(Producto):

    def __init__(self, costo, descripción, id, nombre_prod, ventas):
        super().__init__(costo, descripción, id, nombre_prod)
        self.id=id
        self.ventas=ventas

    def agregar_bebida(self):

        super().agregar_producto()

        conexion = mysql.connector.connect(
            host="localhost",
            user="usuario_db",
            password="contrasena_db",
            database="ingsoft"
        )

        cursor = conexion.cursor()

        sql = "INSERT INTO Bebida (id, ventas) VALUES (%s, %s)"
        valores = (self.id, self.ventas)
        cursor.execute(sql, valores)

        conexion.commit()

        cursor.close()
        conexion.close()

