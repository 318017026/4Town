from Usuario import *

class Cliente(Usuario):

    # Inicializar un cliente
    def __init__(self, nombre, contra, apeidoP, apeidoM,fechaNac, correo, direccion, infoenvio, tarjeta, numero):
        super().__init__(nombre, contra, apeidoP, apeidoM,fechaNac, correo)
        self.direccion = direccion
        self.infoenvio = infoenvio
        self.tarjeta = tarjeta
        self.numero = numero

    # Crear un cliente y añadirlo a la base de datos
    def agregar_cliente(cliente):

        # Añadir usuario en la base de datos
        super().agregar_usuario()

        # Conectar con la base de datos
        conexion = mysql.connector.connect(
            host="localhost",
            user="usuario_db",
            password="contrasena_db",
            database="ingsoft"
        )

        # Crear un cursor para interactuar con la base de datos
        cursor = conexion.cursor()

        # Insertar el nuevo cliente en la tabla "Cliente"
        sql = "INSERT INTO Cliente (direccion, informacion_envio, tarjeta, numero) VALUES (%s, %s, %s, %s)"
        valores = (cliente.direccion, cliente.infoenvio, cliente.tarjeta, cliente.numero)
        cursor.execute(sql, valores)

        # Guardar los cambios en la base de datos
        conexion.commit()

        # Cerrar la conexión con la base de datos
        cursor.close()
        conexion.close()

    #Imprimir los datos del cliente
    def verDatos(self):
        print("Nombre:", self.nombre)
        print("Apellido paterno:", self.apeidoP)
        print("Apellido materno:", self.apeidoM)
        print("Fecha de nacimiento:", self.fechaNac)
        print("Correo:", self.correo)
        print("Dirección:", self.direccion)
        print("Información de envío:", self.infoenvio)
        print("Tarjeta:", self.tarjeta)
        print("Número:", self.numero)

    # Cambia el nombre
    def cambiaNombre(self, nuevoNombre):
        """
        Cambia el nombre del cliente
        """
        # Actualizar el nombre del cliente en la base de datos
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

        # Actualizar el nombre del cliente en la instancia
        self.nombre = nuevoNombre
        print("Nombre actualizado a", self.nombre)

    # Cambia el apeido Paterno
    def cambiaApeidoP(self, nuevoApeidoP):
        """
        Cambia el apellido paterno del cliente
        """
        # Actualizar el apellido paterno del cliente en la base de datos
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

        # Actualizar el apellido paterno del cliente en la instancia
        self.apellidoP = nuevoApeidoP
        print("Apellido paterno actualizado a", self.apellidoP)

    # Cambia el apeido Materno
    def cambiaApeidoM(self, nuevoApeidoM):
        """
        Cambia el apellido materno del cliente
        """
        # Actualizar el apellido materno del cliente en la base de datos
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

        # Actualizar el apellido materno del cliente en la instancia
        self.apellidoM = nuevoApeidoM
        print("Apellido materno actualizado a", self.apellidoM)

    # Cambia la fecha de nacimiento
    def cambiaFechaNac(self, nueva_fecha):
        # Cambiar la fecha de nacimiento del cliente
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
        # Cambiar el correo del cliente
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

    # Cambia la direccion de entrega
    def cambiaDireccion(self, nueva_direccion):
        # Cambiar la dirección del cliente
        self.direccion = nueva_direccion

        # Conectar con la base de datos
        conexion = mysql.connector.connect(
            host="localhost",
            user="usuario_db",
            password="contrasena_db",
            database="ingsoft"
        )

        # Crear un cursor para interactuar con la base de datos
        cursor = conexion.cursor()

        # Actualizar la dirección en la tabla "Cliente"
        sql = "UPDATE Cliente SET direccion = %s WHERE id = %s"
        valores = (self.direccion, self.id)
        cursor.execute(sql, valores)

        # Guardar los cambios en la base de datos
        conexion.commit()

        # Cerrar la conexión con la base de datos
        cursor.close()
        conexion.close()

    # Cambia la informacion del envio
    def cambiaInfoEnvio(self, nueva_infoenvio):
        """
        Cambia la información de envío del cliente
        """
        self.infoenvio = nueva_infoenvio

        # Conectar con la base de datos
        conexion = mysql.connector.connect(
            host="localhost",
            user="usuario_db",
            password="contrasena_db",
            database="ingsoft"
        )

        # Crear un cursor para interactuar con la base de datos
        cursor = conexion.cursor()

        # Actualizar el registro del cliente en la tabla "Cliente"
        sql = "UPDATE Cliente SET informacion_envio = %s WHERE id = %s"
        valores = (self.infoenvio, self.id)
        cursor.execute(sql, valores)

        # Guardar los cambios en la base de datos
        conexion.commit()

        # Cerrar la conexión con la base de datos
        cursor.close()
        conexion.close()

    # Cambia el numero de tarjeta
    def cambiaTarjeta(self, nueva_tarjeta):
        """
        Cambia el número de tarjeta de crédito del cliente
        """
        self.tarjeta = nueva_tarjeta

        # Conectar con la base de datos
        conexion = mysql.connector.connect(
            host="localhost",
            user="usuario_db",
            password="contrasena_db",
            database="ingsoft"
        )

        # Crear un cursor para interactuar con la base de datos
        cursor = conexion.cursor()

        # Actualizar el registro del cliente en la tabla "Cliente"
        sql = "UPDATE Cliente SET tarjeta = %s WHERE id = %s"
        valores = (self.tarjeta, self.id)
        cursor.execute(sql, valores)

        # Guardar los cambios en la base de datos
        conexion.commit()

        # Cerrar la conexión con la base de datos
        cursor.close()
        conexion.close()

    # Cambia el numero celular
    def cambiaNumero(self, nuevo_numero):
        """
        Cambia el número celular del cliente
        """
        self.numero = nuevo_numero

        # Conectar con la base de datos
        conexion = mysql.connector.connect(
            host="localhost",
            user="usuario_db",
            password="contrasena_db",
            database="ingsoft"
        )

        # Crear un cursor para interactuar con la base de datos
        cursor = conexion.cursor()

        # Actualizar el registro del cliente en la tabla "Cliente"
        sql = "UPDATE Cliente SET numero = %s WHERE id = %s"
        valores = (self.numero, self.id)
        cursor.execute(sql, valores)

        # Guardar los cambios en la base de datos
        conexion.commit()

        # Cerrar la conexión con la base de datos
        cursor.close()
        conexion.close()

    # Método para eliminar al cliente de la base de datos
    def eliminarCliente(self):

        # Conectar con la base de datos
        conexion = mysql.connector.connect(
            host="localhost",
            user="usuario_db",
            password="contrasena_db",
            database="ingsoft"
        )

        # Crear un cursor para interactuar con la base de datos
        cursor = conexion.cursor()

        try:
            # Eliminar al cliente de la tabla Usuario primero
            sql = "DELETE FROM Usuario WHERE id = %s"
            valores = (self.id,)
            cursor.execute(sql, valores)

            # Eliminar al cliente de la tabla Cliente
            sql = "DELETE FROM Cliente WHERE id = %s"
            valores = (self.id,)
            cursor.execute(sql, valores)

            # Guardar los cambios en la base de datos
            conexion.commit()

            print(f"El cliente {self.nombre} ha sido eliminado exitosamente de la base de datos.")
        except mysql.connector.Error as error:
            # Si hay algún error, imprimir el mensaje de error
            print(f"Error al eliminar al cliente {self.nombre}: {error}")
        finally:
            # Cerrar la conexión con la base de datos
            cursor.close()
            conexion.close()
            del self
