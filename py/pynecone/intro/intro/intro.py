# type: ignore
"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from pcconfig import config

import pynecone as pc

docs_url = "https://pynecone.io/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


class State(pc.State):
    """The app state."""

    pass


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
            
        ),
        padding_top="10%",
    )


# Add state and page to the app.
app = pc.App(state=State)
app.add_page(index)
app.compile()
