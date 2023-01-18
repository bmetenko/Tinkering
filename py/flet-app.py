import math

import flet as ft

def main(page: ft.Page):

    app_items = []
    text_1 = ft.Text(
        value="Introductory App in Flet",
        color="red",
        bgcolor="green",
        text_align=ft.TextAlign.CENTER,
        expand=1
    )

    text_2 = ft.Text(
        "Move the slider please..."
    )

    def change_expand(e):
        text_2.expand = int(e.control.value)
        text_2.update()

    slider = ft.Slider(
            min=1,
            max=10,
            divisions=9,
            label="{value}",
            width=500,
            on_change_end=change_expand
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

    text_3 = ft.Text(
        f"Opacity: 1.00"
    )

    def hover_opacity(e, text_element=text_3):
        if e.control.opacity >= 0.1:
            e.control.opacity *= 0.90
        else:
            e.control.opacity = 1

        text_element.value = f"Opacity: {e.control.opacity:.2f}"

        e.control.update()
        text_element.update()

    hover_container = ft.Container(
        width=100,
        height=100,
        bgcolor=ft.colors.DEEP_ORANGE_50,
        ink=False,
        on_hover=hover_opacity,
        content=ft.Text("Hover over to change opacity.", color=ft.colors.GREEN),
        alignment=ft.alignment.center,
    )
    
    button = ft.ElevatedButton(
            "Toggle container...",
            on_click=opacity_container_1,
            icon=ft.icons.FAVORITE_BORDER,
            icon_color="blue",
            on_long_press=hover_opacity
        )

    app_items.append(text_1)
    app_items.append(text_2)
    app_items.append(slider)
    app_items.append(container_1)
    app_items.append(button)
    app_items.append(hover_container)
    app_items.append(text_3)

    page.add(
        ft.ResponsiveRow(
            app_items,
            alignment=ft.MainAxisAlignment.CENTER
        )
    )


ft.app(target=main)