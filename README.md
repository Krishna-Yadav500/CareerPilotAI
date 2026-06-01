 # 🚀 CareerPilot AI – AI-Powered Career Guidance Platform

CareerPilot AI is an intelligent end-to-end career guidance system that helps students and job seekers analyze resumes, identify skill gaps, and receive personalized job recommendations, interview preparation, and career roadmaps using AI.

Built using **Python, Streamlit, Machine Learning, NLP, and Google Gemini AI**, this project transforms a simple resume into actionable career insights.

---

## 🌟 Live Features

### 📄 Resume Analyzer
- Upload PDF resumes
- Extract and process text using NLP

### 📊 ATS Score Checker
- Compares resume with job description
- Generates ATS compatibility score
- Shows matching and missing skills

### 🎯 Skill Gap Analysis
- Identifies missing skills for target roles
- Helps users improve employability

### 💼 Job Recommendation Engine
- Suggests relevant jobs based on resume
- Uses TF-IDF + Cosine Similarity

### 🎤 AI Interview Question Generator
- Generates:
  - Technical Questions
  - HR Questions
  - Project-based Questions
- Powered by Google Gemini AI

### 🧠 AI Career Counselor
- Provides personalized career roadmap
- Suggests skills, certifications, and projects
- Includes weekly learning plan

### 📚 Course Recommender
- Suggests courses based on skill gaps
- Provides certifications and project ideas

### 📊 Analytics Dashboard
- Skill distribution visualization
- ATS score insights
- Job match analysis using interactive charts

---

## 🛠️ Tech Stack

- **Frontend/UI:** Streamlit  
- **Backend:** Python  
- **Machine Learning:** Scikit-learn  
- **NLP:** TF-IDF Vectorization  
- **AI Integration:** Google Gemini API  
- **Visualization:** Plotly  
- **Data Handling:** Pandas, NumPy  

---

## 🧠 Key Concepts Used

- Natural Language Processing (NLP)
- TF-IDF Vectorization
- Cosine Similarity
- Prompt Engineering
- AI-based content generation
- Streamlit session state management
- Modular Python architecture

---

## 📂 Project Structure
## 📂 Project Structure


CareerPilotAI/
│
├── app/
│ ├── app.py
│ └── utils/
│ ├── ats_score.py
│ ├── skill_gap.py
│ ├── job_matcher.py
│ ├── interview_generator.py
│ ├── career_counselor.py
│ └── course_recommender.py
│
├── data/
│ ├── jobs.csv
│ └── skills_database.csv
│
├── models/
├── notebooks/
├── .streamlit/
│ └── secrets.toml
└── README.md




---

## 🚀 How to Run Locally

### 1️⃣ Clone Repository
bash
git clone https://github.com/your-username/CareerPilotAI.git
cd CareerPilotAI

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run Streamlit App
streamlit run app/app.py

🔐 API Key Setup (Important)

Create a file:

.streamlit/secrets.toml

Add:

GEMINI_API_KEY="your_api_key_here"


📌 Future Improvements
Resume ranking system for companies
Live job scraping from portals
BERT-based semantic matching
User authentication system
Multi-language support
🎯 Project Impact

CareerPilot AI helps users:

Improve resume quality
Identify skill gaps
Prepare for interviews
Get better job matches
Build structured career roadmaps


👨‍💻 Author
Krishna Yadav
B.Tech CSE (3rd Year)
AI/ML Enthusiast
