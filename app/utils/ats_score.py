def calculate_ats_score(
    resume_skills,
    jd_skills
):

    score = (
        len(
            set(resume_skills)
            &
            set(jd_skills)
        )
        /
        len(jd_skills)
    ) * 100

    return round(score,2)


import re

def extract_skills(text, skills_list):

    text = text.lower()

    found_skills = []

    for skill in skills_list:

        if skill.lower() in text:
            found_skills.append(skill)

    return list(set(found_skills))


def calculate_ats_score(
    resume_text,
    job_description,
    skills_list
):

    resume_skills = extract_skills(
        resume_text,
        skills_list
    )

    jd_skills = extract_skills(
        job_description,
        skills_list
    )

    matched = list(
        set(resume_skills)
        &
        set(jd_skills)
    )

    missing = list(
        set(jd_skills)
        -
        set(resume_skills)
    )

    if len(jd_skills) == 0:

        score = 0

    else:

        score = (
            len(matched)
            /
            len(jd_skills)
        ) * 100

    return (
        round(score, 2),
        matched,
        missing
    )