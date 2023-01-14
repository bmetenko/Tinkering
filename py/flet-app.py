import math

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

    container_1 = ft.Container(
        width=100,
        height=100,
        gradient=ft.SweepGradient(
            start_angle=math.pi * (1/3),
            end_angle=math.pi * (2/3),
            rotation=1,
            colors=[
                ft.colors.AMBER,
                ft.colors.BLUE_400,
                ft.colors.YELLOW_300
            ],
            center=ft.alignment.top_left,
            tile_mode=ft.GradientTileMode.REPEATED
        ),
        bgcolor="Red",
        border_radius=2,
        animate_opacity=300,
        border=ft.border.all(2, ft.colors.BLUE_300)
    )

    def opacity_container_1(e):
        container_1.opacity = 0 \
            if bool(container_1.opacity) \
            else 1
        container_1.update()

    page.add(
        container_1,
        ft.ElevatedButton(
            "Toggle container...",
            on_click=opacity_container_1,
            icon=ft.icons.FAVORITE_BORDER,
            icon_color="blue"
        )
    )


ft.app(target=main)