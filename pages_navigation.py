import flet as ft
import time
from UserControls.greeter import GreeterControl

def main(page: ft.Page):
    # maximize the window
    page.window_maximized = True
    page.title = "Routes Example"

    # To navigate between pages, use page.go(route) - a helper method that updates page.route
    page_store = ft.View(
                    "/store",
                    [
                        ft.AppBar(title=ft.Text("Store"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                    ],
                )
    
    page_home = ft.View(
                "/",
                [
                    ft.AppBar(title=ft.Text("Flet app"), bgcolor=ft.colors.SURFACE_VARIANT),
                    ft.ElevatedButton("Visit Store", on_click=lambda _: page.go("/store")),
                    ft.ElevatedButton("Visit Greeter", on_click=lambda _: page.go("/greeter")),
                ],
            )
    
    greeter = GreeterControl()
    page_greeter = ft.View(
                    "/greeter",
                    [
                        ft.AppBar(title=ft.Text("Greeter"), bgcolor=ft.colors.SURFACE_VARIANT),
                        greeter,
                        ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                    ],
                )

    def route_change(route):
        page.views.clear()
        page.views.append(page_home)
        if page.route == "/store":
            page.views.append(page_store)
        elif page.route == "/greeter":
            # greeter = GreeterControl()
            # page.views.append(greeter)
            page.views.append(page_greeter)
        page.update()

    def view_pop():
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    # page.on_route_change event handler is a function of a route, navigation history stack (a list of views depending on the current route)
    page.on_route_change = route_change
    # page.on_view_pop event handler, fires when the user clicks automatic "Back" button in AppBar control, remove the last element from views collection and navigate to view's root "under" it.
    page.on_view_pop = view_pop
    page.go(page.route)

ft.app(target=main)