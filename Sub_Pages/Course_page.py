import streamlit as st
from UI_Components.Chat_Course import chat
from Sub_Pages.Course_MCQ import Course_MCQ
from Gen_Process.Learn_Recommendations import write_recommendation_data_to_Learn_file
import json

def update_problem_status(file_path, problem_id, completed_status):
    with open(file_path, 'r') as file:
        data = json.load(file)

    if problem_id in data:
        data[problem_id]['Completed'] = completed_status
        print(f"Updated {problem_id} to Completed = {completed_status}")
    else:
        return f"Problem ID {problem_id} not found in the data"

    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

    return "JSON file updated successfully."

def display_content(Course_list, MCQ_list, current_index, Tittle):
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

    # Alternate display between course and MCQ
    if current_index % 2 == 0:  # Even index for Course
        course_file = Course_list[current_index // 2]
        st.markdown(f'<h1 class="centered-title">{Tittle}</h1>', unsafe_allow_html=True)
        st.markdown(
            """
            <style>
            .gradient-divider-sidebar {
                height: 5px;
                border-radius: 15px;
                background: linear-gradient(to right, #212529, #343a40, #212529);
                margin: 30px 0;
                border: none;
            }
            </style>
            <div class="gradient-divider-sidebar"></div>
            """,
            unsafe_allow_html=True
        )
        try:
            with open(course_file, "r") as file:
                markdown_content = file.read()
            st.markdown(markdown_content)
        except FileNotFoundError:
            st.error(f"File not found: {course_file}")
    else:  # Odd index for MCQ
        mcq_file = MCQ_list[current_index // 2]
        st.markdown(f'<h1 class="centered-title">MCQ {current_index // 2 + 1}</h1>', unsafe_allow_html=True)
        Course_MCQ(mcq_file)  # Call the function to display MCQ content

def course_page(Course_list, MCQ_list, Tittle, Course_ID):
    # Initialize session state if it doesn't exist
    if 'current_index' not in st.session_state:
        st.session_state['current_index'] = 0

    # Cap the index within the bounds of Course_list and MCQ_list
    total_content = len(Course_list) + len(MCQ_list)
    if st.session_state['current_index'] >= total_content:
        st.session_state['current_index'] = total_content - 1

    # Call the separated display function
    display_content(Course_list, MCQ_list, st.session_state['current_index'], Tittle)


    # 'Next' button
    if st.button('Next Chapter', use_container_width=True):
        if st.session_state['current_index'] < total_content - 1:
            st.session_state['current_index'] += 1
            st.rerun()
        else:
            st.success("You have Completed the Course!")
            st.balloons()
            file_path = r'dynamic files\Main_pages\Learn.json'
            completed_status = True
            print(update_problem_status(file_path, Course_ID, completed_status))
            write_recommendation_data_to_Learn_file()
