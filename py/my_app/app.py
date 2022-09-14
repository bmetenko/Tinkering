import asyncio

from shiny import App, render, ui, reactive

time_choices: dict[str, str] = {"t0": "5 seconds", "t1": "30 seconds", "t2": "1 minute"}
seconds_map: dict[str, int] = {"t0": 5, "t1": 30, "t2": 60}

app_ui = ui.page_fluid(
    ui.h2("Hello Shiny!"),
    ui.input_slider("n", "N", 0, 100, 20),
    ui.output_text_verbatim("txt"),
    ui.input_checkbox_group("time_choice", "Supply time to wait:", time_choices),
    ui.input_action_button("start_timer", "Start timer!"), 
    ui.output_text_verbatim("timer")

)


def server(input, output, session):
    @output
    @render.text
    def txt():
        return f"n*2 is {input.n() * 2}"

    @output
    @render.text
    @reactive.event(input.start_timer)
    async def timer():
        time_to_wait = 0
        print(input.time_choice())
        for val in input.time_choice():
            time_to_wait += seconds_map[val]
        
        while time_to_wait > 0:
            print(f"waiting: {time_to_wait} seconds")
            time_to_wait -= 1
            await asyncio.sleep(1)
        
        return "Timer done."



app = App(app_ui, server)
