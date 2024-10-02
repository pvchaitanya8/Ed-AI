
# **ED AI - AI-Powered Educational Platform**

**ED AI** is an AI-powered educational assistant designed to enhance the learning experience through personalized course recommendations, a Socratic method-based AI chat feature, and mock interviews. This project was developed to tackle educational challenges, particularly in personalized learning and scalable teaching assistance.

## **Table of Contents**
- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [Creating the `.env` File](#creating-the-env-file)
- [Running the Application](#running-the-application)
- [Challenges and Solutions](#challenges-and-solutions)
- [Future Opportunities](#future-opportunities)

## **Introduction**

ED AI leverages GenAI to personalize learning by providing students with real-time recommendations and engaging them in a Socratic-style conversation for learning complex topics like Data Structures and Algorithms. The mock interview feature simulates interview environments, helping users prepare for coding and technical interviews. ED AI aims to make learning more interactive and efficient through AI, providing a scalable solution to challenges in education.

## **Features**

1. **Personalized Learning Recommendations**: The platform tailors course suggestions to users based on their progress and learning preferences.
   
2. **Socratic Method AI Chat**: An AI assistant asks probing questions that guide learners through problems, helping them grasp complex concepts independently.

3. **AI-Powered Mock Interview**: Simulate coding and technical interviews to help students prepare for real-world challenges.

## **Technologies Used**

- **Python**
- **Streamlit**
- **JSON**
- **Git**

## **Setup Instructions**

### Prerequisites

- **Python 3.8+**
- **Gemini API Key** (for AI-powered features)

### Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/ed-ai.git
    cd ed-ai
    ```

2. **Create a Virtual Environment** (recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## **Creating the `.env` File**

To secure sensitive information such as API keys, follow the steps below to create and configure a `.env` file.

1. Inside the root of your project directory, create a file named `.env`:
    ```bash
    touch .env
    ```

2. Open the `.env` file and add the following line:
    ```
    GEMINI_API_KEY='your-gemini-api-key-here'
    ```

   Replace `your-gemini-api-key-here` with your actual Gemini API key.

3. Ensure that your `.env` file is included in `.gitignore` so that it is not pushed to version control:
    ```
    # .gitignore
    .env
    ```

## **Running the Application**

1. **Backend (Streamlit & Flask)**:
    ```bash
    streamlit run app.py
    ```

2. **Frontend (Flutter)**:
    ```bash
    flutter run
    ```

3. Access the platform on `localhost` or the specified port, e.g. `http://localhost:8501/`.

## **Challenges and Solutions**

- **Socratic AI Tuning**: It was a challenge to design the Socratic AI to ask insightful and contextually appropriate questions. This required fine-tuning the NLP model and testing with a variety of learning scenarios.  
- **Seamless Integration**: Balancing various modules like personalized learning, mock interviews, and Socratic chats was another challenge. We conducted multiple rounds of UI/UX testing to ensure that all the components were intuitive and fluid for users.

## **Future Opportunities**

- **Expansion to New Topics**: ED AI currently focuses on Data Structures and Algorithms. In the future, we aim to expand the Socratic method-based AI assistant to cover broader subjects, such as Machine Learning, Databases, and System Design.
  
- **Scalability for Large User Bases**: Future iterations will focus on optimizing the platform to handle a large number of users simultaneously without sacrificing performance.
  
- **Advanced Mock Interviews**: Adding new interview types such as behavioral and system design interviews would provide a more comprehensive experience for users preparing for real-world job opportunities.

---

By following these steps, you'll have **ED AI** up and running, enabling users to enjoy a personalized and interactive learning experience!