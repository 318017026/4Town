import mysql.connector

class Producto:

    def __init__(self, costo, descripcion, id, nombre_prod):
        self.costo=costo
        self.descripcion=descripcion
        self.id=id
        self.nombre_prod=nombre_prod

    def agregar_producto(self):

        db = mysql.connector.connect(
            host="localhost",
            user="tu_usuario",
            password="tu_contraseña",
            database="ingsoft"
        )

        cursor = db.cursor()

        sql = "INSERT INTO Producto (id, nombre, descripcion, costo) VALUES (%s, %s, %s, %s)"
        val = (self.id, self.nombre, self.descripcion, self.costo)
        
        cursor.execute(sql, val)
        
        db.commit()

        cursor.close()

        db.close()

    # Realizar Inventario
    def actualizarNombre(self, nuevoNombre):
        """
        Cambia el nombre del Producto
        """
        # Actualizar el nombre del producto en la base de datos
        db = mysql.connector.connect(
            host="localhost",
            user="tu_usuario",
            password="tu_contraseña",
            database="ingsoft"
        )

        cursor = db.cursor()
        sql = "UPDATE Producto SET nombre = %s WHERE id = %s"
        val = (nuevoNombre, self.id)
        cursor.execute(sql, val)
        db.commit()

        # Actualizar el nombre del producto en la instancia
        self.nombre_prod = nuevoNombre
        print("Nombre actualizado a", self.nombre_prod)

    def actualizarDescripcion():
        """
        Cambia la descripción del Producto
        """
        # Actualizar la descripción del producto en la base de datos
        db = mysql.connector.connect(
            host="localhost",
            user="tu_usuario",
            password="tu_contraseña",
            database="ingsoft"
        )

        cursor = db.cursor()
        sql = "UPDATE Producto SET descripcion = %s WHERE id = %s"
        val = (nuevaDescripcion, self.id)
        cursor.execute(sql, val)
        db.commit()

        # Actualizar la descripción del producto en la instancia
        self.descripcion = nuevaDescripcion
        print("Descripcion actualizada a", self.descripcion)

    def actualizarCosto():
        """
        Cambia el costo del Producto
        """
        # Actualizar el costo del producto en la base de datos
        db = mysql.connector.connect(
            host="localhost",
            user="tu_usuario",
            password="tu_contraseña",
            database="ingsoft"
        )

        cursor = db.cursor()
        sql = "UPDATE Producto SET costo = %s WHERE id = %s"
        val = (nuevoCosto, self.id)
        cursor.execute(sql, val)
        db.commit()

        # Actualizar el costo del producto en la instancia
        self.costo = nuevoCosto
        print("Costo actualizado a", self.costo)