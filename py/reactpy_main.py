from reactpy import component, html, run, hooks

@component
def hello_world():
    return html.h1("Hello, World!")


def increment(last_count):
    return last_count + 1


def decrement(last_count):
    return last_count - 1


@component
def Counter():
    initial_count = 0
    count, set_count = hooks.use_state(initial_count)
    return html.div(
        html.div(
        hello_world()
        ),
        html.br(),
        f"Count: {count}",
        html.br(),
        html.button(
            {"on_click": lambda event: set_count(initial_count)}, "Reset"
        ),
        html.br(),
        html.div(
        {"style": 
         {"backgroundColor": "blue", "height": "80px"},
         "children": ["nested...", "nested2..."]
         }
        ),
        html.button({"on_click": lambda event: set_count(increment)}, "+"),
        html.button({"on_click": lambda event: set_count(decrement)}, "-"),
    )

run(Counter)