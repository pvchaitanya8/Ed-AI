import streamlit as st
import os
from dotenv import load_dotenv
from google_auth_oauthlib.flow import Flow
import google.auth.transport.requests

load_dotenv()
client_secrets_file = 'Login_Secret.json'

# Initialize the OAuth flow
flow = Flow.from_client_secrets_file(
    client_secrets_file,
    scopes=["openid", "https://www.googleapis.com/auth/userinfo.email", "https://www.googleapis.com/auth/userinfo.profile"],
    redirect_uri="http://localhost:8501"
)

st.set_page_config(page_title="Login Demo", layout="centered")

if 'login_status' not in st.session_state:
    st.session_state['login_status'] = False

if not st.session_state['login_status']:
    auth_url, _ = flow.authorization_url()

    # Custom CSS for the red button
    st.markdown("""
        <style>
        .button-container {
            display: flex;
            justify-content: center;
            margin-top: 20px;
        }
        </style>
        """, unsafe_allow_html=True)

    # Render the red button using inline HTML and CSS
    st.markdown(f'''
        <div class="button-container">
            <a href="{auth_url}" style="
                display: inline-block;
                background-color: red;
                color: white;
                border: none;
                padding: 10px 20px;
                text-align: center;
                text-decoration: none;
                font-size: 16px;
                cursor: pointer;
                border-radius: 50px;
            ">Login with Google</a>
        </div>
    ''', unsafe_allow_html=True)

    # Check for OAuth callback
    query_params = st.query_params
    if 'code' in query_params:
        code = query_params['code']
        try:
            flow.fetch_token(code=code)
            credentials = flow.credentials
            request = google.auth.transport.requests.Request()
            id_info = credentials.id_token

            if id_info:
                st.session_state['login_status'] = True
                st.rerun()  # Use rerun instead of rerun for Streamlit
        except Exception as e:
            st.error(f"Error during login: {e}")
            st.write("Ensure that the redirect URI matches the one configured in Google Cloud Console and that the authorization code is valid.")

else:
    st.title("Welcome to Your Dashboard!")
    st.write("You are now logged in with Google!")
