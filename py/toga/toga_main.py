from functools import partial

import toga
from toga.style.pack import COLUMN, LEFT, RIGHT, ROW, Pack


def calculate(widget, effect_container, secondary_container):
    print(widget)
    print(widget.__dict__)
    try:
        effect_container.value = (float(secondary_container.value) - 32.0) * 5.0 / 9.0
    except ValueError:
        effect_container.value = "???"

def build(app):
    c_box, f_box, box = toga.Box(), toga.Box(), toga.Box()

    c_input = toga.TextInput(readonly=True)
    f_input = toga.TextInput()

    c_label = toga.Label("Celsius", style=Pack(text_align=LEFT))
    f_label = toga.Label("Fahrenheit", style=Pack(text_align=LEFT))
    join_label = toga.Label("is equivalent to", style=Pack(text_align=RIGHT))

    calculate_c_label = partial(
        calculate,
        effect_container=c_input,
        secondary_container=f_input
    )

    button = toga.Button("Calculate", on_press=calculate_c_label)

    f_box.add(f_input)
    f_box.add(f_label)

    c_box.add(join_label)
    c_box.add(c_input)
    c_box.add(c_label)

    box.add(f_box)
    box.add(c_box)
    box.add(button)

    box.style.update(direction=COLUMN, padding=10)
    f_box.style.update(direction=ROW, padding=5)
    c_box.style.update(direction=ROW, padding=5)

    c_input.style.update(flex=1)
    f_input.style.update(flex=1, padding_left=210)
    c_label.style.update(width=100, padding_left=10)
    f_label.style.update(width=100, padding_left=10)
    join_label.style.update(width=200, padding_right=10)

    button.style.update(padding=15)

    return box


def main():
    return toga.App(
        "Temperature Converter",
        "org.beeware.f_to_c",
        startup=build
    )


if __name__ == "__main__":
    main().main_loop()