# type: ignore
import random
import string

from pcconfig import config
import pynecone as pc
import plotly as pl
import plotly.graph_objects as go

docs_url = "https://pynecone.io/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"

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

letters = string.ascii_lowercase

class Idea(pc.Model, table=True):
    author: str
    text: str
    feasibility100: int
    practicality100: int


def pc_idea(idea: Idea):
    return pc.box(
        pc.heading(idea.author),
        pc.text(idea.text),
        pc.text(f"feazblt:{idea.feasibility100}"),
        pc.text(f"praktklt:{idea.practicality100}")
    )

with pc.session() as session:
    session.add(
        Idea(
            author=''.join(random.choice(letters) for i in range(3)),
            text=''.join(random.choice(letters) for i in range(10)),
            feasibility100=random.choice(list(range(100))),
            practicality100=random.choice(list(range(100)))
        )
    )
    session.commit()

class AppState(pc.State):
    switched_container: bool = False
    color = [
        "red",
        "green",
        "blue",
    ]

    def change(self):
        self.switched_container = not (self.switched_container)

    def get_ideas(self):
        with pc.session() as session:
            self.ideas = (
                session.query(Idea)
                .all()
            )

        return self.ideas

    def pc_idea_stream(self):
        self.get_ideas()
        contents = []
        for id in self.ideas:
            contents.append(pc_idea(id))

        return pc.box(contents)



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
                                                            pc.foreach(AppState.color, colored_box),
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
            pc.responsive_grid(
                # pc.foreach(AppState.get_ideas, pc_idea)
            )
        ),
        padding_top="10%",
    )


# Add state and page to the app.
app = pc.App(state=AppState)
app.add_page(index)
app.compile()
