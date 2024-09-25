import json
import streamlit as st
from streamlit_ace import st_ace
import io
import sys

def Coding_Problems_page(markdown_file, Problem_title, test_cases):
    st.markdown(
        f"""
        <style>
        .title h1 {{
            font-size: 2.5rem;
            font-weight: 600;
            text-align: center;
            color: #343a40;
            margin-top: 20px;
        }}
        </style>
        <div class="title">
        <h1>{Problem_title}</h1>
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
            "monokai",
            "tomorrow_night_bright",
            "tomorrow_night_blue",
            "tomorrow_night_eighties",
            "tomorrow_night_eiffel",
            "tomorrow_night_stark",
            "twilight",
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

    def execute_code(code, inputs):
        output_buffer = io.StringIO()
        error_buffer = io.StringIO()

        # Simulate input by overriding the built-in input() function
        input_lines = iter([inputs])  # Pass the full input string at once

        def mock_input(prompt=None):
            try:
                return next(input_lines)  # Return the full input string on the first input() call
            except StopIteration:
                raise ValueError("Insufficient input data provided for input() calls")

        try:
            # Redirect print statements to capture them
            sys.stdout = output_buffer
            sys.stderr = error_buffer

            # Execute the user's code, replacing input() with our mock function
            exec(code, {"input": mock_input})

            # Get the captured output and errors
            output = output_buffer.getvalue()
            error = error_buffer.getvalue()

            # Restore original stdout and stderr
            sys.stdout = sys.__stdout__
            sys.stderr = sys.__stderr__

            if error:
                return f"Error:\n{error}"
            else:
                return output.strip() if output else "Code executed successfully, but no output was produced."

        except Exception as e:
            # Ensure stdout and stderr are restored in case of error
            sys.stdout = sys.__stdout__
            sys.stderr = sys.__stderr__
            return f"An error occurred: {e}"

    # Display test cases
    st.subheader("Test Cases")
    for i, (input_data, expected_output) in enumerate(test_cases):
        st.markdown(f"**Test Case {i+1}:** Input: `{input_data}`, Expected Output: `{expected_output}`")

    # Button to run the code
    if st.button("Run Code"):
        if code:
            st.subheader("Output:")
            all_passed = True
            for i, (input_data, expected_output) in enumerate(test_cases):
                output = execute_code(code, input_data)
                result = output

                if output == expected_output:
                    st.success(f"""
                        **✅ Test Case {i+1} Passed!**
                        - **Your Output:** {result}
                    """)

                else:
                    st.error(f"""
                        **⚠️ Test Case {i+1} Failed!**  
                        - **Your Output:** {result}  
                        - **Expected Output:** `{expected_output}`
                    """)
                    all_passed = False

            if all_passed:
                st.balloons()

        else:
            st.warning("Please write some code before running it.")


# Example test cases to validate code
with open(r'EXP\Redirecting_test_problem.json', 'r') as file:
    data = json.load(file)

problem_problem_id = data["ID"]
problem_title = data["title"]
problem_problem_description = data["Problem_Description"]
problem_test_cases = data["Test_Cases"]

Coding_Problems_page(problem_problem_description, problem_title, problem_test_cases)


