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
# NONE

# Importaciones de Administrador
# NONE

# Importaciones de Cliente
from models.model_cliente import getCliente
from alchemy_classes.Cliente import Cliente

# Importaciones de Pedido
from models.model_pedido import crearPedido, enlistaPedidosVendedor, enlistaPedidosCliente

# Importaciones de Venta
from models.model_venta import generaVentas

# Importaciones de Insumo
from models.model_insumo import enlistaInsumos, getInsumo, modificaInsumo, insertaInsumo
from alchemy_classes.Venta import Venta

# Importaciones de Credencial
from alchemy_classes.Credencial import Credencial


# Variables globales
dominios_validos = ['gmail.com', 'hotmail.com', 'ciencias.unam.mx']