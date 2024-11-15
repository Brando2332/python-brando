from conexion_db import *
import flet as ft

def main (page: ft.Page):
    def crear_usuario(e):
        nombre = tf_nombre.value
        clave = tf_clave.value
        rol = tf_rol.value
        crear_usuario_db(nombre, clave, rol)
        page.open(ft.AlertDialog(title=ft.Text("Usuario creado exitosamente"), modal=False))

    page.add(ft.SafeArea(ft.Text("Administracion de usuarios", size=20)))

    subtitulo_anadir = ft.Text("anadir nuevo usuario")
    tf_nombre = ft.TextField(label="Nombre")
    tf_clave = ft.TextField(label="Clave")
    tf_rol = ft.TextField(label="Rol")

    btn_crear = ft.ElevatedButton("crear usuario", on_click = crear_usuario)
    
    page.add(subtitulo_anadir, tf_nombre, tf_clave, tf_rol, btn_crear)

ft.app(main)    