from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample resumes
resumes = [
    "Python SQL Excel data analysis machine learning pandas",
    "Java spring boot backend development microservices",
    "HR recruitment onboarding employee relations"
]

# Job description
job_description = """
Looking for a Data Analyst with Python, SQL, Excel and data visualization skills
"""

documents = resumes + [job_description]

tfidf = TfidfVectorizer()
vectors = tfidf.fit_transform(documents)

similarity = cosine_similarity(vectors[-1], vectors[:-1])

for i, score in enumerate(similarity[0]):
    print(f"Resume {i+1} Match Score: {score*100:.2f}%")
