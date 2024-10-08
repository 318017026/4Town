# Archivo de importaciones globales
from alchemy_classes.__init__ import db

# Importaciones generales (Flask, re y mysql.connector)
from flask import Blueprint, redirect, render_template, url_for, request, session, g, redirect
from flask import flash, get_flashed_messages
import re
import mysql.connector

# Importaciones modelo CRUD Bebida
from models.CRUD_Bebida_M import agregar_bebida, obtener_bebidas, eliminar_bebida,actualizar_bebida, obtener_bebida_por_id, estatus_conexion, obtener_bebidas_por_id
 
# Importaciones de modelo Usuario
from models.Usuario_M import getUserByEmail, getUserByName, getCrendential, deactivate_user, activate_user
from alchemy_classes.Usuario import Usuario
# Importaciones de Vendedor
from models.model_vendedor import obtener_vendedores, eliminar_vendedor, obtener_vendedor_por_id, actualizar_vendedor
from alchemy_classes.Vendedor import Vendedor

# Importaciones de Administrador
# NONE

# Importaciones de Cliente
from models.model_cliente import getCliente, getClientes
from alchemy_classes.Cliente import Cliente

# Importaciones de Pedido
from models.model_pedido import crearPedido, enlistaPedidosVendedor, enlistaPedidosCliente

# Importaciones de Venta
<<<<<<< HEAD
from models.model_venta import generaVentas, obtener_ventas, obtener_ventas_eliminados
# Importaciones de Insumo
from models.model_insumo import enlistaInsumos, getInsumo, modificaInsumo, insertaInsumo
from alchemy_classes.Insumo import Insumo

from alchemy_classes.Venta import Venta
=======
from models.model_venta import generaVentas
from alchemy_classes.Venta import Venta

# Importaciones de Insumo
from models.model_insumo import enlistaInsumos, getInsumo, modificaInsumo, insertaInsumo
from alchemy_classes.Insumo import Insumo
>>>>>>> f1562b62b0199ef7aaa62dfdb1c4e89603c1a2ce

# Importaciones de Credencial
from alchemy_classes.Credencial import Credencial


# Variables globales
dominios_validos = ['gmail.com', 'hotmail.com', 'ciencias.unam.mx']
