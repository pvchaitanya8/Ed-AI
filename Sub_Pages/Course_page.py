import streamlit as st
from UI_Components.Chat_Course import chat

def course_page(markdown_file, title):
    st.sidebar.markdown(
        """
        <style>
        .mentor-title {
            font-size: 28px;
            font-weight: bold;
            background: linear-gradient(90deg, #FFF5EE, #F3CFC6, #f9bec7, #ffafcc, #f72585, #b5179e, #7209b7, #560bad, #480ca8, #3a0ca3, #3f37c9, #4361ee, #4895ef, #4cc9f0, #caf0f8, #FFF5EE, #FFF5EE);
            background-clip: text;
            -webkit-background-clip: text;
            color: transparent;
            background-size: 200% 200%;
            animation: gradientFlow 5s ease infinite;
            text-align: center;
            margin-top: 0;
            margin-bottom: 15px;
        }

        @keyframes gradientFlow {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        </style>
        <h1 class="mentor-title">✨ Mentor Chat</h1>
        """,
        unsafe_allow_html=True
    )
    st.sidebar.markdown(
        """
        <style>
        .gradient-divider-sidebar {
            height: 5px;
            border-radius: 15px;
            background: linear-gradient(to right, #212529, #343a40, #212529);
            margin: 0px 0;
            border: none;
        }
        </style>
        <div class="gradient-divider-sidebar"></div>
        """,
        unsafe_allow_html=True
    )

    with st.sidebar:
        chat()

    st.markdown(
        """
        <style>
        .centered-title {
            text-align: center;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown(f'<h1 class="centered-title">{title}</h1>', unsafe_allow_html=True)

    st.markdown(
        """
        <style>
        .gradient-divider {
            height: 5px;
            border-radius: 15px;
            background: linear-gradient(to right, #495057, #212529, #495057);
            margin: 0px 0;
            border: none;
        }
        </style>
        <div class="gradient-divider"></div>
        """,
        unsafe_allow_html=True
    )

    try:
        with open(markdown_file, "r") as file:
            markdown_content = file.read()
        st.markdown(markdown_content)
    except FileNotFoundError:
        st.error(f"File not found: {markdown_file}")

    st.markdown(
        """
        <style>
        .gradient-divider {
            height: 5px;
            border-radius: 15px;
            background: linear-gradient(to right, #495057, #212529, #495057);
            margin: 0px 0;
            border: none;
        }
        </style>
        <div class="gradient-divider"></div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html= True)
    st.markdown("""
    <style>
    .stButton>button {
        width: 300px;  /* Adjust the width as needed */
    }
    </style>
    """, unsafe_allow_html=True)

    if st.button('Next'):
        st.success("Heading to next...")
        return