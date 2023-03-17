import streamlit as st
from streamlit_extras.badges import badge
from streamlit_extras.app_logo import add_logo

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

from streamlit_card import card

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

st.write(
    """
    # Welcome to the Pandas Optimization App
    
    This app helps you optimize your pandas dataframes for speed and memory. 
    Click on the pages on the left to learn more!
    """
)