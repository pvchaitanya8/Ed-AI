import streamlit as st
import json
import time

def Assignment_MCQ(test_file):
    # Load the JSON data
    with open(test_file, "r") as f:
        questions_data = json.load(f)

    # Sample questions from easy level
    questions = questions_data['questions']

    # Variables to store current question, answers, and timer
    current_question_idx = st.session_state.get('current_question_idx', 0)
    if 'selected_answers' not in st.session_state:
        st.session_state['selected_answers'] = [None] * len(questions)
    selected_answers = st.session_state['selected_answers']

    # Timer setup (30 minutes countdown)
    if 'timer_end_time' not in st.session_state:
        st.session_state['timer_end_time'] = time.time() + 30 * 60  # 30 minutes

    # Create a placeholder for the timer
    timer_placeholder = st.empty()

    # Function to navigate through questions
    def navigate(direction):
        if direction == "next" and current_question_idx < len(questions) - 1:
            st.session_state['current_question_idx'] = current_question_idx + 1
        elif direction == "prev" and current_question_idx > 0:
            st.session_state['current_question_idx'] = current_question_idx - 1
        else:
            st.session_state['current_question_idx'] = direction  # For question number navigation

    # Function to clear answer for the current question
    def clear_answer():
        selected_answers[current_question_idx] = None

    # Page layout starts here
    st.markdown("<h2 style='text-align: center;'>MCQS</h2>", unsafe_allow_html=True)

    # Timer at the top
    with st.container():
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

        st.write(f"**Time left:** ⏳ {divmod(max(0, int(st.session_state['timer_end_time'] - time.time())), 60)[0]}:{divmod(max(0, int(st.session_state['timer_end_time'] - time.time())), 60)[1]:02d}")

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


    # Main content layout
    colq_1, colq_2 = st.columns([7, 3])
    with colq_1:
        # Display the current question
        st.markdown(f"### Question {current_question_idx + 1}:", unsafe_allow_html=True)
        st.markdown(f"<h4>{questions[current_question_idx]['question']}</h4>", unsafe_allow_html=True)

        # Display answer options as radio buttons
        selected_answer = st.radio(
            "", 
            questions[current_question_idx]['options'], 
            index=questions[current_question_idx]['options'].index(selected_answers[current_question_idx]) if selected_answers[current_question_idx] else 0,
            key=f"question_{current_question_idx}"
        )
        # Store the selected answer
        if selected_answer:
            selected_answers[current_question_idx] = selected_answer

    with colq_2:
        # Create the question number navigation grid
        st.markdown("<h5>Jump to Question</h5>", unsafe_allow_html=True)
        cols = st.columns(5)
        for idx, question in enumerate(questions):
            with cols[idx % 5]:
                button_label = f"Q{idx + 1}"
                if st.button(button_label, key=f"q_btn_{idx}"):
                    navigate(idx)

    # Create the bottom navigation buttons
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


    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if current_question_idx > 0:
            st.button("Previous", on_click=navigate, args=("prev",), use_container_width=True)

    with col2:
        if current_question_idx < len(questions) - 1:
            st.button("Next", on_click=navigate, args=("next",), use_container_width=True)

    with col3:
        st.button("Clear", on_click=clear_answer, use_container_width=True)

    with col4:
        st.button("Submit", key="submit", use_container_width=True)

    # Submit logic
    if st.session_state.get('submit', False):
        correct_count = 0
        for idx, question in enumerate(questions):
            if selected_answers[idx] == question['answer']:
                correct_count += 1
            else:
                st.write(f"Question {idx + 1}: {question['question']}")
                st.write(f"Your Answer: {selected_answers[idx]}")
                st.write(f"Correct Answer: {question['answer']}")
                # Safely access the 'incorrect_explanation' with a default value
                incorrect_explanations = question.get('incorrect_explanation', {})
                explanation = incorrect_explanations.get(selected_answers[idx], 'N/A')
                st.write(f"Explanation: {explanation}")
        st.write(f"**Score: {correct_count} / {len(questions)}**")


    # Timer logic with continuous update
    while True:
        timer_end_time = st.session_state['timer_end_time']
        time_left = max(0, int(timer_end_time - time.time()))

        if time_left == 0:
            st.warning("Time's up! Submitting automatically.")
            st.session_state['submit'] = True
            st.rerun()  # Force the app to refresh and submit when the timer runs out
        
        # Update the timer continuously
        minutes, seconds = divmod(time_left, 60)
    
        time.sleep(1)
        st.rerun()
        