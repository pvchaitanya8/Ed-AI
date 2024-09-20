import streamlit as st
from streamlit_ace import st_ace
import io
import contextlib

def Coding_Problems_page(markdown_file):
    st.markdown(
        """
        <style>
        .title h1 {
            font-size: 2.5rem;
            font-weight: 600;
            text-align: center;
            color: #343a40;
            margin-top: 20px;
        }
        </style>
        <div class="title">
        <h1>Two Sum</h1>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col_question1, col_question2 = st.columns([5, 5])

    with col_question1:
        theme_choice = st.selectbox("Reading Theme", ["Dark", "Light"], help="Adjust the reading mode according to your comfort.")

        if theme_choice == "Light":
            container_css = """
            <style>
            .gradient-divider {
                height: 5px;
                border-radius: 15px;
                background: linear-gradient(to right, #adb5bd, #ced4da, #adb5bd);
                margin: 0px 0;
                border: none;
            }
            .scroll-container {
                height: 550px;
                overflow-y: scroll;
                padding: 20px;
                border: 1px solid #ccc;
                border-radius: 10px;
                background-color: #f8f9fa;
                color: #212529;
                font-family: 'Courier New', Courier, monospace;
                font-size: 1.1rem;
                line-height: 1.6;
            }
            </style>
            """
        else:
            container_css = """
            <style>
            .gradient-divider {
                height: 5px;
                border-radius: 15px;
                background: linear-gradient(to right, #495057, #343a40, #495057);
                margin: 0px 0;
                border: none;
            }
            .scroll-container {
                height: 550px;
                overflow-y: scroll;
                padding: 20px;
                border: 1px solid #495057;
                border-radius: 10px;
                background-color: #050505;
                color: #f8f9fa;
                font-family: 'Courier New', Courier, monospace;
                font-size: 1.1rem;
                line-height: 1.6;
            }
            </style>
            """

        st.markdown(container_css, unsafe_allow_html=True)

        st.markdown('<div class="gradient-divider"></div>', unsafe_allow_html=True)

        try:
            with open(markdown_file, "r") as file:
                markdown_content = file.read()

            st.markdown(
                f"""
                <div class="scroll-container">
                {markdown_content}
                </div>
                """,
                unsafe_allow_html=True
            )
        except FileNotFoundError:
            st.error(f"File not found: {markdown_file}")


    with col_question2:
        themes_options = [
            "twilight",
            "tomorrow_night_bright",
            "tomorrow_night_blue",
            "tomorrow_night_eighties",
            "tomorrow_night_eiffel",
            "tomorrow_night_stark",
            "monokai",
            "dracula",
            "solarized_dark",
            "solarized_light",
            "github",
            "zenburn"
        ]

        language_options = [
            "python"
        ]

        col_editor1, col_editor2, col_editor3 = st.columns([3, 2, 5])
        with col_editor1:
            user_theme = st.selectbox("Compiler Theme", themes_options)
        with col_editor2:
            user_language = st.selectbox("Select Language", language_options)
        with col_editor3:
            user_font_size = st.slider(
                "Select Font Size",
                min_value=10,
                max_value=30,
                value=18,
                step=1,
                format="%d",
                key="font_size_slider"
            )

        code = st_ace(
            placeholder="Write your Python code here...",
            language=user_language,
            theme=user_theme,
            height=560, 
            font_size=user_font_size, 
            show_gutter=True, 
            keybinding="vscode", )

    def execute_code(code):
        output_buffer = io.StringIO()
        error_buffer = io.StringIO()

        try:
            # Capture stdout
            with contextlib.redirect_stdout(output_buffer):
                with contextlib.redirect_stderr(error_buffer):
                    exec(code, {})

            output = output_buffer.getvalue()
            error = error_buffer.getvalue()

            if error:
                return f"Error:\n{error}"
            else:
                return output if output else "Code executed successfully, but no output was produced."

        except Exception as e:
            return f"An error occurred: {e}"

    if st.button("Run Code"):
        if code:
            st.subheader("Output:")
            output = execute_code(code)
            st.text(output)
        else:
            st.warning("Please write some code before running it.")
