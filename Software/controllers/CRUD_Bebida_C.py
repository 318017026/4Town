from controllers.__init__ import Blueprint, redirect, render_template, url_for, request, agregar_bebida, estatus_conexion
from controllers.__init__ import obtener_bebidas, eliminar_bebida, actualizar_bebida, obtener_bebida_por_id

# Declaracion de Blueprints
createBluePrint = Blueprint("createDrink", __name__, url_prefix="/create")
readBluePrint = Blueprint("readDrink",__name__,url_prefix="/read")
updateBluePrint = Blueprint("updateDrink", __name__, url_prefix="/update")
deleteBluePrint = Blueprint("deleteDrink",__name__, url_prefix="/delete")

@createBluePrint.route("/create", methods=["GET","POST"])# type: ignore
def create():
    if estatus_conexion:
        if request.method == "POST":
            nombre = request.form["nombre"]
            descripcion = request.form["descripcion"]
            costo = request.form["costo"]
            agregar_bebida(nombre, descripcion, costo)
            return redirect(url_for('readDrink.read'))
        else:
            return render_template("create.html")
    
@readBluePrint.route("/read", methods=["GET","POST"]) # type: ignore
def read():
    if estatus_conexion:
        productos = obtener_bebidas()
        return render_template("index.html", bebidas=productos)
        
@deleteBluePrint.route("/delete/<int:id>",methods=["GET","POST"])# type: ignore
def delete(id):
    if estatus_conexion:
        eliminar_bebida(id)
        return redirect(url_for('readDrink.read'))
    
@updateBluePrint.route("/update/<int:id>", methods=["GET","POST"])# type: ignore
def update(id):
    row = obtener_bebida_por_id(id)
    if estatus_conexion:
        if request.method == "POST":
            if row is not None:
                nombre = request.form["nombre"]
                descripcion = request.form["descripcion"]
                costo = request.form["costo"]
                ventas = request.form["ventas"]
                if not redudant_update(row,nombre,descripcion,costo,ventas):
                    nombre = row.nombre if nombre=='' else row.nombre if nombre==row.nombre else nombre
                    descripcion = row.descripcion if descripcion=='' else row.descripcion if descripcion==row.descripcion else descripcion
                    costo = row.costo if costo=='' else row.costo if costo==row.costo else abs(float(costo))
                    ventas = row.ventas if ventas=='' else row.ventas if ventas==row.ventas else abs(int(ventas))
                    actualizar_bebida(id,nombre,descripcion,costo,ventas)
                else:
                    print(f"ALERTA: Actualización redundante del registro (Acción abortada) {row} - Controlador CRUD Modelo")
            else:
                print("ERROR: El producto referido no existe. - Controlador CRUD Modelo")
            return redirect(url_for('readDrink.read'))
        else:
            if row is not None:
                return render_template("edit.html", id_p=id, nombre_p=row.nombre, descripcion_p=row.descripcion, costo_p = row.costo, ventas_p=row.ventas)
            return render_template("edit.html", id_p=id)

'''
Funcion que determina si una actualizacion es redundante
'''
def redudant_update(row, nombre, descripcion, costo, ventas):
    if (nombre == '') and (descripcion == '') and (costo == '') and (ventas == ''):
        return True
    elif (row.nombre==nombre)and(row.descripcion==descripcion)and(row.costo==float(costo))and(row.ventas==int(ventas)):
        return True
    else:
        return False