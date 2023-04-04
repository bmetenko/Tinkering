# type: ignore
import random
import string
from typing import List

import numpy as np
# from pcconfig import config
import pynecone as pc
# import plotly as pl
import plotly.graph_objects as go
import pandas as pd

docs_url = "https://pynecone.io/docs/getting-started/introduction"

line_plotly = go.Figure(
    [
        go.Scatter(
            x = [1, 2, 3, 4, 5, 6, 7],
            y = [2, 6, 7, 4, 6, 1, 2],
            marker=dict(
                color="red"
            )
        )
    ]
)

big_df = pd.DataFrame(np.random.randn(16, 100))
big_df_style = big_df.style.set_sticky(axis="index")
big_df_html = big_df_style.to_html()

letters = string.ascii_lowercase

class Idea(pc.Model, table=True):
    author: str
    text: str
    feasibility: int
    practicality: int

def pc_idea(idea_) -> pc.Box:
    print(idea_.__dict__)
    return pc.hstack(
        pc.heading(idea_.author),
        pc.text(idea_.text),
        pc.text(idea_.feasibility),
        pc.text(idea_.practicality)
    )

def nested_acc(level=5):
    out = pc.accordion(
        pc.accordion_item(
            pc.accordion_button(
                pc.heading("Example"),
                pc.accordion_icon(),
            ),
            pc.accordion_panel(
                pc.text(
                    "final layer"
                ) if level == 0
                else (
                    pc.hstack(
                        pc.text(f"{level=}"),
                        nested_acc(level - 1)
                    )
                )
            ),
        ),
        width="100%",
    )

    return out

with pc.session() as session:
    fz = int(random.choice(list(range(100))))
    pt = int(random.choice(list(range(100))))
    new_idea = Idea(
            author=''.join(random.choice(letters) for i in range(5)),
            text=''.join(random.choice(letters) for i in range(10)),
            feasibility=fz,
            practicality=pt
        )
    session.add(
        new_idea
    )
    session.commit()

class AppState(pc.State):
    switched_container: bool = False
    color: List[str] = [
        "red",
        "green",
        "blue",
    ]
    ideas = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(self.__dict__)

    def change(self):
        self.switched_container = not (self.switched_container)

    @pc.var
    def get_ideas(self) -> List[Idea]:
        with pc.session() as session:
            self.ideas = (
                session.query(Idea)
                .all()
            )

        print(self.ideas)

        return self.ideas

    @pc.var
    def pc_idea_stream(self):
        contents = []
        for id in self.ideas:
            contents.append(id)
        return contents



def colored_box(color):
    return pc.box(
        pc.center(
            pc.text(color),
            padding="5px",
            border_radius="2px"
        ), 
        bg=color, 
        padding="5px", 
        color="white"
    )


def index() -> pc.Component:
    return pc.center(
        pc.vstack(
            pc.html(
                """
                <style>
                #bounce {
                    animation: bounce 0.5s infinite alternate;
                }

                @keyframes bounce {
                from {
                    transform: translateY(0);
                    }
                to {
                    transform: translateY(-10px);
                    }
                }

                </style>
                """
            ),
            pc.text(
                "Welcome",
                background="""
                linear-gradient(
                    90deg, rgba(2,0,36,1) 0%, 
                    rgba(9,9,121,1) 35%, 
                    rgba(0,212,255,1) 100%
                    )
                """,
                padding="1em",
                color="white",
                width="stretch",
                id="bounce"
            ),
            pc.hstack(
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
                    ),
                ),
                pc.plotly(
                    data=line_plotly
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
                                pc.button("Toggle", on_click=AppState.change),
                                pc.cond(
                                    AppState.switched_container,
                                    pc.text("Text is blue", color="blue"),
                                    pc.text("Text is red", color="red"),
                                ),
                                pc.tabs(
                                    pc.tab_list(
                                        pc.tab("W"),
                                        pc.tab("S"),
                                        pc.tab("I"),
                                        pc.tab("A")
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
                                        pc.tab_panel(
                                            pc.center(
                                                pc.alert(
                                                    pc.alert_icon(),
                                                    pc.alert_title(
                                                        pc.responsive_grid(
                                                            pc.foreach(
                                                                AppState.color, 
                                                                colored_box
                                                            ),
                                                            columns=[3],
                                                        )
                                                    ),
                                                    status="info"
                                                )
                                            )
                                        )
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
            ),
            pc.hstack(
                pc.center(
                pc.responsive_grid(
                    pc.foreach(AppState.get_ideas, pc_idea)
                ),
                overflow_y="scroll",
                height="4em",
                align_items="center",
                ),
            ),
            pc.hstack(
                nested_acc(3)
            ),
            pc.html(
                big_df_html,
                width="25em",
                overflow="scroll",
                border_color="red",
                border_width="0.2em"
            )
        ),
        padding_top="10%",
    )


# Add state and page to the app.
app = pc.App(state=AppState)
app.add_page(index)
app.compile()
