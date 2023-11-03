from pathlib import Path
from io import StringIO
import hashlib

import numpy as np
import pandas as pd
import streamlit as st
import streamlit_echarts as ec
from streamlit_extras.badges import badge
from streamlit_extras.app_logo import add_logo
from streamlit_extras.colored_header import colored_header
from streamlit_card import card
from streamlit_extras.echo_expander import echo_expander
from streamlit_extras.let_it_rain import rain
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.vertical_slider import vertical_slider
from streamlit_extras.toggle_switch import st_toggle_switch
from streamlit_extras.tags import tagger_component
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_extras.grid import grid
from streamlit_extras.function_explorer import function_explorer
from streamlit_extras.markdownlit import mdlit
from streamlit_extras.stylable_container import stylable_container
from streamlit_extras.metric_cards import style_metric_cards
from streamlit_extras.card import card
from streamlit_extras.chart_container import chart_container
# noinspection PyProtectedMember
from lets_plot import ggplot, geom_point, ggsize, aes, _kbridge, theme

from pyecharts.charts import WordCloud
from pyecharts import options as opts

st.set_page_config(
    page_title="Hello",
    page_icon="🎃",

)
# LetsPlot.setup_html()

df = pd.read_csv("https://raw.githubusercontent.com/JetBrains/lets-plot-docs/master/data/iris.csv")
p = ggplot(df) \
    + geom_point(aes('petal_length', 'petal_width', color='species'), size=5) \
    + ggsize(600, 400) \
    + theme()

# noinspection PyProtectedMember
plot_html = _kbridge._generate_static_html_page(p.as_dict(), True)
# viz_html = HTML(filename=fullpath_html)

st.markdown(
    "<style>"
    ".streamlit-expanderContent{background-color:black !important;}"
    "</style>",
    unsafe_allow_html=True
)

with st.expander("Let's Plot bridge", 1):
    with stylable_container(
            key="plot-background",
            css_styles="""
        center {
            background-color: white;
            color: black;
            border-radius: 20px;
            padding: 5px 10px;
            margin: 5px 10px;
        }
        center{
            border-color: red;
            border-width: 0.5em;
            border-style: solid;
            &:hover {
                border-color: blue;
            }
        }
        """,
    ):
        with chart_container(df):
            st.markdown(
                "<center>" + plot_html + "</center>",
                unsafe_allow_html=True
            )

# card(
#     title="Welcome",
#     text="If you dare!",
#     image="https://placekitten.com/500/500",
# )
style_metric_cards(
    background_color="red",
    box_shadow=False,
    border_color='green',
    border_size_px=4,
    border_radius_px=3,
    border_left_color='yellow'
)

st.metric(
    delta_color='normal',
    label="Tacky Coloring", value=5000, delta=15000
)

### Source: https://www.svgbackgrounds.com/
with open(Path.cwd()/"assets"/"flat-mountains.svg") as f:
    svg_content = f.readlines()

with open(Path.cwd()/"assets"/"flat-mountains.css") as f:
    xml_content = "".join(f.readlines())


def tags():

    grid2 = grid([2,3,2], vertical_align="bottom")
    with grid2.expander("grid0", expanded=True):
        tagger_component(
            "Feature request",
            ["accepted", "🚩triaged", "backlog"],
            color_name=['blue', 'orange', 'red']
        )
    with grid2.expander("grid1", expanded=True):
        tagger_component(
            "Animal tags",
            ["turtle", "rabbit", "lion"],
            color_name=["green", "lightblue", "yellow"],
        )

    with grid2.expander("grid1", expanded=True):
        tagger_component(
            "Next Feature",
            ["prediction"],
            color_name=["violet"],
        )

    grid2 = grid(1, 2, vertical_align="bottom")
    with grid2.expander("grid0", expanded=True):
        tagger_component(
            "Feature request",
            ["accepted", "🚩triaged", "backlog"],
            color_name=['blue', 'orange', 'red']
        )
    with grid2.expander("grid1", expanded=True):
        tagger_component(
            "Animal tags",
            ["turtle", "rabbit", "lion"],
            color_name=["green", "lightblue", "yellow"],
        )

    with grid2.expander("grid1", expanded=True):
        tagger_component(
            "Next Feature",
            ["prediction"],
            color_name=["violet"],
        )


# print(xml_content)

st.markdown(
    f'''
    <style>
    {xml_content}
    </style>
    ''',
    unsafe_allow_html=True
)

option = {
    "graphic": {
      "elements": [
        {
          "type": 'group',
          "left": 'center',
          "top": 'center',
          "children": [
            {
            "type": 'rect',
            "x": i * 20,
            "shape": {
              "x": 0,
              "y": -40,
              "width": 10,
              "height": 80
            },
            "style": {
              "fill": '#5470c6'
            },
            "keyframeAnimation": {
              "duration": 1000,
              "delay": i * 200,
              "loop": "true",
              "keyframes": [
                {
                  "percent": 0.5,
                  "scaleY": 0.3,
                  "easing": 'cubicIn'
                },
                {
                  "percent": 1,
                  "scaleY": 1,
                  "easing": 'cubicOut'
                } 
              ]
            }
          } for i in range(3)
          ]
        }
      ]
    }
  }

events = {
    "click": "function(params) { console.log(params.name) }"
}



chart = WordCloud(
    init_opts=opts.InitOpts(
            animation_opts=opts.AnimationOpts(
                animation_delay=1000, 
                animation_easing="easeOut"
            )
        )
).add("", [(
    "Welcome", np.random.randint(0, 4)) for i in range(50)
    ], shape="octagon"
    )

ec.st_pyecharts(chart)

# ec.st_echarts(options=option, events=events)

if 'prev' in st.session_state.keys():
    previous_page = st.session_state['prev']
    st.write(f"Welcome from the {previous_page} page.")

st.session_state['prev'] = 'introduction'

with st.sidebar:
    make_it_rain = st_toggle_switch(
        label="Enable emoji rain?",
        # key="switch_1",
        default_value=True,
        label_after=False,
        inactive_color="#D3D3FF",
        active_color="#115600",
        track_color="#29B5FF",
    )

    st.radio(
        "Checksum to generate",
        ["MD5", "SHA256", "SHA1"],
        horizontal=True,
        key='sum'
    )

    checksum_dict = {
        "MD5": hashlib.md5,
        "SHA256": hashlib.sha256,
        "SHA1": hashlib.sha1
    }

    sum_name = st.session_state['sum']
    with st.expander(sum_name, True):

        uploaded_file = st.file_uploader(
            f"{sum_name} of file:",
            accept_multiple_files=False,
            key="file"
        )

        if uploaded_file is not None:
            bytes_data = uploaded_file.getvalue()

            st.write(
                checksum_dict[sum_name](bytes_data).hexdigest()
            )



if make_it_rain:
    rain(
        emoji="🎃",
        font_size=30,
        falling_speed=25,
        animation_length="infinite",
    )

with echo_expander():
    c0, c1 = st.columns(2)
    with c0:
        card(
            title="Hello!",
            text="Enjoy your stay!",
            image="https://cdn.pixabay.com/photo/2015/04/27/11/48/sign-741813_1280.jpg",
            url="https://www.github.com/bmetenko",
        )

    with c1:
        card(
            title="2nd Welcome",
            text="Not sure why it was needed...",
            image="https://pandas.pydata.org/static/img/pandas_mark.svg",
            url='/Theory'
        )

    with st.expander("Echo Container Disassembly"):
        import dis
        import inspect
        st.write(dis.Bytecode(echo_expander).dis())
        st.write(inspect.getsource(echo_expander))

logo_url = "https://seeklogo.com/images/S/streamlit-logo-1A3B208AE4-seeklogo.com.png"
add_logo(logo_url)

badge(type="github", name="bmetenko")


colored_header(
    label="Welcome to the Pandas Optimization App",
    description="This app helps you optimize your pandas dataframes for speed and memory. ",
    color_name="violet-70",
)

st.write(
    """
    Click on the pages on the left to learn more!
    """
)

st.markdown(
    """
    _Actually, this is just a toy website for testing streamlit components, but don't tell anyone._
    """
)

# st.write(svg_content[0], unsafe_allow_html=True)

def example():
    st.write("## Vertical Slider Example, buggy in current iteration...")
    vertical_slider(
        key="slider",
        default_value=25,
        step=1,
        min_value=0,
        max_value=100,
        # track_color="gray",  # optional
        # thumb_color="blue",  # optional
        # slider_color="red",  # optional
    )
    st.write(f'value: {st.session_state["slider"]}')


# with st.sidebar as sidebar:
#     example()

tags()


add_vertical_space(3)
function_explorer(add_vertical_space)
add_vertical_space(2)

mdlit("""
??? toggle
    @(🎁)(Click me!)(https://www.youtube.com/watch?v=dQw4w9WgXcQ)
    ??? 2nd toggle
        [violet]Nested[/violet] contenet <-
""")




next_page = st.button("Move to next page!")
if next_page:
    st.session_state['prev'] = 'introduction'
    switch_page("theory")