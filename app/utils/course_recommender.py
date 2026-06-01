import streamlit as st
import google.generativeai as genai



import streamlit as st

genai.configure(
    api_key=st.secrets["GEMINI_API_KEY"]
)



model = genai.GenerativeModel(
    "models/gemini-2.5-flash"
)


def recommend_courses(
    missing_skills
):

    prompt = f"""
    For these skills:

    {missing_skills}

    Recommend:

    1. Best Course
    2. Best Certification
    3. Best YouTube Resource
    4. One Mini Project

    Return in structured format.
    """

    response = model.generate_content(
        prompt
    )

    return response.text