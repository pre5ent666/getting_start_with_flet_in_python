import flet as ft

class GreeterControl(ft.UserControl):
    def build(self):
        return ft.Column([
            ft.TextField(label="Your name"),
            ft.ElevatedButton("Login")
        ])

def main(page):
    page.add(GreeterControl())
    page.add(GreeterControl())

ft.app(target=main)