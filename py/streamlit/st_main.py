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
    


col_1, col_2 = st.columns(2)

with col_1:
    st.date_input("Choose a date:")

with col_2:
    st.write("Choose a date please.")
    st.write("Or don't...")
    st.write("I'm not your boss.")

html_from_file(html_source)