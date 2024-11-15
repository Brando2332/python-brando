from conexion_db import *
import flet as ft

def main (page: ft.Page):
    def verificar_usuario(e):
        nombre = tf_nombre.value
        clave = tf_clave.value
        
        page.open(ft.AlertDialog(title=ft.Text(verificar_usuario_db(nombre, clave)), modal=False))

    page.add(ft.SafeArea(ft.Text("Login", size=20)))

    tf_nombre = ft.TextField(label="Usuario")
    tf_clave = ft.TextField(label="Clave")
    btn_login = ft.ElevatedButton("Login", on_click = verificar_usuario) 

    label_usuario=ft.Text("")
    label_rol=ft.Text("")

    page.add(tf_nombre, tf_clave, btn_login, label_usuario, label_rol)

ft.app(main)    