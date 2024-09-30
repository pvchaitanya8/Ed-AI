import base64
import streamlit as st
from Pages.Chat import chat
from Pages.Learn_page import Learn_page
from streamlit_option_menu import option_menu
from Pages.Mock_Interview_page_tr import Mock_Interview_page_tr
# from Pages.Mock_Assessment import Mock_Assessment
from Pages.Practice_MCQ_page import Practice_MCQ_page
from UI_Components.profile_pic import get_base64_image
from Pages.Practice_Coding_page import Practice_Coding_page
from Pages.Mock_Interview_page_hr import Mock_Interview_page_hr
def clear_and_rewrite_memory_of_navbar(file_path, new_content):
    with open(file_path, 'w') as file:
        file.write(new_content)

def read_memory_of_navbar(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return f"File '{file_path}' not found."
    except Exception as e:
        return f"An error occurred: {e}"
    
def load_image_as_base64(image_path):
    with open(image_path, "rb") as img_file:
        base64_string = base64.b64encode(img_file.read()).decode('utf-8')
    return f"data:image/png;base64,{base64_string}"

def navbar():
    memory_of_navbar = r'EXP\memory.txt'
    memory_of_selected_round = r'EXP\memory_1.txt'
    memory_of_select_button = r'EXP\memory select problem.txt'

    image_path = r"Static_Files\NavBar\Ed AI logo.png"
    profile_pic_url = r"Static_Files\NavBar\profile pic.png"
    encoded_image = load_image_as_base64(image_path)
    link_url = "https://github.com/pvchaitanya8?tab=repositories"

    query_params = st.query_params

    # Check if the memory has already been cleared in the session
    if 'memory_cleared' not in st.session_state:
        clear_and_rewrite_memory_of_navbar(memory_of_select_button, "None")
        st.session_state['memory_cleared'] = True

    if ("selected_image" not in query_params) and (read_memory_of_navbar(memory_of_select_button) == "None"):
        col1, col2, col3, col4 = st.columns([0.9, 7, 3, 0.6])

        with col1:
            st.markdown(f'<a href="{link_url}" target="_blank"><img src="{encoded_image}" style="max-width: 200%; height: auto; display: block; transform: translateY(15px);" width="100"></a>', unsafe_allow_html=True)

        with col2:
            selected = option_menu(
                menu_title=None, 
                options=["Learn", "Practice", "Mock Interview", "Chat"], 
                icons=["book", "pencil-square", "briefcase", "chat-dots"], 
                menu_icon="cast",
                default_index=0,
                orientation="horizontal",
            )
            clear_and_rewrite_memory_of_navbar(memory_of_navbar, selected)
            
        with col3:
            search_query = st.text_input("Search", placeholder="🔎 Search...", label_visibility="collapsed")
            st.markdown(
                """
                <style>
                    div[data-testid="stTextInput"] label {
                        display: none;
                    }
                </style>
                """,
                unsafe_allow_html=True
            )

        with col4:
            User_Display_Name = "Chaitanya"
            profile_pic_base64 = get_base64_image(profile_pic_url)

            st.markdown(
                f"""
                <style>
                .container {{
                    position: relative;
                    width: 50px; 
                    margin-left: auto;
                    margin-right: auto;
                    transition: opacity 0.3s ease-in-out;
                }}

                .circle-img {{
                    display: block;
                    border-radius: 50%;
                    width: 100%;
                }}

                .hover-text {{
                    position: absolute;
                    top: 50%;
                    left: 50%;
                    transform: translate(-50%, 88%);
                    color: #9e9fa3;
                    font-size: 16px;
                    text-align: center;
                    opacity: 0;
                    transition: opacity 0.3s ease-in-out;
                }}

                .container:hover {{
                    opacity: 0.8; 
                }}

                .container:hover .hover-text {{
                    opacity: 1;
                }}
                </style>

                <div class="container">
                    <img src="data:image/png;base64,{profile_pic_base64}" class="circle-img">
                    <div class="hover-text">{User_Display_Name}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

        st.markdown(
            """
            <style>
            .gradient-divider {
                height: 6px;
                border-radius: 15px;
                margin: 10px 0;
                background: linear-gradient(135deg, #18008b, #644bdc, #cebfff, #644bdc, #18008b);
                background-size: 200% 200%;
                box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
                animation: gradientFlow 3.5s ease-in-out infinite;
                transition: height 0.3s ease;
            }

            .gradient-divider:hover {
                height: 8px;
                box-shadow: 0px 6px 12px rgba(0, 0, 0, 0.3);
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
            selected_round = st.selectbox(
                "Select practice type",
                [
                    "📄 MCQs Practice",
                    "🧑‍💻 Coding Practice",
                ],
                label_visibility="collapsed"
            )
            if selected_round == "📄 MCQs Practice":
                temp_selected_round = "MCQs Practice"
            elif selected_round == "🧑‍💻 Coding Practice":
                temp_selected_round = "Coding Practice"
            clear_and_rewrite_memory_of_navbar(memory_of_selected_round, temp_selected_round)

            if selected_round == "📄 MCQs Practice":
                Practice_MCQ_page()
            elif selected_round == "🧑‍💻 Coding Practice":
                Practice_Coding_page()

        elif selected == "Mock Interview":
            selected_round = st.selectbox(
                "Select Interview Round",
                [
                    # "📃 MCQ Assessment Round",
                    # "📃 Coding Assessment Round",
                    "💻 Technical Interview Round",
                    "🧑‍💻 HR Interview Round"
                ]
            )
            # if selected_round == "📃 MCQ Assessment Round":
            #     Mock_Assessment()
            # elif selected_round == "📃 Coding Assessment Round":
            #     Mock_Assessment()
            if selected_round == "💻 Technical Interview Round":
                Mock_Interview_page_tr()
            elif selected_round == "🧑‍💻 HR Interview Round":
                Mock_Interview_page_hr()

        elif selected == "Chat":
            chat()
            
        if search_query:
            st.write(f"Search results for: {search_query}")
    elif read_memory_of_navbar(memory_of_navbar) == "Learn":
        Learn_page()
    elif read_memory_of_navbar(memory_of_navbar) == "Practice":
        selected_round = read_memory_of_navbar(memory_of_selected_round)
        if selected_round == "MCQs Practice":
            Practice_MCQ_page()
        elif selected_round == "Coding Practice":
            Practice_Coding_page()
