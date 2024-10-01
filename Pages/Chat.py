import time
import random
import streamlit as st
import re

def generate_response_socratic():
    """Generate a random response with a slight delay to simulate typing."""
    responses = [
        "generate_response_socratic | Hello there! How can I assist you today?",
        """generate_response_socratic | Here's a simple Python code snippet that prints "Hello, World!" to the console:

        ```python
        # This is a simple program that prints "Hello, World!"
        print("Hello, World!")
        ```
        """
    ]
    response = random.choice(responses)
    return response

def generate_response_non_socratic():
    """Generate a random response with a slight delay to simulate typing."""
    responses = [
        "generate_response_non_socratic | Hello there! How can I assist you today?",
        """generate_response_non_socratic | Here's a simple Python code snippet that prints "Hello, World!" to the console:

        ```python
        # This is a simple program that prints "Hello, World!"
        print("Hello, World!")
        ```
        """
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
        code_block_pattern = r'```python(.*?)```'
        parts = re.split(code_block_pattern, content, flags=re.DOTALL)
        
        for i, part in enumerate(parts):
            if i % 2 == 0:  # Regular text
                st.markdown(f'<div class="assistant-message">{part.strip()}</div>', unsafe_allow_html=True)
            else:  # Python code
                st.code(part.strip(), language='python')

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
