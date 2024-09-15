import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase


def VideoTransformer(self, frame):
    return frame

def Mock_Interview():
    col1, col2 = st.columns([5, 4])
    with col1:
        hardness = st.selectbox("Select the hardness level:", ["😉 Easy", "👍 Medium", "💪 Hard"])
        
        comments = st.text_area("Anything you'd like to say? (Optional)")
        
    with col2:
        topics = st.multiselect(
            "Select the topics you are interested in:", 
            ["Trees", "Graphs", "Arrays", "Linked Lists", "Stacks", "Queue"]
        )
            
        st.markdown("""
            <style>
            .reduced-line-gap {
                margin-bottom: -20px;  /* Adjust this value to reduce or increase the gap */
            }
            </style>
            """, unsafe_allow_html=True)

        st.write('<div class="reduced-line-gap">select Video and Mic:</div>', unsafe_allow_html=True)
        webrtc_streamer(key="example", video_transformer_factory=VideoTransformer)

    uploaded_file = st.file_uploader("Upload your resume", type="pdf")
        

    st.markdown("---")

    if st.button("Let's Start the Interview"):
        # Print out the inputs
        st.write("Hardness:", hardness)
        st.write("Topics selected:", ", ".join(topics) if topics else "None")
        st.write("Additional comments:", comments if comments else "None")

        if uploaded_file is not None:
            st.write("Resume uploaded successfully!")
        else:
            st.write("No resume uploaded.")
