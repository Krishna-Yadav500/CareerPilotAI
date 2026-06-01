from sentence_transformers import SentenceTransformer

from sklearn.metrics.pairwise import cosine_similarity


from sklearn.feature_extraction.text import TfidfVectorizer


import pandas as pd


def get_job_recommendations(
    resume_text,
    jobs_df,
    top_n=5
):

    documents = (
        [resume_text]
        +
        jobs_df["Description"].tolist()
    )

    vectorizer = TfidfVectorizer(
        stop_words="english"
    )

    vectors = vectorizer.fit_transform(
        documents
    )

    resume_vector = vectors[0]

    job_vectors = vectors[1:]

    similarities = cosine_similarity(
        resume_vector,
        job_vectors
    )[0]

    jobs_df = jobs_df.copy()

    jobs_df["Match Score"] = (
        similarities * 100
    )

    jobs_df = jobs_df.sort_values(
        by="Match Score",
        ascending=False
    )

    return jobs_df.head(top_n)