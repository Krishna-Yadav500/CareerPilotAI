import streamlit as st

import google.generativeai as genai




genai.configure(
    api_key=st.secrets["GEMINI_API_KEY"]
)




model = genai.GenerativeModel(
    "models/gemini-2.5-flash"
)


def generate_career_roadmap(
    resume_text,
    target_role,
    timeline
):

    prompt = f"""
    You are an expert AI Career Counselor.

    Resume:

    {resume_text}

    Target Role:

    {target_role}

    Timeline:

    {timeline}

    Generate:

    1. Career Readiness Score (0-100)

    2. Missing Skills

    3. Learning Roadmap

    4. Recommended Certifications

    5. Recommended Projects

    6. Interview Preparation Plan

    7. Weekly Study Schedule

    Return in a clean professional format.
    """

    response = model.generate_content(
        prompt
    )

    return response.text