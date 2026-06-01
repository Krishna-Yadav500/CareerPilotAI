import streamlit as st
import pandas as pd
import pdfplumber

import plotly.express as px

from utils.job_matcher import (
    get_job_recommendations
)

from utils.career_counselor import (
    generate_career_roadmap
)

from utils.interview_generator import (
    generate_questions
)

from utils.course_recommender import (
    recommend_courses
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

st.markdown("""
<style>

.main {
    padding-top: 1rem;
}

.block-container {
    padding-top: 1rem;
}

</style>
""", unsafe_allow_html=True)

# =====================================
# LOAD SKILLS DATABASE
# =====================================

skills_df = pd.read_csv(
    "Data/skills_database.csv"
)

skills_list = (
    skills_df["skill"]
    .dropna()
    .tolist()
)

jobs_df = pd.read_csv(
    "Data/jobs.csv"
)

# =====================================
# SIDEBAR
# =====================================

st.sidebar.title("🚀 CareerPilot AI")

page = st.sidebar.selectbox(
    "Choose Module",
    [
        "Home",
        "Resume Upload",
        "ATS Score",
        "Skill Gap Analysis",
        "Job Recommendations",
        "Interview Questions",
        "Career Counseling",
        "Course Recommendations",
        "Dashboard"
    ]
)






# =====================================
# MAIN TITLE
# =====================================

# st.title("🚀 CareerPilot AI")
# st.subheader("AI-Powered Career Guidance Platform")

if page == "Home":

    st.title("🚀 CareerPilot AI")

    st.markdown("""
    ### Welcome to CareerPilot AI

    An AI-powered platform that helps students:

    ✅ Analyze Resume

    ✅ Calculate ATS Score

    ✅ Identify Skill Gaps

    ✅ Get Job Recommendations

    ✅ Practice Interviews

    ✅ Generate Career Roadmaps

    ✅ Find Learning Resources

    """)

    st.info(
        "Start by uploading your resume."
    )




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
             


# =====================================
# INTERVIEW QUESTIONS
# =====================================


elif page == "Interview Questions":

    st.header(
        "🎤 AI Interview Question Generator"
    )

    if "resume_text" not in st.session_state:

        st.warning(
            "Please upload your resume first."
        )

    else:

        role = st.selectbox(
            "Select Role",
            [
                "Machine Learning Intern",
                "Data Scientist",
                "AI Engineer",
                "Data Analyst",
                "Python Developer"
            ]
        )

        if st.button(
            "Generate Questions"
        ):

            with st.spinner(
                "Generating Questions..."
            ):

                questions = generate_questions(
                    st.session_state["resume_text"],
                    role
                )

            st.success(
                "Questions Generated"
            )

            st.write(
                questions
            )

            st.download_button(
                "Download Questions",
                questions,
                file_name="interview_questions.txt"
            )




            
# =====================================
#CAREER COUNSELING
# =====================================




elif page == "Career Counseling":

    st.header(
        "🧠 AI Career Counselor"
    )

    if "resume_text" not in st.session_state:

        st.warning(
            "Please upload your resume first."
        )

    else:

        role = st.selectbox(
            "Target Role",
            [
                "Machine Learning Engineer",
                "Data Scientist",
                "AI Engineer",
                "Data Analyst",
                "Python Developer",
                "Software Engineer"
            ]
        )

        timeline = st.selectbox(
            "Target Timeline",
            [
                "3 Months",
                "6 Months",
                "12 Months"
            ]
        )

        if st.button(
            "Generate Career Roadmap"
        ):

            with st.spinner(
                "Generating Roadmap..."
            ):

                roadmap = generate_career_roadmap(
                    st.session_state["resume_text"],
                    role,
                    timeline
                )

            st.success(
                "Roadmap Generated Successfully"
            )

            st.write(
                roadmap
            )

            st.download_button(
                "Download Roadmap",
                roadmap,
                file_name="career_roadmap.txt"
            )



# =====================================
#COURSE RECOMMENDATIONS
# =====================================



elif page == "Course Recommendations":

    st.header(
        "📚 AI Course Recommender"
    )

    skills_input = st.text_area(
        "Enter Missing Skills (comma separated)"
    )

    if st.button(
        "Recommend Courses"
    ):

        recommendations = recommend_courses(
            skills_input
        )

        st.write(
            recommendations
        )

        st.download_button(
            "Download Recommendations",
            recommendations,
            file_name="courses.txt"
        )




# =====================================
# DASHBOARD
# =====================================

elif page == "Dashboard":

    st.header("📊 CareerPilot Dashboard")

    if "resume_text" not in st.session_state:

        st.warning(
            "Please upload your resume first."
        )

    else:

        # ==========================
        # SKILLS ANALYSIS
        # ==========================

        resume_skills = extract_skills(
            st.session_state["resume_text"],
            skills_list
        )

        total_skills = len(
            resume_skills
        )

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Skills Detected",
                total_skills
            )

        with col2:

            st.metric(
                "Skills Database",
                len(skills_list)
            )

        # ==========================
        # PIE CHART
        # ==========================

        chart_data = {
            "Category": [
                "Detected Skills",
                "Remaining Skills"
            ],
            "Count": [
                total_skills,
                len(skills_list) - total_skills
            ]
        }

        fig = px.pie(
            chart_data,
            names="Category",
            values="Count",
            title="Skill Coverage Analysis"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        # ==========================
        # JOB RECOMMENDATIONS
        # ==========================

        recommendations = get_job_recommendations(
            st.session_state["resume_text"],
            jobs_df,
            top_n=5
        )

        st.subheader(
            "Top Recommended Jobs"
        )

        st.dataframe(
            recommendations,
            use_container_width=True
        )

        # ==========================
        # BAR CHART
        # ==========================

        fig2 = px.bar(
            recommendations,
            x="Role",
            y="Match Score",
            title="Top Job Match Scores"
        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )
