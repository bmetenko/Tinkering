import flet as ft

def main(page: ft.Page):

    text_1 = ft.Text(
        value="Introductory App in Flet",
        color="red",
        bgcolor="green",
        text_align=ft.TextAlign.CENTER,
        expand=1
    )

    page.controls.append(text_1)
    page.update()

    text_2 = ft.Text(
        "Move the slider please..."
    )

    def change_expand(e):
        text_2.expand = int(e.control.value)
        text_2.update()

    page.add(
        text_2,
        ft.Slider(
            min=1,
            max=10,
            divisions=9,
            label="{value}",
            width=500,
            on_change_end=change_expand
        )
    )


ft.app(target=main)