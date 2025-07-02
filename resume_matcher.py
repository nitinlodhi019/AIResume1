# resume_matcher.py
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


# This function will be called from app.py
def calculate_match_score(job_description_text, required_skills, resume_processed_text, resume_extracted_skills):
    # 1. Semantic Similarity using TF-IDF and Cosine Similarity
    documents = [job_description_text, resume_processed_text]

    # Initialize TF-IDF Vectorizer
    # You might want to use a pre-trained word embedding model (like Word2Vec or BERT)
    # for more advanced semantic understanding, especially for short texts or synonyms.
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(documents)

    # Calculate cosine similarity between job description and resume
    semantic_similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]

    # 2. Skill Matching (Rule-based)
    # Convert required skills to a set for faster lookup
    required_skills_set = set([skill.lower() for skill in required_skills])

    # Find how many required skills are present in the resume's extracted skills
    matched_required_skills = [
        skill for skill in required_skills_set
        if skill in [es.lower() for es in resume_extracted_skills]
    ]

    skill_match_percentage = 0
    if len(required_skills_set) > 0:
        skill_match_percentage = len(matched_required_skills) / len(required_skills_set)

    # 3. Combine Scores
    # You can assign weights to different components.
    # For example, semantic similarity might be 60% and skill match 40%.
    # Adjust weights based on your priorities and testing.

    # Example weighting:
    # If required skills are provided, give them more weight.
    # If only job description is provided, rely more on semantic similarity.

    if len(required_skills_set) > 0:
        # If specific skills are required, prioritize them
        combined_score = (semantic_similarity * 0.6 + skill_match_percentage * 0.4) * 100
    else:
        # If no specific skills are listed, rely solely on semantic similarity
        combined_score = semantic_similarity * 100

    # Ensure score is within 0-100 range
    final_score = np.clip(combined_score, 0, 100)

    return final_score, matched_required_skills
