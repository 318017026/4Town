# Archivo de importaciones globales
from flask import Blueprint, redirect, render_template, url_for, request, session, g, redirect
from flask import flash, get_flashed_messages
from models.CRUD_Bebida_M import agregar_bebida, obtener_bebidas, eliminar_bebida,actualizar_bebida
from models.CRUD_Bebida_M import  obtener_bebida_por_id, estatus_conexion
from models.Usuario_M import getUserByEmail, getUserByName, getCrendential, deactivate_user, activate_user
import re

# Arreglo de dominios validos para correo
dominios_validos = ['gmail.com', 'hotmail.com', 'ciencias.unam.mx']