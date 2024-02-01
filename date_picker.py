import datetime
import flet as ft

#TODO: Can we change the language to Chinese?

def main(page: ft.Page):
    def change_date(e):
        t.value = f"Date picker changed, value is {date_picker.value}"
        page.update()

    def date_picker_dismissed(e):
        t.value = f"Date picker dismissed, value is {date_picker.value}"
        page.update()

    date_picker = ft.DatePicker(
        on_change=change_date,
        on_dismiss=date_picker_dismissed,
        first_date=datetime.datetime(2023, 10, 1),
        last_date=datetime.datetime(2024, 10, 1),
    )
    
    page.overlay.append(date_picker)

    date_button = ft.ElevatedButton(
        "Pick date",
        icon=ft.icons.CALENDAR_MONTH,
        on_click=lambda _: date_picker.pick_date(),
    )
    t = ft.Text()
    page.add(date_button, t)

ft.app(target=main)