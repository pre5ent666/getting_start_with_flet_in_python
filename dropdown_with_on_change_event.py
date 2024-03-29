import flet as ft

def main(page: ft.Page):
    def dropdown_changed(e):
        t.value = f"Dropdown changed to {dd.value}."

        # change background color of page
        page.bgcolor = dd.value
        # change text color of dropdown
        dd.color = dd.value
        page.update()

    t = ft.Text()
    dd = ft.Dropdown(
        on_change=dropdown_changed,
        options=[
            ft.dropdown.Option("Red"),
            ft.dropdown.Option("Green"),
            ft.dropdown.Option("Blue"),
        ],
        width=200,
    )
    page.add(dd, t)

ft.app(target=main)