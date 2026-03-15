import os
import pdfplumber

folder_path = "."

for file in os.listdir(folder_path):
    if file.endswith(".pdf"):
        with pdfplumber.open(file) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text()
        print("\n====================")
        print("Resume:", file)
        print(text[:500])
