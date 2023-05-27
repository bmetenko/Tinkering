import streamlit as st
import streamlit_elements as ste


# region Typography
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

# endregion
    
# region Expanders
with st.expander("Streamlit Expander", True):
    with ste.elements("Intenal Expander"): # type: ignore
        # ste.mui.Typography("Test")
        with ste.mui.Accordion():
            with ste.mui.AccordionSummary(expandIcon=ste.mui.icon.ExpandMore()):
                ste.mui.Typography("Internal Expander from MUI")

            with ste.mui.AccordionDetails():
                ste.mui.Alert("Internal Expander content", severity="warning")

# endregion

# region Grid

with ste.elements("grid"): # type: ignore
    layout = [
        # Parameters: element_identifier, x_pos, y_pos, width, height, [item properties...]
        ste.dashboard.Item("1st", 0, 0, 2, 2),
        ste.dashboard.Item("2nd", 2, 0, 2, 2, isDraggable=False, moved=False),
        ste.dashboard.Item("3rd", 0, 2, 2, 2, isResizable=False),
        ]
    
    with ste.dashboard.Grid(layout):
        ste.mui.Paper("First item (✅ drag and ✅ resize)", key="1st", sx={"padding": "1em"})
        ste.mui.Paper("Second item (❌ drag)", key="2nd", sx={"padding": "1em"})
        ste.mui.Paper("Third item (❌ resize)", key="3rd", sx={"padding": "1em"})

# endregion

# Continue: https://okld-gallery.streamlit.app/?p=elements
# Ref: https://mui.com/material-ui/react-accordion/