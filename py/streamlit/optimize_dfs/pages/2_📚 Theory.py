import streamlit as st
from streamlit_extras.colored_header import colored_header
from streamlit_extras.app_logo import add_logo
from streamlit_extras.stodo import to_do

logo_url = "https://seeklogo.com/images/S/streamlit-logo-1A3B208AE4-seeklogo.com.png"
add_logo(logo_url)

if 'prev' in st.session_state.keys():
    previous_page = st.session_state['prev']
    st.write(f"Welcome from the {previous_page} page.")

st.session_state['prev'] = 'theory'


colored_header(
    label="Pandas Optimization Theory",
    description="Steps included",
    color_name="blue-green-70",
)

st.write("""
    Pandas is a powerful tool for data analysis, 
    but it can be slow and memory-intensive when dealing with large datasets. 
    There are several ways to optimize pandas to improve its performance, including:
    
    - Dropping unnecessary columns
    - Using appropriate data types
    - Vectorizing operations
    - Using in-place operations
    - And more!
    
    To learn more about these optimizations, click on the next page on the left!
""")


st.write("To Learn")
to_do(
    [(st.write, "Pandas DataType Conversion")],
    "dtypes",
)

next_page = st.button("Continue? 3, 2, 1...", disabled=not st.session_state['dtypes'])

if next_page:
    from streamlit_extras.switch_page_button import switch_page
    st.session_state['prev'] = 'theory'
    switch_page("example")



go_back = st.button("Go Back!")
if go_back:
    from streamlit_extras.switch_page_button import switch_page
    st.session_state['prev'] = 'theory'
    switch_page("introduction")

