
import re

def analyze_job_description(text):

    skills = [
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

    found_skills = [
        skill for skill in skills
        if re.search(
            r'(?<!\w)' + re.escape(skill) + r'(?!\w)',
            text,
            re.IGNORECASE
        )
    ]

    return {
        "required_skills": found_skills,
        "total_skills": len(found_skills)
    }
