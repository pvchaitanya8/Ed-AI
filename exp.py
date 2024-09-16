import os
import streamlit as st
import base64
import mimetypes

# Helper function to load and encode images in base64
def load_image_as_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

# Helper function to get the MIME type based on the file extension
def get_mime_type(filename):
    mime_type, _ = mimetypes.guess_type(filename)
    return mime_type or 'application/octet-stream'

def Learn_page():
    # Define the directory_Featured containing the images
    directory_Featured = r"Static_Files\Learn_Page\Featured"
    directory_All_Courses = r"Static_Files\Learn_Page\All_Courses"

    if os.path.exists(directory_Featured):
        # Image dimensions and margin
        image_width = 550
        image_height = 350
        margin_right = 3  # Gap between images

        # Prepare image tags and calculate total width
        image_tags = ""
        filenames = sorted(os.listdir(directory_Featured))
        N = 0  # Number of images
        for i, filename in enumerate(filenames):
            file_path = os.path.join(directory_Featured, filename)
            if os.path.isfile(file_path):
                N += 1
                encoded_image = load_image_as_base64(file_path)
                mime_type = get_mime_type(filename)
                # Remove margin-right for the last image in the sequence
                margin_style = f"margin-right: {margin_right}px;" if i < len(filenames) - 1 else ""
                image_tags += f'<img src="data:{mime_type};base64,{encoded_image}" alt="{filename}" style="{margin_style}">'

        # Calculate total width of one set of images (including margins)
        total_width = N * image_width + (N - 1) * margin_right

        # Duplicate images for seamless scrolling
        full_image_tags = image_tags + image_tags

        # Insert CSS with dynamic total_width
        st.markdown(f"""
        <style>
        .scroll-container {{
            overflow: hidden;
            position: relative;
            width: 100%;
        }}

        .scroll-content {{
            display: flex;
            width: {2 * total_width}px; /* Double the total width */
            animation: scroll 30s linear infinite; /* Adjust duration as needed */
            transition: transform 0.5s ease;
        }}

        .scroll-content img {{
            width: {image_width}px;
            height: {image_height}px;
            object-fit: cover;
            border-radius: 3px;
            flex-shrink: 0; /* Prevent images from shrinking */
            transition: transform 0.4s ease, border-radius 1s ease;
        }}

        .scroll-container:hover .scroll-content {{
            animation-play-state: paused; /* Pause animation on hover */
        }}

        .scroll-content img:hover {{
            transform: scale(0.9); /* Magnify the image on hover */
            border-radius: 11px;
        }}

        @keyframes scroll {{
            0% {{
                transform: translateX(0);
            }}
            100% {{
                transform: translateX(-{total_width}px);
            }}
        }}
        </style>
        """, unsafe_allow_html=True)

        # Create the scrolling container
        st.markdown(f"""
        <div class="scroll-container">
            <div class="scroll-content">
                {full_image_tags}
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.error(f"Directory not found: {directory_Featured}")

    # "Recommendation" Section
    st.title("Recommendation")

    # Image gallery for all courses (Static image gallery)
    if os.path.exists(directory_All_Courses):
        # Image dimensions and margin
        image_width = 480 
        image_height = 230
        margin_right = 10  # Gap between images

        # Prepare image tags
        image_tags = ""
        filenames = sorted(os.listdir(directory_All_Courses))
        for i, filename in enumerate(filenames):
            file_path = os.path.join(directory_All_Courses, filename)
            if os.path.isfile(file_path):
                encoded_image = load_image_as_base64(file_path)
                mime_type = get_mime_type(filename)
                # Remove margin-right for the last image in the sequence
                margin_style = f"margin-right: {margin_right}px;" if i < len(filenames) - 1 else ""
                image_tags += f'<img src="data:{mime_type};base64,{encoded_image}" alt="{filename}" style="border-radius: 3px; {margin_style} width: {image_width}px; height: {image_height}px; object-fit: cover; vertical-align: middle;">'

        # Insert CSS for the scrollable container with hover effects
        st.markdown(f"""
        <style>
        .scroll-container-static {{
            overflow-x: auto;
            white-space: nowrap;
            -webkit-overflow-scrolling: touch;
            padding-bottom: 10px;
            margin-bottom: 20px;
        }}

        .scroll-content-static img {{
            display: inline-block;
            width: {image_width}px;
            height: {image_height}px;
            object-fit: cover;
            border-radius: 30px;
            margin-right: {margin_right}px;
            vertical-align: middle;
            transition: transform 0.3s ease, box-shadow 0.3s ease, border-radius 1s ease; /* Smooth transition for hover effects */
        }}

        .scroll-content-static img:hover {{
            transform: scale(0.95); /* Slightly increase the size on hover */
            box-shadow: 0px 4px 15px rgba(227, 194, 250, 0.8); /* Add shadow on hover */
        }}

        /* Dark themed scrollbar with rounded corners */
        .scroll-container-static::-webkit-scrollbar {{
            height: 8px;
        }}

        .scroll-container-static::-webkit-scrollbar-track {{
            background: #333;  /* Dark background for the track */
            border-radius: 20px; /* This does not affect the visual on some browsers */
        }}

        .scroll-container-static::-webkit-scrollbar-thumb {{
            background: #555;  /* Darker thumb */
            border-radius: 10px;
            border: 2px solid #333; /* Add a border to the thumb to visually create the effect of rounded corners */
        }}

        .scroll-container-static::-webkit-scrollbar-thumb:hover {{
            background: #888;  /* Slightly lighter on hover */
        }}

        .scroll-container-static {{
            scrollbar-width: thin;  /* Firefox */
            scrollbar-color: #555 #333;  /* Darker colors for Firefox */
            border-radius: 10px; /* This will only affect the container, not the scrollbar itself */
        }}
        </style>
        """, unsafe_allow_html=True)

        # Create the scrollable container
        st.markdown(f"""
        <div class="scroll-container-static">
            <div class="scroll-content-static">
                {image_tags}
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.error(f"Directory not found: {directory_All_Courses}")

    # "All Courses" Section
    st.title("All Courses")

    # Image gallery for all courses (Static image gallery)
    if os.path.exists(directory_All_Courses):
        # Image dimensions and margin
        image_width = 480 
        image_height = 230
        margin_right = 10  # Gap between images

        # Prepare image tags
        image_tags = ""
        filenames = sorted(os.listdir(directory_All_Courses))
        for i, filename in enumerate(filenames):
            file_path = os.path.join(directory_All_Courses, filename)
            if os.path.isfile(file_path):
                encoded_image = load_image_as_base64(file_path)
                mime_type = get_mime_type(filename)
                # Remove margin-right for the last image in the sequence
                margin_style = f"margin-right: {margin_right}px;" if i < len(filenames) - 1 else ""
                image_tags += f'<img src="data:{mime_type};base64,{encoded_image}" alt="{filename}" style="border-radius: 3px; {margin_style} width: {image_width}px; height: {image_height}px; object-fit: cover; vertical-align: middle;">'

        # Insert CSS for the scrollable container with hover effects
        st.markdown(f"""
        <style>
        .scroll-container-static {{
            overflow-x: auto;
            white-space: nowrap;
            -webkit-overflow-scrolling: touch;
            padding-bottom: 10px;
            margin-bottom: 20px;
        }}

        .scroll-content-static img {{
            display: inline-block;
            width: {image_width}px;
            height: {image_height}px;
            object-fit: cover;
            border-radius: 30px;
            margin-right: {margin_right}px;
            vertical-align: middle;
            transition: transform 0.3s ease, box-shadow 0.3s ease, border-radius 1s ease; /* Smooth transition for hover effects */
        }}

        .scroll-content-static img:hover {{
            transform: scale(0.95); /* Slightly increase the size on hover */
            box-shadow: 0px 4px 15px rgba(227, 194, 250, 0.8); /* Add shadow on hover */
        }}

        /* Dark themed scrollbar with rounded corners */
        .scroll-container-static::-webkit-scrollbar {{
            height: 8px;
        }}

        .scroll-container-static::-webkit-scrollbar-track {{
            background: #333;  /* Dark background for the track */
            border-radius: 20px; /* This does not affect the visual on some browsers */
        }}

        .scroll-container-static::-webkit-scrollbar-thumb {{
            background: #555;  /* Darker thumb */
            border-radius: 10px;
            border: 2px solid #333; /* Add a border to the thumb to visually create the effect of rounded corners */
        }}

        .scroll-container-static::-webkit-scrollbar-thumb:hover {{
            background: #888;  /* Slightly lighter on hover */
        }}

        .scroll-container-static {{
            scrollbar-width: thin;  /* Firefox */
            scrollbar-color: #555 #333;  /* Darker colors for Firefox */
            border-radius: 10px; /* This will only affect the container, not the scrollbar itself */
        }}
        </style>
        """, unsafe_allow_html=True)

        # Create the scrollable container
        st.markdown(f"""
        <div class="scroll-container-static">
            <div class="scroll-content-static">
                {image_tags}
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.error(f"Directory not found: {directory_All_Courses}")

Learn_page()