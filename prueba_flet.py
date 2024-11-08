import flet as ft

def main (page: ft.page):
    saludo = ft.Text("saludo")
    page.add(saludo)

ft.app(target=main)