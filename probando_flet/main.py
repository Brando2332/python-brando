import flet as ft


def main(page: ft.Page):
    def calcular(e):
        try:
            entrada = tf_num1.value
            entrada = entrada.replace("x","*")
            entrada = entrada.replace("^","**")
            resultado = eval(entrada)
            label_resultado.value = f"resultado {resultado}"
            page.update()
        except Exception as e:
            label_resultado.value = "expresion invalida"
            page.update()

    titulo = ft.Text("CALCULADORA")
    page.add(titulo)
    
    tf_num1 = ft.TextField(width=140)
    page.add(tf_num1)

    boton_calcular = ft.ElevatedButton(text="calcular", on_click=calcular)
    page.add(boton_calcular)

    label_resultado = ft.Text("resultado: ")
    page.add(label_resultado)

ft.app(target=main)
