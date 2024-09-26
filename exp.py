import json
import streamlit as st
import pandas as pd
from Sub_Pages.Coding_Problems_Page import Coding_Problems_page

def clear_and_rewrite_memory_of_navbar(file_path, new_content):
    with open(file_path, 'w') as file:
        file.write(new_content)

def Practice_Coding_page():
    memory_of_select_button = r'EXP\memory select problem.txt'
    st.title("All Coding Problems")

    # Initialize Session State for navigation
    if 'selected_problem' not in st.session_state:
        st.session_state.selected_problem = None
        clear_and_rewrite_memory_of_navbar(memory_of_select_button, str(st.session_state.selected_problem))

    # Sample Data
    data = {
        "S no.": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"],
        "Title": [
            "Find the Longest Substring Containing",
            "Two Sum",
            "Add Two Numbers",
            "Longest Substring Without Repeating",
            "Median of Two Sorted Arrays",
            "Longest Palindromic Substring",
            "Zigzag Conversion",
            "Reverse Integer",
            "String to Integer (atoi)",
            "Palindrome Number",
            "Regular Expression Matching",
            "Container With Most Water",
            "Integer to Roman",
            "Roman to Integer",
            "Longest Common Prefix"
        ],
        "Difficulty": ["Medium", "Easy", "Medium", "Medium", "Hard", "Medium", "Medium", "Medium", "Medium", "Easy", "Hard", "Medium", "Medium", "Easy", "Easy"]
    }

    df = pd.DataFrame(data)

    # Filtering Mechanism
    difficulty_filter = st.selectbox("Filter by Difficulty:", ["All", "Easy", "Medium", "Hard"], index=0)

    if difficulty_filter != "All":
        df = df[df["Difficulty"] == difficulty_filter]

    # Function to Style Difficulty Labels
    def difficulty_bg_color(difficulty):
        if difficulty == "Easy":
            return 'background-color: rgba(0, 200, 0, 0.7); color: white; font-weight: bold; border-radius: 30px; padding: 5px; text-align: center;'
        elif difficulty == "Medium":
            return 'background-color: rgba(249, 105, 14, 0.75); color: white; font-weight: bold; border-radius: 30px; padding: 5px; text-align: center;'
        elif difficulty == "Hard":
            return 'background-color: rgba(255, 0, 0, 0.7); color: white; font-weight: bold; border-radius: 30px; padding: 5px; text-align: center;'
        return ''

    # Styling and Headers
    st.markdown("""
        <style>
            .problem-row { margin-bottom: 10px; }
            .solve-button { text-align: center; }
        </style>
        <hr style='border: 2px solid #ccc; border-radius: 5px;'>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns([1, 5, 2, 2])
    with col1:
        st.subheader("S no.")
    with col2:
        st.subheader("Title")
    with col3:
        st.subheader("Difficulty")
    with col4:
        st.subheader("Action")
    
    st.markdown("<hr style='border: 1px solid #ddd;'>", unsafe_allow_html=True)

    # Displaying the List of Problems
    for i, row in df.iterrows():
        col1, col2, col3, col4 = st.columns([1, 5, 2, 2])

        with col1:
            st.markdown(f"<p style='text-align: center;'>{row['S no.']}</p>", unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"<p style='font-size: 16px; text-align: left;'>{row['Title']}</p>", unsafe_allow_html=True)
        
        with col3:
            st.markdown(f"<div style='{difficulty_bg_color(row['Difficulty'])}'>{row['Difficulty']}</div>", unsafe_allow_html=True)
        
        with col4:
            if st.button(f"Solve 💻", key=f"button_{i}"):
                st.session_state.selected_problem = row.to_dict()
                clear_and_rewrite_memory_of_navbar(memory_of_select_button, str(st.session_state.selected_problem))
                st.rerun()

        st.markdown("<hr style='border: 1px solid #eee;'>", unsafe_allow_html=True)

    # Conditional Rendering: Show Problem Page if a Problem is Selected
    if st.session_state.selected_problem:
        selected = st.session_state.selected_problem
        st.markdown("<hr style='border: 2px solid #ccc; border-radius: 5px;'>", unsafe_allow_html=True)
        st.header(f"Solve: {selected['Title']}")

        # Load Problem Details from JSON
        try:
            with open(r'EXP\Redirecting_test_problem.json', 'r') as file:
                data = json.load(file)

            problem_title = data["title"]
            problem_problem_description = data["Problem_Description"]
            problem_test_cases = data["Test_Cases"]

            Coding_Problems_page(problem_problem_description, problem_title, problem_test_cases)
        
        except FileNotFoundError:
            st.error("Problem details file not found.")

        # Option to Go Back to the List
        if st.button("Back to All Problems"):
            st.session_state.selected_problem = None
            st.rerun()

Practice_Coding_page()
