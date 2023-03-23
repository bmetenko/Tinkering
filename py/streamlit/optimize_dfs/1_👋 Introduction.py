from pathlib import Path

import streamlit as st
from streamlit_extras.badges import badge
from streamlit_extras.app_logo import add_logo
from streamlit_extras.colored_header import colored_header
from streamlit_card import card
from streamlit_extras.echo_expander import echo_expander
from streamlit_extras.let_it_rain import rain
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

### Source: https://www.svgbackgrounds.com/
with open(Path.cwd()/"assets"/"flat-mountains.svg") as f:
    svg_content = f.readlines()

with open(Path.cwd()/"assets"/"flat-mountains.css") as f:
    xml_content = "".join(f.readlines())


# print(xml_content)

st.markdown(
    f'''
    <style>
    {xml_content}
    </style>
    ''',
    unsafe_allow_html=True
)

if 'prev' in st.session_state.keys():
    previous_page = st.session_state['prev']
    st.write(f"Welcome from the {previous_page} page.")

st.session_state['prev'] = 'introduction'

rain(
    emoji="👋",
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

next_page = st.button("Move to next page!")
if next_page:
    st.session_state['prev'] = 'introduction'
    switch_page("theory")