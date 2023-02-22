import streamlit as st

from streamlit.components.v1 import html

st.write("Hello World")


html_source = "index.html"

def html_from_file(file_name):
    with open(file_name, "r") as html_file:
        return html(
            html_file.read(),
            height=0,
            width=0
        )
    
html_from_file(html_source)