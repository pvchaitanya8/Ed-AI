import time
import random
import streamlit as st

def generate_response_socratic():
    """Generate a random response with a slight delay to simulate typing."""
    responses = [
        "socratic | Hello there! How can I assist you today?",
        "socratic | Hi, human! Is there anything I can help you with?",
        "socratic | Do you need help?",
    ]
    response = random.choice(responses)
    return response

def generate_response_non_socratic():
    """Generate a random response with a slight delay to simulate typing."""
    responses = [
        "Hello there! How can I assist you today?",
        "Hi, human! Is there anything I can help you with?",
        "Do you need help?",
    ]
    response = random.choice(responses)
    return response

def chat():
    toggle_socratic = st.toggle("Socratic Mode", value=True)

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


    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        if message["role"] == "assistant":
            st.markdown(f'<div class="assistant-message">{message["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="user-message">{message["content"]}</div>', unsafe_allow_html=True)


    prompt = st.chat_input("What’s on your mind?")
    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.markdown(f'<div class="user-message">{prompt}</div>', unsafe_allow_html=True)

        if toggle_socratic:
            response_text = generate_response_socratic()
        else:
            response_text = generate_response_non_socratic()

        response_container = st.empty()

        partial_response = ""
        for word in response_text.split():
            partial_response += word + " "
            response_container.markdown(f'<div class="assistant-message">{partial_response}</div>', unsafe_allow_html=True)
            time.sleep(0.1)

        st.session_state.messages.append({"role": "assistant", "content": response_text})
        response_container.markdown(f'<div class="assistant-message">{response_text}</div>', unsafe_allow_html=True)
        st.rerun()