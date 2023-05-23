from Usuario import *

class Vendedor(Usuario):

    def __init__(self, nombre, contra, apeidoP, apeidoM,fechaNac, correo):
        super().__init__(nombre. contra, apeidoP, apeidoM, fechaNac, correo)
        self,id = None
        self.userId = None
    
    def agregar_vendedor(self):

        # Añadir nuevo Usuario vendedor en la base de datos, y conseguimos su id
        id = super().agregar_usuario()

        # Conectar con la base de datos
        conexion = mysql.connector.connect(
            host="localhost",
            user="usuario_db",
            password="contrasena_db",
            database="ingsoft"
        )
        self.userId = id

        # Crear un cursor para interactuar con la base de datos
        cursor = conexion.cursor()

        # Insertar el nuevo vendedor en la tabla "Vendedor"
        sql = "INSERT INTO Vendedor (userId) VALUES (%s)"
        valores = (id)
        cursor.execute(sql, valores)

        self.id = cursor.lastrowid
        # Guardar los cambios en la base de datos
        conexion.commit()

        # Cerrar la conexión con la base de datos
        cursor.close()
        conexion.close()
    
    def cosultar_vendedor(self):

        conexion = mysql.connector.connect(
            host="localhost",
            user="usuario_db",
            password="contrasena_db",
            database="ingsoft"
        )

        # Crear un cursor para interactuar con la base de datos
        cursor = conexion.cursor()

        # Insertar el nuevo vendedor en la tabla "vendedor"
        sql = "SELECT * FROM Vendedor WHERE id = (%s)"
        valores = (self.id)
        cursor.execute(sql, valores)

        # Guardar los cambios en la base de datos
        conexion.commit()

        # Cerrar la conexión con la base de datos
        cursor.close()
        conexion.close()

        for (id, userId) in cursor:
            res = {
                "id": id,
                "userId": userId
            }

        return res
    
    def eliminar_vendedor(self):

        conexion = mysql.connector.connect(
            host="localhost",
            user="usuario_db",
            password="contrasena_db",
            database="ingsoft"
        )

        # Crear un cursor para interactuar con la base de datos
        cursor = conexion.cursor()

        # Insertar el nuevo vendedor en la tabla "Vendedor"
        sql = "DELETE FROM Vendedor WHERE id = (%s)"
        valores = (self.id)
        cursor.execute(sql, valores)

        # Guardar los cambios en la base de datos
        conexion.commit()

        # Cerrar la conexión con la base de datos
        cursor.close()
        conexion.close()

    # Cambia el nombre
    def cambiaNombre(self, nuevoNombre):
        """
        Cambia el nombre del vendedor
        """
        # Actualizar el nombre del vendedor en la base de datos
        db = mysql.connector.connect(
            host="localhost",
            user="tu_usuario",
            password="tu_contraseña",
            database="ingsoft"
        )

        cursor = db.cursor()
        sql = "UPDATE Usuario SET nombre = %s WHERE id = %s"
        val = (nuevoNombre, self.id)
        cursor.execute(sql, val)
        db.commit()

        # Actualizar el nombre del vendedor en la instancia
        self.nombre = nuevoNombre
        print("Nombre actualizado a", self.nombre)

    # Cambia el apeido Paterno
    def cambiaApeidoP(self, nuevoApeidoP):
        """
        Cambia el apellido paterno del vendedor
        """
        # Actualizar el apellido paterno del vendedor en la base de datos
        db = mysql.connector.connect(
            host="localhost",
            user="tu_usuario",
            password="tu_contraseña",
            database="ingsoft"
        )

        cursor = db.cursor()
        sql = "UPDATE Usuario SET apellidoP = %s WHERE id = %s"
        val = (nuevoApeidoP, self.id)
        cursor.execute(sql, val)
        db.commit()

        # Actualizar el apellido paterno del vendedor en la instancia
        self.apellidoP = nuevoApeidoP
        print("Apellido paterno actualizado a", self.apellidoP)

    # Cambia el apeido Materno
    def cambiaApeidoM(self, nuevoApeidoM):
        """
        Cambia el apellido materno del vendedor
        """
        # Actualizar el apellido materno del vendedor en la base de datos
        db = mysql.connector.connect(
            host="localhost",
            user="tu_usuario",
            password="tu_contraseña",
            database="ingsoft"
        )

        cursor = db.cursor()
        sql = "UPDATE Usuario SET apellidoM = %s WHERE id = %s"
        val = (nuevoApeidoM, self.id)
        cursor.execute(sql, val)
        db.commit()

        # Actualizar el apellido materno del vendedor en la instancia
        self.apellidoM = nuevoApeidoM
        print("Apellido materno actualizado a", self.apellidoM)

    # Cambia la fecha de nacimiento
    def cambiaFechaNac(self, nueva_fecha):
        # Cambiar la fecha de nacimiento del vendedor
        self.fechaNac = nueva_fecha

        # Conectar con la base de datos
        conexion = mysql.connector.connect(
            host="localhost",
            user="usuario_db",
            password="contrasena_db",
            database="ingsoft"
        )

        # Crear un cursor para interactuar con la base de datos
        cursor = conexion.cursor()

        # Actualizar la fecha de nacimiento en la tabla "Usuario"
        sql = "UPDATE Usuario SET fechaNacimiento = %s WHERE id = %s"
        valores = (self.fechaNac, self.id)
        cursor.execute(sql, valores)

        # Guardar los cambios en la base de datos
        conexion.commit()

        # Cerrar la conexión con la base de datos
        cursor.close()
        conexion.close()

    # Cambia el correo electronico
    def cambiaCorreo(self, nuevo_correo):
        # Cambiar el correo del vendedor
        self.correo = nuevo_correo

        # Conectar con la base de datos
        conexion = mysql.connector.connect(
            host="localhost",
            user="usuario_db",
            password="contrasena_db",
            database="ingsoft"
        )

        # Crear un cursor para interactuar con la base de datos
        cursor = conexion.cursor()

        # Actualizar el correo en la tabla "Usuario"
        sql = "UPDATE Usuario SET correo = %s WHERE id = %s"
        valores = (self.correo, self.id)
        cursor.execute(sql, valores)

        # Guardar los cambios en la base de datos
        conexion.commit()

        # Cerrar la conexión con la base de datos
        cursor.close()
        conexion.close()





    
