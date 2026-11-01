
import re

SKILLS = [
    "Python", "SQL", "Java", "JavaScript",
    "Flask", "FastAPI", "Django",
    "Pandas", "NumPy", "Scikit-learn",
    "Machine Learning", "Deep Learning",
    "NLP", "LangChain", "RAG",
    "Power BI", "Excel", "AWS",
    "Docker", "Git", "MongoDB",
    "MySQL", "TensorFlow", "PyTorch",
    "Transformers", "ChromaDB", "FAISS"
]


def extract_resume_details(text):

    # Extract email
    email = re.findall(
        r'[\w.+-]+@[\w.-]+\.[a-zA-Z]{2,}',
        text
    )

    # Extract phone number
    phone = re.findall(
        r'(?<!\d)(?:\+91[-\s]?)?[6-9]\d{9}(?!\d)',
        text
    )

    # Extract technical skills
    found_skills = [
        skill for skill in SKILLS
        if re.search(
            r'(?<!\w)' + re.escape(skill) + r'(?!\w)',
            text,
            re.IGNORECASE
        )
    ]

    # Extract experience
    experience = re.findall(
        r'\d+(?:\.\d+)?\+?\s*(?:years?|yrs?)',
        text,
        re.IGNORECASE
    )

    # Extract education-related lines
    education_keywords = [
        "bachelor", "master", "degree",
        "b.tech", "b.e.", "mba",
        "bsc", "msc", "education"
    ]

    education = [
        line.strip()
        for line in text.splitlines()
        if any(word in line.lower()
               for word in education_keywords)
    ]

    return {
        "email": email[0] if email else "Not found",
        "phone": phone[0] if phone else "Not found",
        "skills": found_skills,
        "experience": experience,
        "education": education
    }
