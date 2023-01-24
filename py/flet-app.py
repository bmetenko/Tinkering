import math

import flet as ft
from flet.plotly_chart import PlotlyChart

def parse_file(e: ft.FilePickerResultEvent):
    selected_files = (
            ", ".join(map(lambda f: f.name, e.files)) if e.files else "Cancelled!"
        )

    file_contents = []
    for file in e.files:
        file_path = file.path
        file_name = file.name
        with open(file_path, "r") as f:
            if ".md" in file_name or ".txt" in file_name:
                file_contents.append("".join(f.readlines()))

    
    print(file_contents)
    print(selected_files)

def gen_graph():
    import plotly.express as px

    df = px.data.gapminder()
    df = df.query("continent == 'Americas'")

    figure = px.scatter(
        df,
        x="gdpPercap", 
        y="lifeExp", 
        animation_frame="year", 
        animation_group="country",
        size="pop", 
        color="country", 
        hover_name="country", 
        log_x = True, 
        size_max=45, 
        range_x=[100,100000], 
        range_y=[25,90]
    )

    return figure

def swap_theme(page, control):
    check = control.control.value
    page.theme_mode = ft.ThemeMode.DARK if check else ft.ThemeMode.LIGHT
    string_val = 'Light' if not check else 'Dark'
    control.control.label = f"Swap mode: Current ({string_val})" 
    control.control.thumb_color = {
            ft.MaterialState.HOVERED: ft.colors.BLUE_400 if not check else ft.colors.YELLOW_400,
            ft.MaterialState.FOCUSED: ft.colors.BLUE_200 if not check else ft.colors.YELLOW_200,
            ft.MaterialState.DEFAULT: ft.colors.BLUE_100 if not check else ft.colors.YELLOW_100
            }
    control.control.track_color = ft.colors.WHITE30 if check else ft.colors.BLACK87
    page.update()
    


def main(page: ft.Page):
    app_items = []

    page.scroll = "always"
    page.theme_mode = ft.ThemeMode.LIGHT
    mode_switch = ft.Switch(
        label="Swap mode: Current (Light)",
        on_change=lambda e: swap_theme(page, e),
        thumb_color={
            ft.MaterialState.HOVERED: ft.colors.BLUE_400,
            ft.MaterialState.FOCUSED: ft.colors.BLUE_200,
            ft.MaterialState.DEFAULT: ft.colors.BLUE_100
            },
        track_color=ft.colors.BLACK87
    )

    file_picker = ft.FilePicker(
        on_result = parse_file   
    )

    file_button = ft.ElevatedButton(
        "Upload File:",
        icon=ft.icons.UPLOAD_FILE_OUTLINED,
        on_click=lambda _: file_picker.pick_files(
            allow_multiple=True
        )
    )

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

    def toggle_icon(e):
        e.control.selected = not e.control.selected
        e.control.update()

    icon_row = ft.Row(
        [
            ft.IconButton(
                icon=ft.icons.BATTERY_1_BAR,
                selected_icon=ft.icons.BATTERY_FULL_ROUNDED,
                selected=False,
                style=ft.ButtonStyle(color={"selected": "blue", "": "yellow"}),
                icon_size=20,
                on_click=toggle_icon
                ),
            ft.IconButton(
                icon=ft.icons.AC_UNIT_SHARP,
                icon_color=ft.colors.RED,
                icon_size=20,
                selected_icon=ft.icons.ACCESS_ALARM_SHARP,
                on_click=toggle_icon
                ),
            mode_switch
        ],
        alignment="center"
    )
    
    # app_items.append(mode_switch)
    app_items.append(file_button)
    app_items.append(file_picker)
    app_items.append(text_1)
    app_items.append(text_2)
    app_items.append(slider)
    app_items.append(container_1)
    app_items.append(button)
    app_items.append(hover_container)
    app_items.append(text_3)
    app_items.append(icon_row)
    app_items.append(PlotlyChart(gen_graph(), expand=True))

    page.add(
        ft.ResponsiveRow(
            app_items,
            alignment=ft.MainAxisAlignment.CENTER
        )
    )


ft.app(target=main, view=ft.WEB_BROWSER)