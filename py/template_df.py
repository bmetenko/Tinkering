import jinja2 as j2
import pandas as pd

from jinja2 import Environment, ChoiceLoader, FileSystemLoader
from pandas.io.formats.style import Styler


class MyStyler(Styler):
    env = Environment(
        loader=ChoiceLoader([
            FileSystemLoader("templates"),
            Styler.loader,
        ])
    )
    template_html_table = env.get_template("template.j2")

data = {
    "fruit": ["apple", "orange", "lemon"],
    "cost": [0.25, 0.5, 0.2],
    "votes": [12, 30, 22]
}

df = pd.DataFrame(data)



# MyStyler(df)

# print(MyStyler(df).to_html(
#     table_title="Extending Example",
#     rows=df.to_dict(orient='records'),
#     columns=df.columns.to_list()
# ))

table_params = {
    "header_color": "green",
    "background_color": "red"
}

env = Environment(loader=FileSystemLoader("templates/"))
template = env.get_template("template.j2")

content = template.render(
    table_title="Extending Example",
    rows=df.to_dict(orient='records'),
    columns=df.columns.to_list(),
    **table_params
)

print(content)

import os

os.makedirs("out/", exist_ok=True)

with open("out/index.html", mode="w", encoding="UTF-8") as f:
    f.write(content)