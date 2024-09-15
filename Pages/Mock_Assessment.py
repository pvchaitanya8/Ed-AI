import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase

def Mock_Assessment():
    col1, col2 = st.columns([5, 4])
    with col1:
        hardness = st.selectbox("Select the hardness level:", ["😉 Easy", "👍 Medium", "💪 Hard"])
        
        comments = st.text_area("Anything you'd like to say? (Optional)")
        
    with col2:
        topics = st.multiselect(
            "Select the topics you are interested in:", 
            ["Trees", "Graphs", "Arrays", "Linked Lists", "Stacks", "Queue"]
        )
            
        uploaded_file = st.file_uploader("Upload your resume", type="pdf")
        

    st.markdown("---")

    if st.button("Let's Start the Assessment"):
        # Print out the inputs
        st.write("Hardness:", hardness)
        st.write("Topics selected:", ", ".join(topics) if topics else "None")
        st.write("Additional comments:", comments if comments else "None")

        if uploaded_file is not None:
            st.write("Resume uploaded successfully!")
        else:
            st.write("No resume uploaded.")
