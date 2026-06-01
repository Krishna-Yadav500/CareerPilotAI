import google.generativeai as genai


genai.configure(
    api_key="AQ.Ab8RN6LgLVYAB4JmUbv98zGUgiqHuez7mNuXB49ZIx0xFtuEzw"
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