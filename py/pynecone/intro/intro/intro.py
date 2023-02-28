# type: ignore
"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from pcconfig import config

import pynecone as pc

docs_url = "https://pynecone.io/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


class ToggleState(pc.State):
    switched_container: bool = False

    def change(self):
        self.switched_container = not (self.switched_container)


def index() -> pc.Component:
    return pc.center(
        pc.vstack(
            pc.chart(
                pc.area(
                    data=pc.data(
                        "area",
                        x = [1, 4, 5, 6, 7, 1, 5, 6],
                        y = [2, 3, 4, 5, 6, 7, 8, 9]
                    ),
                    style = {
                        "data":{
                            "fill": "green",
                            "stroke": "yellow",
                            "strokeWidth": 1
                        }
                    }
                ),
                pc.area(
                    data=pc.data(
                        "line",
                        x = [1, 2, 3, 4, 5, 6, 7],
                        y = [2, 6, 7, 4, 6, 1, 2]
                    ),
                    style={
                        "data":{
                            "fill": "red"
                        }
                    }
                )
            ),
            pc.accordion(
                pc.accordion_item(
                    pc.accordion_button(
                        pc.heading("Chart Info"),
                        pc.accordion_icon()
                    ),
                    pc.accordion_panel(
                        pc.center(
                            pc.vstack(
                                pc.button("Toggle", on_click=ToggleState.change),
                                pc.cond(
                                    ToggleState.switched_container,
                                    pc.text("Text is blue", color="blue"),
                                    pc.text("Text is red", color="red"),
                                ),
                                pc.tabs(
                                    pc.tab_list(
                                        pc.tab("W"),
                                        pc.tab("S"),
                                        pc.tab("I"),
                                    ),
                                    pc.tab_panels(
                                        pc.tab_panel(
                                            pc.center(
                                                    pc.alert(
                                                        pc.alert_icon(),
                                                        pc.alert_title(
                                                            "Warning label."
                                                            ),
                                                        status="warning",
                                                    ),
                                                )
                                            ),
                                        pc.tab_panel(
                                            pc.center(
                                                pc.alert(
                                                    pc.alert_icon(),
                                                    pc.alert_title(
                                                        "Success label."
                                                        ),
                                                    status="success",
                                                    ),
                                                )
                                            ),
                                        pc.tab_panel(
                                            pc.center(
                                                pc.alert(
                                                        pc.alert_icon(),
                                                        pc.alert_title(
                                                            "Information label."
                                                            ),
                                                        status="info",
                                                    ),
                                                )
                                            ),
                                    ),
                                    variant="enclosed-colored",
                                    is_fitted=True,
                                    is_lazy=True
                                )
                            ),
                        ),
                        border_width="thick",
                        border_color="purple",
                        padding="1em",
                    ),
                    width="100%"
                )
            )
        ),
        padding_top="10%",
    )


# Add state and page to the app.
app = pc.App(state=ToggleState)
app.add_page(index)
app.compile()
