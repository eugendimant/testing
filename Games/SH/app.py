import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(page_title="Crimson Corridor 2D", layout="wide")

st.title("Crimson Corridor 2D: Serbianhero at Nachtarena")
st.caption(
    "Use WASD/Arrow keys to move, E to interact, Space to slap (cartoon), and P to pause."
)

html_path = Path(__file__).with_name("index.html")
html = html_path.read_text(encoding="utf-8")

components.html(html, height=760, scrolling=False)

with st.expander("How to play", expanded=False):
    st.markdown(
        """
        **Controls**
        - Move: **WASD / Arrow keys**
        - Interact: **E**
        - Slap (cartoon): **Space**
        - Pause: **P**

        **Goal**
        - Build respect/viral energy and keep heat low to pass all three door checks.
        """
    )
