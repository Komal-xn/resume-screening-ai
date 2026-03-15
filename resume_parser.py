import os
import pdfplumber
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Job description
job_description = """
Looking for a Data Analyst with Python, SQL, Excel,
data visualization, and machine learning skills.
"""

resume_texts = []
resume_names = []

# Extract text from resumes
for file in os.listdir():
    if file.endswith(".pdf"):
        with pdfplumber.open(file) as pdf:
            text = ""
            for page in pdf.pages:
                if page.extract_text():
                    text += page.extract_text()

        resume_texts.append(text)
        resume_names.append(file)

# Combine resumes + job description
documents = resume_texts + [job_description]

# Convert text to vectors
vectorizer = TfidfVectorizer(stop_words="english")
vectors = vectorizer.fit_transform(documents)

# Compare resumes with job description
similarity = cosine_similarity(vectors[-1], vectors[:-1])

# Print ranking
scores = similarity[0]

results = list(zip(resume_names, scores))
results.sort(key=lambda x: x[1], reverse=True)

print("\nTop Matching Resumes:\n")

for name, score in results:
    print(name, "→", round(score * 100, 2), "% match")
