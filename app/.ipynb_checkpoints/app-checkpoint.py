import streamlit as st
import pandas as pd
import pdfplumber

from utils.job_matcher import (
    get_job_recommendations
)

from utils.ats_score import (
    calculate_ats_score,
    extract_skills
)

from utils.skill_gap import (
    find_missing_skills
)

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="CareerPilot AI",
    page_icon="🚀",
    layout="wide"
)

# =====================================
# LOAD SKILLS DATABASE
# =====================================

skills_df = pd.read_csv(
    "../Data/skills_database.csv"
)

skills_list = (
    skills_df["skill"]
    .dropna()
    .tolist()
)

jobs_df = pd.read_csv(
    "../Data/jobs.csv"
)

# =====================================
# SIDEBAR
# =====================================

st.sidebar.title("🚀 CareerPilot AI")

page = st.sidebar.selectbox(
    "Choose Module",
    [
        "Resume Upload",
        "ATS Score",
        "Skill Gap Analysis",
        "Job Recommendations",
        "Interview Questions",
        "Career Counseling"
    ]
)

# =====================================
# MAIN TITLE
# =====================================

st.title("🚀 CareerPilot AI")
st.subheader("AI-Powered Career Guidance Platform")

# =====================================
# RESUME UPLOAD PAGE
# =====================================

if page == "Resume Upload":

    st.header("📄 Upload Resume")

    uploaded_file = st.file_uploader(
        "Upload Your Resume (PDF)",
        type=["pdf"]
    )

    if uploaded_file:

        resume_text = ""

        with pdfplumber.open(uploaded_file) as pdf:

            for page_pdf in pdf.pages:

                page_text = page_pdf.extract_text()

                if page_text:
                    resume_text += page_text

        st.session_state["resume_text"] = resume_text

        st.success(
            "Resume Uploaded Successfully!"
        )

        st.subheader(
            "Resume Preview"
        )

        st.text_area(
            "Extracted Text",
            resume_text,
            height=350
        )

# =====================================
# ATS SCORE PAGE
# =====================================

elif page == "ATS Score":

    st.header("📄 ATS Score Checker")

    if "resume_text" not in st.session_state:

        st.warning(
            "Please upload your resume first."
        )

    else:

        job_description = st.text_area(
            "Paste Job Description Here",
            height=250
        )

        if st.button(
            "Calculate ATS Score"
        ):

            score, matched, missing = calculate_ats_score(
                st.session_state["resume_text"],
                job_description,
                skills_list
            )

            st.subheader(
                f"ATS Score: {score}%"
            )

            st.progress(
                int(score)
            )

            st.subheader(
                "✅ Matching Skills"
            )

            if len(matched) == 0:

                st.warning(
                    "No matching skills found."
                )

            else:

                for skill in matched:

                    st.markdown(
                        f"✅ {skill}"
                    )

            st.subheader(
                "❌ Missing Skills"
            )

            if len(missing) == 0:

                st.success(
                    "No missing skills found."
                )

            else:

                for skill in missing:

                    st.markdown(
                        f"❌ {skill}"
                    )

# =====================================
# SKILL GAP ANALYSIS
# =====================================

elif page == "Skill Gap Analysis":

    st.header(
        "🎯 Skill Gap Analysis"
    )

    if "resume_text" not in st.session_state:

        st.warning(
            "Please upload your resume first."
        )

    else:

        job_description = st.text_area(
            "Paste Job Description",
            height=250
        )

        if st.button(
            "Analyze Skill Gap"
        ):

            resume_skills = extract_skills(
                st.session_state["resume_text"],
                skills_list
            )

            jd_skills = extract_skills(
                job_description,
                skills_list
            )

            missing_skills = find_missing_skills(
                resume_skills,
                jd_skills
            )

            st.subheader(
                "📌 Missing Skills"
            )

            if len(missing_skills) == 0:

                st.success(
                    "No missing skills found!"
                )

            else:

                for skill in missing_skills:

                    st.markdown(
                        f"❌ {skill}"
                    )

            st.subheader(
                "✅ Existing Skills"
            )

            for skill in resume_skills:

                st.markdown(
                    f"✔️ {skill}"
                )

# =====================================
# PLACEHOLDER PAGES
# =====================================

# =====================================
# JOB RECOMMENDATIONS
# =====================================

elif page == "Job Recommendations":

    st.header("💼 Job Recommendations")

    if "resume_text" not in st.session_state:

        st.warning(
            "Please upload your resume first."
        )

    else:

        recommendations = get_job_recommendations(
            st.session_state["resume_text"],
            jobs_df,
            top_n=5
        )

        st.subheader(
            "Top Recommended Jobs"
        )

        for _, row in recommendations.iterrows():

            st.metric(
                row["Role"],
                f"{row['Match Score']:.2f}%"
            )
             

elif page == "Interview Questions":

    st.header(
        "🎤 Interview Questions"
    )

    st.info(
        "Coming in next step..."
    )

elif page == "Career Counseling":

    st.header(
        "🧠 Career Counseling"
    )

    st.info(
        "Coming in next step..."
    )