import streamlit as st
from streamlit_extras.colored_header import colored_header
from streamlit_extras.app_logo import add_logo

logo_url = "https://seeklogo.com/images/S/streamlit-logo-1A3B208AE4-seeklogo.com.png"
add_logo(logo_url)


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