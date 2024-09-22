import json
import streamlit as st

def Course_MCQ(test_file):
    with open(test_file, "r") as f:
        questions_data = json.load(f)

    questions = questions_data['questions']

    current_question_idx = st.session_state.get('current_question_idx', 0)
    if 'selected_answers' not in st.session_state:
        st.session_state['selected_answers'] = [None] * len(questions)
    selected_answers = st.session_state['selected_answers']

    def navigate(direction):
        if direction == "next" and current_question_idx < len(questions) - 1:
            st.session_state['current_question_idx'] = current_question_idx + 1
        elif direction == "prev" and current_question_idx > 0:
            st.session_state['current_question_idx'] = current_question_idx - 1
        else:
            st.session_state['current_question_idx'] = direction
        st.rerun()  # Trigger UI refresh after navigation

    def clear_answer():
        selected_answers[current_question_idx] = None
        st.rerun()  # Trigger UI refresh after clearing the answer

    st.markdown("<h2 style='text-align: center;'>MCQS</h2>", unsafe_allow_html=True)

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

    colq_1, colq_2 = st.columns([7, 3])
    with colq_1:
        st.markdown(f"### Question {current_question_idx + 1}:", unsafe_allow_html=True)
        st.markdown(f"<h4>{questions[current_question_idx]['question']}</h4>", unsafe_allow_html=True)

        selected_answer = st.radio(
            "", 
            questions[current_question_idx]['options'], 
            index=None if selected_answers[current_question_idx] is None else questions[current_question_idx]['options'].index(selected_answers[current_question_idx]),
            key=f"question_{current_question_idx}"
        )
        
        if selected_answer:
            selected_answers[current_question_idx] = selected_answer
            # Show immediate feedback
            if selected_answer == questions[current_question_idx]['answer']:
                st.success("Correct!")
                st.write(f"Explanation: {questions[current_question_idx]['explanation']}")
            else:
                st.error("Incorrect!")
                selected_option_key = selected_answer[0]  # Extracting the key ('A', 'B', etc.)
                explanation = questions[current_question_idx]['incorrect_explanation'].get(selected_option_key, "No explanation available.")
                st.write(f"Explanation: {explanation}")

    with colq_2:
        st.markdown("<h5>Jump to Question</h5>", unsafe_allow_html=True)
        cols = st.columns(5)
        for idx, question in enumerate(questions):
            with cols[idx % 5]:
                button_label = f"Q{idx + 1}"
                if st.button(button_label, key=f"q_btn_{idx}"):
                    navigate(idx)

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

    col1, col2, col3 = st.columns(3)

    with col1:
        if current_question_idx > 0:
            st.button("Previous", on_click=navigate, args=("prev",), use_container_width=True)

    with col2:
        if current_question_idx < len(questions) - 1:
            st.button("Next", on_click=navigate, args=("next",), use_container_width=True)

    with col3:
        st.button("Clear", on_click=clear_answer, use_container_width=True)

