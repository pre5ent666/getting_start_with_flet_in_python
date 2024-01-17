import flet as ft

def main(page: ft.Page):
    # title
    page.title = "Calculator"

    # result of calculator (Text control)
    result = ft.Text(value="0", color=ft.colors.WHITE, size=40)

    # create column control containing Rows of ElevatedButtons
    col = ft.Column(
        controls=[
            ft.Row(controls=[result], alignment="end"),
            ft.Row(
                controls=[
                    ft.ElevatedButton(
                        text="AC",
                        expand=1.2,
                    ),
                    ft.ElevatedButton(
                        text="+/-",
                        expand=1.2,
                    ),
                    ft.ElevatedButton(
                        text="%",
                        expand=1,
                    ),
                    ft.ElevatedButton(
                        text="/",
                        expand=1,
                    ),
                ]
            ),
            ft.Row(
                controls=[
                    ft.ElevatedButton(
                        text="7",
                        expand=1,
                    ),
                    ft.ElevatedButton(
                        text="8",
                        expand=1,
                    ),
                    ft.ElevatedButton(
                        text="9",
                        expand=1,
                    ),
                    ft.ElevatedButton(
                        text="*",
                        expand=1,
                    ),
                ]
            ),
            ft.Row(
                controls=[
                    ft.ElevatedButton(
                        text="4",
                        expand=1,
                    ),
                    ft.ElevatedButton(
                        text="5",
                        expand=1,
                    ),
                    ft.ElevatedButton(
                        text="6",
                        expand=1,
                    ),
                    ft.ElevatedButton(
                        text="-",
                        expand=1,
                    ),
                ]
            ),
            ft.Row(
                controls=[
                    ft.ElevatedButton(
                        text="1",
                        expand=1,
                    ),
                    ft.ElevatedButton(
                        text="2",
                        expand=1,
                    ),
                    ft.ElevatedButton(
                        text="3",
                        expand=1,
                    ),
                    ft.ElevatedButton(
                        text="+",
                        expand=1,
                    ),
                ]
            ),
            ft.Row(
                controls=[
                    ft.ElevatedButton(
                        text="0",
                        expand=2,
                    ),
                    ft.ElevatedButton(
                        text=".",
                        expand=1,
                    ),
                    ft.ElevatedButton(
                        text="=",
                        expand=1,
                    ),
                ]
            ),
        ]
    )

    # add container into page and set properties
    page.add(
        ft.Container(
            width=300,
            bgcolor=ft.colors.BLACK,
            border_radius=ft.border_radius.all(20),
            padding=20,
            content=col
        )
    )

ft.app(target=main)
