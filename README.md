# Resume Screening AI

This project builds an AI system that automatically ranks resumes based on how well they match a job description.

## Features
- Resume text processing
- TF-IDF vectorization
- Cosine similarity matching
- Candidate ranking

## Tech Stack
- Python
- NLP
- Scikit-learn
- Machine Learning
  ## Output Example

Top Matching Resumes:

22776912.pdf → 8.32 % match  
22450718.pdf → 7.22 % match  
20824105.pdf → 6.52 % match  
20024870.pdf → 6.23 % match  
20001721.pdf → 6.01 % match

## How to Run

1. Clone the repository

git clone https://github.com/Komal-xn/resume-screening-ai.git

2. Install dependencies

pip install -r requirements.txt

3. Run the script

py resume_parser.py

## Project Structure

resume-screening-ai
│
├── resume_parser.py      # Main script for resume screening
├── requirements.txt      # Required Python libraries
├── README.md             # Project documentation
└── sample resumes        # Resume PDFs used for testing

## Future Improvements

- Build a web interface using Streamlit
- Allow recruiters to upload resumes dynamically
- Extract specific skills like Python, SQL, etc.
- Improve ranking accuracy using advanced NLP models
