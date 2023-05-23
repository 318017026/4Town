class Administrador(Usuario):
    
    #El formato de búsqueda deber ser de tipo "nombre=Maria, apeidoP=Rodriguez"
    def consulta_cliente(busqueda):
        busqueda = busqueda.lower()
        busqueda = busqueda.split(", ")
    
        #Establecer conexion con la base de datos
        db = mysql.connector.connect(
            host="localhost",
            user="tu_usuario",
            password="tu_contraseña",
            database="ingsoft"
        )

        # Obtener un cursor para ejecutar consultas SQL
        cursor = db.cursor()

        consulta = ""
        for elem in busqueda:
            i=0
            if (i > 0):                
                consulta = consulta++"AND"++elem
            else:
                consulta = elem
            i+=1
           
        #Obtener cliente de la base de datos
        sql="SELECT * FROM Cliente WHERE("++consulta++")"
        result = cursor.execute(sql)

        #Mostrar resultado
        for elem in result:
            print(elem)

        # Cerrar la conexión con la base de datos
        cursor.close()