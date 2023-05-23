from alchemyClasses.db import db, Producto, Bebida, Insumo

def enlistaBebidas():
    return db.session.query(Bebida, Producto).join(Producto).all()

def enlistaInsumos():
    return db.session.query(Insumo, Producto).join(Producto).all()

def getProducto(id):
    return Producto.query.filter(Producto.id == id).first()

def isBebida(id):
    return Bebida.query.filter(Bebida.id == id).first() != None

def getInsumo(id):
    return Insumo.query.filter(Insumo.id == id).first()

def modificaProducto(id, nombre, descripcion, costo):
    producto = Producto.query.filter(Producto.id == id).first()
    producto.nombre = nombre
    producto.descripcion = descripcion
    producto.costo = costo
    db.session.commit()

def modificaInsumo(id, nombre, descripcion, costo, piezas):
    modificaProducto(id, nombre, descripcion, costo)
    insumo = Insumo.query.filter(Producto.id == id).first()
    insumo.piezas = piezas
    db.session.commit()

def insertaBebida(nombre, descripcion, costo):
    producto = Producto(nombre, descripcion, costo)
    db.session.add(producto)
    db.session.commit()
    bebida = Bebida(producto.id, 0)
    db.session.add(bebida)
    db.session.commit()

def insertaInsumo(nombre, descripcion, costo, piezas):
    producto = Producto(nombre, descripcion, costo)
    db.session.add(producto)
    db.session.commit()
    bebida = Insumo(producto.id, piezas)
    db.session.add(bebida)
    db.session.commit()