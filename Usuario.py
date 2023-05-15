import mysql.connector

class Usuario:

    def __init__(self, nombre, contra, apeidoP, apeidoM,fechaNac, correo):
        self.nombre = nombre
        self.password = contra
        self.apeidoP = apeidoP
        self.apeidoM = apeidoM
        self.fechaNac = fechaNac
        self.correo = correo
        self.statusSesion = True
        self.credencial = 154531234


    def agregar_usuario(self):
        """
        Agrega un nuevo usuario a la tabla 'Usuario' de la base de datos
        """
        # Establecer conexión con la base de datos
        db = mysql.connector.connect(
            host="localhost",
            user="tu_usuario",
            password="tu_contraseña",
            database="ingsoft"
        )

        # Obtener un cursor para ejecutar consultas SQL
        cursor = db.cursor()

        # Definir la consulta SQL para insertar un nuevo usuario
        sql = "INSERT INTO Usuario (nombre, apellidoP, apellidoM, fechaNacimiento, correo, contrasena, estatusSesion, credencial) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        val = (self.nombre, self.apellidoP, self.apellidoM, self.fechaNacimiento, self.correo, self.contrasena,
               self.estatusSesion, self.credencial)

        # Ejecutar la consulta SQL
        cursor.execute(sql, val)

        # Confirmar los cambios en la base de datos
        db.commit()

        # Cerrar la conexión con la base de datos
        db.close()