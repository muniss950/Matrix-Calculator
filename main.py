import flet as ft
import fletmat

def main(page: ft.Page):

    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.CALCULATE),
        leading_width=40,
        title=ft.Text("Matrix Calculator"),
        center_title=False,
        bgcolor=ft.colors.SURFACE_VARIANT,
        )
    page.title="Matrix"
    page.window_height=500
    page.window_width=350
    page.window_left=500
    page.window_top=200
    page.window_resizable=False
    page.scroll=True
    result=fletmat.fletmat(5,5)
    page.add(
        
        result,
        ft.Row(
            controls=[
                ft.ElevatedButton(text="AC"),
                ft.ElevatedButton(text="INV"),
                ft.ElevatedButton(text="Tr"),
                ft.ElevatedButton(text="S/o"),
            ],

        ),
        ft.Row(
            controls=[
                ft.ElevatedButton(text="7"),
                ft.ElevatedButton(text="8"),
                ft.ElevatedButton(text="9"),
                ft.ElevatedButton(text="x"),
            ],

        ),
        ft.Row(
            controls=[
                ft.ElevatedButton(text="4"),
                ft.ElevatedButton(text="5"),
                ft.ElevatedButton(text="6"),
                ft.ElevatedButton(text="-"),
            ],

        ),
        ft.Row(
            controls=[
                ft.ElevatedButton(text="1"),
                ft.ElevatedButton(text="2"),
                ft.ElevatedButton(text="3"),
                ft.ElevatedButton(text="+"),
            ],

        ),
        ft.Row(
             controls=[
                ft.ElevatedButton(text="0"),
                ft.ElevatedButton(text="."),
                ft.ElevatedButton(text="="),
            ],

        ),
    )
ft.app(target=main)