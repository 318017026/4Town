# Importaciones generales (Flask)
from flask import Flask, render_template, redirect, url_for, g, session
from alchemy_classes.__init__ import db

# Importaciones de Controlador Bebida
from controllers.CRUD_Bebida_C import createBluePrint, readBluePrint, deleteBluePrint, updateBluePrint

# Importaciones de Controlador Usuario
from controllers.Usuario_C import loginBluePrint

# Importaciones de Controlador Inventario
from controllers.controller_inventario import inventario_bp

# Importaciones de Controlador Hacer Pedido
from controllers.controller_pedido import pedido_bp

# Importaciones de Controlador Monitorear Estatus
from controllers.controller_status_pedido import status_pedido_bp

# Importaciones de Controlador Reportes de Venta
from controllers.controller_venta import venta_bp, reporteVenta_bp

# Importaciones de Controlador Cliente
from controllers.rutas import clientes

# Importaciones de Controlador Vendedor
from controllers.controller_administrar_vendedores import readSellerBluePrint, createSellerBluePrint, deleteSellerBluePrint, updateSellerBluePrint

#Importancion de Controlador Clientes
from controllers.controller_cliente import consultarCliente_bp
