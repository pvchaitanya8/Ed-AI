import streamlit as st
from UI_Components.navbar import navbar

st.set_page_config(
    page_title="Ed AI",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

def main():
    display_navbar = True
    if display_navbar:
        navbar()

if __name__ == "__main__":
    main()
