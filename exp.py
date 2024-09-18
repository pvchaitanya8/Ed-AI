import streamlit as st
import io
import sys

code_input = st.text_area("Write your Python code here", height=300)

output = None
if st.button("Run Code"):
    # Redirect standard output to capture print statements
    old_stdout = sys.stdout
    new_stdout = io.StringIO()
    sys.stdout = new_stdout
    
    try:
        # Execute the user's code
        exec(code_input)
        # Capture output
        output = new_stdout.getvalue()
    except Exception as e:
        # Capture exceptions and display them
        output = f"Error: {str(e)}"
    finally:
        # Reset standard output to its default value
        sys.stdout = old_stdout

    # Display the output or error
    if output:
        st.subheader("Output:")
        st.code(output)
