import streamlit as st
import streamlit_elements as ste


with ste.elements("title"): # type: ignore
    ste.mui.Typography(
        "Disconnected Elements", 
        align="center",
        gutterBottom=True,
        variant="h3",
        sx = {
            "color": "lightblue",
            "border-color": "aliceblue",
            "border-radius": "2em 2em 0 0",
            "border-style": "dashed",
            "padding": "1em"
        }
        )
    
    ste.mui.Typography(
        "MUI / streamlit elements", 
        align="center",
        gutterBottom=False,
        variant="h5",
        sx = {
            "color": "#dc3545", 
            "font": "bold 1em Helvetica",
            "border-radius": "0 0 2em 2em",
            "border-color": "aliceblue",
            "border-style": "dashed",
            "padding": "1em"
        }
        )
    
    ste.mui.Typography(
        "^ Not a burger...",
        align="center",
        sx = {
            "font": "bold 12px Helvetica",
            "padding": "5px"
        }
    )
    

with st.expander("Streamlit Expander", True):
    with ste.elements("Intenal Expander"): # type: ignore
        # ste.mui.Typography("Test")
        with ste.mui.Accordion():
            with ste.mui.AccordionSummary(expandIcon=ste.mui.icon.ExpandMore()):
                ste.mui.Typography("Internal Expander from MUI")

            with ste.mui.AccordionDetails():
                ste.mui.Alert("Internal Expander content", severity="warning")
    