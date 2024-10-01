import time
import random
import streamlit as st
import re
import textwrap

def generate_response_socratic():
    """Generate a random response with a slight delay to simulate typing."""
    responses = [
        textwrap.dedent("""\
            generate_response_socratic | Here's a simple Python code snippet that prints "Hello, World!" to the console:

            ```python
            # This is a simple program that prints "Hello, World!"
            print("Hello, World!")
            for i in range(2):
                print(i)
            ```
        """),

        textwrap.dedent("""\
        generate_response_non_socratic | Here’s a sample JSON response with user details:

        ```json
        {
            "name": "John Doe",
            "age": 30,
            "email": "johndoe@example.com",
            "is_verified": true,
            "address": {
                "street": "123 Main St",
                "city": "Anytown",
                "zip_code": "12345"
            }
        }
        ```
        The above JSON contains basic user information."""),

        textwrap.dedent("generate_response_socratic | Hello there! How can I assist you today?")
    ]
    response = random.choice(responses)
    return response

def generate_response_non_socratic():
    """Generate a random response with a slight delay to simulate typing."""
    responses = [
        textwrap.dedent("""\
            generate_response_non_socratic | Here's a simple Python code snippet that prints "Hello, World!" to the console:

            ```python
            # This is a simple program that prints "Hello, World!"
            print("Hello, World!")
            ```
        """),

        textwrap.dedent("""\
        generate_response_non_socratic | Here’s a sample JSON response with user details:

        ```json
        {
            "name": "John Doe",
            "age": 30,
            "email": "johndoe@example.com",
            "is_verified": true,
            "address": {
                "street": "123 Main St",
                "city": "Anytown",
                "zip_code": "12345"
            }
        }
        ```
        The above JSON contains basic user information."""),

        textwrap.dedent("generate_response_non_socratic | Hello there! How can I assist you today?")
    ]
    response = random.choice(responses)
    return response

def chat():
    toggle_socratic = st.toggle("Socratic Mode", value=True)

    # Custom CSS for chat UI
    st.markdown("""
        <style>
        .assistant-message {
            text-align: left !important;
            background: linear-gradient(135deg, #3d0e61, #613dc1); /* Gradient from dark blue to a lighter blue */
            color: white;
            padding: 12px;
            border-radius: 20px;
            margin: 5px 0;
            width: fit-content;
            max-width: 80%;
        }
        .user-message {
            text-align: right !important;
            background-color: #333333;
            color: white;
            padding: 12px;
            border-radius: 20px;
            margin: 5px 0;
            width: fit-content;
            max-width: 80%;
            margin-left: auto !important;
        }
        </style>
    """, unsafe_allow_html=True)

    # Initialize the session state for messages
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Function to separate text and code in the assistant's message
    def render_message(content):
        # Patterns to detect both Python and JSON code blocks
        code_block_pattern = r'```(python|json)(.*?)```'
        
        # Split the content by code blocks
        parts = re.split(code_block_pattern, content, flags=re.DOTALL)
        
        for i in range(0, len(parts), 3):
            text_part = parts[i].strip()  # Regular text
            if text_part:
                st.markdown(f'<div class="assistant-message">{text_part}</div>', unsafe_allow_html=True)
            
            if i + 1 < len(parts):
                language = parts[i + 1]  # Either 'python' or 'json'
                code_part = parts[i + 2].strip()  # Code block content
                if code_part:
                    st.code(code_part, language=language)

    # Display previous chat messages
    for message in st.session_state.messages:
        if message["role"] == "assistant":
            render_message(message["content"])
        else:
            st.markdown(f'<div class="user-message">{message["content"]}</div>', unsafe_allow_html=True)

    # User input section
    prompt = st.chat_input("What’s on your mind?")
    if prompt:
        # Store the user message in session state and render it
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.markdown(f'<div class="user-message">{prompt}</div>', unsafe_allow_html=True)

        # Generate a response based on the toggle
        if toggle_socratic:
            response_text = generate_response_socratic()
        else:
            response_text = generate_response_non_socratic()

        # Simulate assistant's typing effect with delay
        response_container = st.empty()
        partial_response = ""
        for word in response_text.split():
            partial_response += word + " "
            if "```python" in partial_response:
                # Display code block if detected in the message
                code_content = partial_response.split("```python")[1].split("```")[0]
                response_container.code(code_content, language='python')
            else:
                response_container.markdown(f'<div class="assistant-message">{partial_response}</div>', unsafe_allow_html=True)
            time.sleep(0.1)

        # Store the assistant's full response and render it completely
        st.session_state.messages.append({"role": "assistant", "content": response_text})
        render_message(response_text)

        # Rerun to update the chat UI
        st.rerun()
