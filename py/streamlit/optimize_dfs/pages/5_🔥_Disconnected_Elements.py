import numpy as np
import streamlit as st
import streamlit_elements as ste

i0 = np.random.randint(0, 100, size=100)
i1 = np.random.randint(0, 100, size=100)
j = zip(i0, i1)

data = [
    { "id": i, "x": str(j[0]), "y": str(j[1])} for i, j in enumerate(j) 
]

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

    if "first_item_resize" not in st.session_state:
        st.session_state.first_item_resize = None

    if st.session_state.first_item_resize is not None:
        text = f"{st.session_state.first_item_resize.target.value} resized or text changed since resize is odd."

    else:
        text = "Resize item 1 ..."

    ste.mui.Typography(text)

    layout = [
        # Parameters: element_identifier, x_pos, y_pos, width, height, [item properties...]
        ste.dashboard.Item("1st", 0, 0, 2, 2),
        ste.dashboard.Item("2nd", 2, 0, 2, 2, isDraggable=False, moved=False),
        ste.dashboard.Item("3rd", 0, 2, 2, 2, isResizable=False),
        ]
    
    with ste.dashboard.Grid(layout):
        ste.mui.Paper(
            "First item (✅ drag and ✅ resize)", 
            key="1st", 
            sx={"padding": "1em"},
            onChange=ste.sync("first_item_resize"))
        ste.mui.Paper("Second item (❌ drag)", key="2nd", sx={"padding": "1em"})
        ste.mui.Paper("Third item (❌ resize)", key="3rd", sx={"padding": "1em"})

        ste.mui.TextField(label="Input some text here", onChange=ste.sync("first_item_resize"))

    with ste.mui.Box(sx={"height": 500}): # type: ignore
        ste.nivo.Voronoi(
        data=data,
        xDomain=[ 0, 100 ],
        yDomain=[ 0, 100 ],
        enableLinks=True,
        linkLineColor="#cccccc",
        cellLineColor="#c6432d",
        pointSize=6,
        pointColor="#5c2dc8",
        margin={ "top": 1, "right": 1, "bottom": 1, "left": 1 }
        )

    with ste.mui.Box(sx={"display": "flex", "justifyContent": "center"}):
        ste.media.Player(
            url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            loop=True,
            pip=True,
            # onReady=lambda: print("loaded video...")
        )

# endregion

# Continue: https://okld-gallery.streamlit.app/?p=elements
# Ref: https://mui.com/material-ui/react-accordion/