import streamlit as st
import pandas as pd

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

def difficulty_bg_color(difficulty):
    if difficulty == "Easy":
        return 'background-color: rgba(0, 255, 0, 0.5); color: white; font-weight: bold; border-radius: 30px; padding: 5px;'
    elif difficulty == "Medium":
        return 'background-color: rgba(249, 105, 14, 0.75); color: white; font-weight: bold; border-radius: 30px; padding: 5px;'
    elif difficulty == "Hard":
        return 'background-color: rgba(255, 0, 0, 0.5); color: white; font-weight: bold; border-radius: 30px; padding: 5px;'
    return ''

st.markdown("""<hr style="border: 2px solid grey; border-radius: 5px;">""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns([1, 4, 2, 2])
with col1:
    st.subheader("S no.")
with col2:
    st.subheader("Title")
with col3:
    st.subheader("Difficulty")
with col4:
    st.subheader("Select")
st.markdown("""<hr style="border: 2px solid grey; border-radius: 5px;">""", unsafe_allow_html=True)

for i, row in df.iterrows():
    col1, col2, col3, col4 = st.columns([1, 4, 2, 2])
    with col1:
        st.write(row["S no."])
    with col2:
        st.write(row["Title"])
    with col3:
        st.markdown(f'<div style="{difficulty_bg_color(row["Difficulty"])} text-align: center;">{row["Difficulty"]}</div>', unsafe_allow_html=True)
    with col4:
        if st.button("Solve 💻", key=f"button_{i}"):
            st.write(f"You clicked on problem: {row['Title']}")

    st.divider()
