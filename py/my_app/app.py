import re
import time

from shiny import App, render, ui, reactive
import rich

time_choices: dict[str, str] = {"t0": "5 seconds", "t1": "30 seconds", "t2": "1 minute"}
seconds_map: dict[str, int] = {"t0": 5, "t1": 30, "t2": 60}

app_ui = ui.page_fluid(
    ui.h2("Hello Shiny!"),
    ui.input_slider("n", "N", 0, 100, 20),
    ui.input_text("txt", ""),
    ui.input_checkbox_group("time_choice", "Supply time to wait:", time_choices),
    ui.input_action_button("start_timer", "Start timer!"), 
    ui.output_text_verbatim("timer")

)


def server(input, output, session):

    x = reactive.Value(0)
    timer_done = reactive.Value(True)
    n: int = 0

    @reactive.Effect
    @reactive.event(input.start_timer)
    def timer_run():
        # reactive.invalidate_later(0.5)
        time_to_wait = 0
        for val in input.time_choice():
            time_to_wait += seconds_map[val]

        x.set(time_to_wait)
        id = ui.notification_show(
            f"{x()} second timer, running...", 
            duration=time_to_wait,
            close_button=True
            )


app = App(app_ui, server)
