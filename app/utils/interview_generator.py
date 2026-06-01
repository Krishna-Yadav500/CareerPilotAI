import streamlit as st
import google.generativeai as genai



genai.configure(
    api_key=st.secrets["GEMINI_API_KEY"]
)



model = genai.GenerativeModel(
    "models/gemini-2.5-flash"
)


def generate_questions(
    resume_text,
    target_role
):

    prompt = f"""
    You are an expert interviewer.

    Resume:

    {resume_text}

    Target Role:

    {target_role}

    Generate:

    5 Technical Questions

    5 HR Questions

    5 Project-Based Questions

    Return in clear format.
    """

    response = model.generate_content(
        prompt
    )

    return response.text