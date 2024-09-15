import streamlit as st
from streamlit_option_menu import option_menu
from UI_Components.profile_pic import get_base64_image
from Pages.Learn_page import Learn_page
from Pages.Practice_page import Practice_Page

def navbar():
    logo_url = r"Static_Files\NavBar\Ed AI logo.png"
    profile_pic_url = r"Static_Files\NavBar\profile pic.png"

    col1, col2, col3, col4 = st.columns([0.7, 7, 3, 0.6])

    with col1:
        st.image(logo_url, width=70)  

    with col2:
        selected = option_menu(
            menu_title=None, 
            options=["Learn", "Practice", "Mock Interview", "Chat"], 
            icons=["book", "pencil-square", "briefcase", "chat-dots"], 
            menu_icon="cast",
            default_index=0,
            orientation="horizontal",
        )
        
    with col3:
        search_query = st.text_input("", placeholder="🔎 Search...")
        st.markdown("""<style>
            div[data-testid="stTextInput"] label {
                display: none;
            }""", unsafe_allow_html=True
        )

    with col4:
        profile_pic_base64 = get_base64_image(profile_pic_url)
        st.markdown(
            f"""
            <style>
            .circle-img {{
                display: block;
                margin-left: auto;
                margin-right: auto;
                border-radius: 50%;
                width: 50px;  /* Adjust the width as needed */
            }}
            </style>
            <img src="data:image/png;base64,{profile_pic_base64}" class="circle-img">
            """,
            unsafe_allow_html=True
        )

    st.markdown(
        """
        <style>
        .gradient-divider {
            height: 4px;
            border-radius: 15px;
            margin: 0px 0;
            background: linear-gradient(90deg, #e02666, #f06595, #5b61e3, #878be0, #803ae8);
            background-size: 200% 200%;
            animation: gradientFlow 6s ease infinite;
        }
        
        @keyframes gradientFlow {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        </style>
        <div class="gradient-divider"></div>
        """,
        unsafe_allow_html=True
    )

    if selected == "Learn":
        Learn_page()

    elif selected == "Practice":
        Practice_Page()

    elif selected == "Mock Interview":
        st.title("Mock Interview")
        st.write("This is the content of Mock Interview.")

    elif selected == "Chat":
        st.title("Chat")
        st.write("This is the content of Chat.")
        
    if search_query:
        st.write(f"Search results for: {search_query}")
        # Add your search handling logic here
